"""Tests for `briefy.choreographer.worker` module."""
from briefy.choreographer.events import InternalEvent
from briefy.choreographer.worker import main
from briefy.choreographer.worker import Worker
from collections import defaultdict
from datetime import datetime
from unittest import mock

import pytest
import uuid


class AssertRead(dict):
    """A dictionary that counts the number of times each value was fetched."""

    def __init__(self, *args, **kw):
        """Initialize."""
        self.read_count = defaultdict(lambda: 0)
        super().__init__(*args, **kw)

    def __getitem__(self, key):
        """Get an item."""
        res = super().__getitem__(key)
        self.read_count[key] += 1
        return res

    def get(self, key, *args):
        """Get an item."""
        res = super().get(key, *args)
        self.read_count[key] += 1
        return res

    def reset(self):
        """Reset counters."""
        for key in self:
            self.read_count[key] = 0


class TestQueue:

    _messages = None

    def get_messages(self):
        return self._messages if self._messages else []

    def write_message(self, message):
        if not self._messages:
            self._messages = []

        self._message.append(message)


@pytest.fixture
def message():
    class DummyMessage:
        def __init__(self):
            self.body = AssertRead(
                event_name='dummy.event',
                id=uuid.uuid4(),
                guid=uuid.uuid4(),
                data={},
                actor='actor',
                request_id=uuid.uuid4(),
                created_at=datetime.utcnow()
            )
            self.body.reset()

        def delete(self):
            """Delete message."""
            pass

    return DummyMessage()


# Unit tests for Worker class
@mock.patch('briefy.choreographer.worker.queryUtility')
@mock.patch('briefy.choreographer.worker.notify')
def test_worker_process_message_with_missing_fields(notify_mock, query_mock, message):
    query_mock.side_effect = lambda interface, name, default: InternalEvent
    body = message.body.copy()
    message.body['guid'] = None
    w = Worker(TestQueue())
    answer = w.process_message(message)
    assert answer
    message.body = body
    message.body['event_name'] = None
    answer = w.process_message(message)
    assert answer


@mock.patch('briefy.choreographer.worker.queryUtility')
@mock.patch('briefy.choreographer.worker.notify')
def test_worker_process_message_when_event_factory_not_found(
        notify_mock,
        query_mock,
        message):
    query_mock.side_effect = lambda interface, name, default: InternalEvent
    logger_mock = mock.Mock()
    w = Worker(TestQueue(), logger_=logger_mock)
    assert w.process_message(message)
    # Now we create an InternalEvent instead of logging no handler was found
    assert not logger_mock.info.call_args


@mock.patch('briefy.choreographer.worker.queryUtility')
@mock.patch('briefy.choreographer.worker.notify')
def test_all_body_parameters_are_used(notify_mock, query_mock, message):
    query_mock.side_effect = lambda interface, name, default: InternalEvent
    logger_mock = mock.Mock()
    w = Worker(TestQueue(), logger_mock)
    w.process_message(message)
    notification = notify_mock.call_args[0][0]
    assert isinstance(notification, InternalEvent)
    assert all(message.body.read_count.values())

    assert notification.event_name == message.body['event_name']
    assert notification.id == message.body['id']
    assert notification.guid == message.body['guid']
    assert notification.created_at == message.body['created_at']
    assert not logger_mock.info.call_args
    assert logger_mock.debug.call_args


@mock.patch('briefy.choreographer.worker.Worker')
@mock.patch('briefy.choreographer.worker.queryUtility')
def test_worker_main(query_mock, worker_mock):

    def worker_call():
        raise RuntimeError

    def worker_init(input_queue, logger_, run_interval=.5):
        assert input_queue
        assert logger_
        return worker_call
    worker_mock.side_effect = worker_init
    with pytest.raises(RuntimeError):
        main()
