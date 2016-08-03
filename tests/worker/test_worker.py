"""Tests for `briefy.choreographer.worker` module."""

from briefy.choreographer.worker import Worker
from briefy.choreographer.worker import main
from collections import defaultdict
from datetime import datetime
from unittest import mock

import pytest
import uuid


class AssertRead(dict):
    """
    A dictionary that counts the number of times each value was fetched
    """
    def __init__(self, *args, **kw):
        self.read_count = defaultdict(lambda: 0)
        super().__init__(*args, **kw)

    def __getitem__(self, key):
        res = super().__getitem__(key)
        self.read_count[key] += 1
        return res

    def reset(self):
        for key in self:
            self.read_count[key] = 0

class TestQueue:
    def __init__(self):
        self.messages = []

    def get_messages(self):
        return self.messages

    def write_message(self, message):
        self.message.append(message)


@pytest.fixture
def message():
    class DummyMessage:
        def __init__(self):
            self.body = AssertRead(
                event_name='dummy.event',
                guid=uuid.uuid4(),
                data = {},
                actor='actor',
                request_id=uuid.uuid4(),
                created_at=datetime.utcnow()
            )
            self.body.reset()
        def delete(self): pass

    return DummyMessage()


# Unit tests for Worker class

@mock.patch("briefy.choreographer.worker.queryUtility")
@mock.patch("briefy.choreographer.worker.notify")
def test_worker_doesnot_process_message_with_missing_fields(notify_mock, query_mock, message):
    query_mock.side_effect = lambda interface, name, context: dict
    body = message.body.copy()
    message.body['guid'] = None
    w  = Worker(TestQueue())
    answer = w.process_message(message)
    assert not answer
    message.body = body
    message.body['event_name'] = None
    answer = w.process_message(message)
    assert not answer


@mock.patch("briefy.choreographer.worker.queryUtility")
@mock.patch("briefy.choreographer.worker.notify")
def test_worker_doesnot_process_message_when_event_factory_not_found(notify_mock, query_mock, message):
    query_mock.side_effect = lambda interface, name, context: None
    logger_mock = mock.Mock()
    w  = Worker(TestQueue(), logger_=logger_mock)
    assert not w.process_message(message)
    assert 'has no handler' in logger_mock.info.call_args[0][0]


@mock.patch("briefy.choreographer.worker.queryUtility")
@mock.patch("briefy.choreographer.worker.notify")
def test_all_body_parameters_are_used(notify_mock, query_mock, message):
    query_mock.side_effect = lambda interface, name, context: dict
    logger_mock = mock.Mock()
    w  = Worker(TestQueue(), logger_mock)
    answer = w.process_message(message)
    notification = notify_mock.call_args[0][0]
    assert isinstance(notification, dict)
    assert all(message.body.read_count.values())
    message.body.pop('event_name')
    assert notification == message.body
    assert not logger_mock.info.call_args
    assert logger_mock.debug.call_args


@mock.patch("briefy.choreographer.worker.Worker")
@mock.patch("briefy.choreographer.worker.queryUtility")
def test_worker_main(query_mock, worker_mock):
    def side(input_queue, logger_, run_interval=.5):
        assert input_queue
        assert logger_
        raise RuntimeError
    worker_mock.side_effect = side
    with pytest.raises(RuntimeError):
        main()

