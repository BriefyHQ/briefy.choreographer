"""Configuration for tests."""
from briefy.choreographer.actions import IAction
from briefy.choreographer.data import IDataTransferObject
from briefy.common.config import SQS_REGION
from briefy.common.queue import IQueue
from zope.component import getGlobalSiteManager
from zope.component import getUtility
from zope.configuration.xmlconfig import XMLConfig

import boto3
import botocore.endpoint
import json
import os


PATH = __file__.split(os.path.sep)[:-1] + ['data', ]


def get_url():
    """Return the url for the SQS server."""
    host = os.environ.get('SQS_IP', '127.0.0.1')
    port = os.environ.get('SQS_PORT', '8080')
    return 'http://{}:{}'.format(host, port)


def mock_sqs():
    """Mock SQS communication."""
    class MockEndpoint(botocore.endpoint.Endpoint):
        def __init__(self, host, *args, **kwargs):
            super().__init__(get_url(), *args, **kwargs)

    botocore.endpoint.Endpoint = MockEndpoint


def read_data_from_file(filename):
    """Read data from data file."""
    path = PATH[:]
    path.append(filename)
    data = open(os.path.sep.join(path), 'r').read()
    return json.loads(data)


class BaseTestCase:
    """Base test case."""

    def setup_class(cls):
        """Setup class."""
        from briefy import choreographer
        XMLConfig('configure.zcml', choreographer)()


class BaseActionCase(BaseTestCase):
    """Action testcase."""

    action_class = None
    action_interface = None
    event_class = None
    data_class = None
    data_file = ''

    def _make_data_object(self):
        """Return a data object instance."""
        klass = self.data_class
        data = read_data_from_file(self.data_file)
        return klass(**data)

    def _make_one(self, data, event):
        """Return an action instance."""
        klass = self.action_class
        return klass(data, event)

    def _prepare_queue(self):
        mock_sqs()
        queue = getUtility(IQueue, self.action_class._queue_name)
        queue_name = queue.name
        sqs = boto3.resource('sqs', region_name=SQS_REGION)
        sqs.create_queue(QueueName=queue_name)
        queue = sqs.get_queue_by_name(QueueName=queue_name)
        for message in queue.receive_messages(MaxNumberOfMessages=100):
            message.delete()

    def setup_method(self, method):
        """Setup testcase."""
        self.registry = getGlobalSiteManager()
        self.data = self._make_data_object()
        self._prepare_queue()
        event = None
        if self.event_class:
            self.event = self.event_class(
                actor='foo',
                request_id='e595e4ee-b4c2-4658-8298-f2af95b0120f',
                guid=self.data.id,
                created_at='2016-07-01T12:32:45',
                data=self.data
            )
            event = self.event
        self.obj = self._make_one(self.data, event)

    def test_interfaces(self):
        """Test that this action provides IAction interfaces."""
        obj = self.obj
        iface = self.action_interface
        assert IAction.providedBy(obj) is True
        assert iface.providedBy(obj) is True

    def test_registration(self):
        """Test that this action is registered."""
        if hasattr(self, 'event'):
            registry = self.registry
            data = self.data
            event = self.event
            adapters = [
                a for a in registry.getAdapters((data, event), IAction)
                if isinstance(a[1], self.action_class)
            ]
            assert len(adapters) == 1

    def test_call(self):
        """Test action execution."""
        obj = self.obj
        queue = obj.queue
        # No messages on the queue
        messages = queue.get_messages(num_messages=10)
        assert isinstance(messages, list)
        assert len(messages) == 0

        # Execute the action
        obj()

        messages = queue.get_messages(num_messages=10)
        assert isinstance(messages, list)
        assert len(messages) == 1


class BaseDataCase(BaseTestCase):
    """Data transfer object testcase."""

    data_class = None
    data_interface = None
    data_file = ''

    def _make_one(self):
        """Return a data object instance."""
        klass = self.data_class
        data = read_data_from_file(self.data_file)
        return klass(**data)

    def test_interfaces(self):
        """Test that this tool provides tool interfaces."""
        obj = self._make_one()
        iface = self.data_interface
        assert IDataTransferObject.providedBy(obj) is True
        assert iface.providedBy(obj) is True


class BaseQueueCase(BaseTestCase):
    """Base tests for queues."""

    queue = None

    def _make_one(self):
        """Return a queue instance."""
        klass = self.queue
        sqs = boto3.resource('sqs', region_name=klass.region_name)
        sqs.create_queue(QueueName=klass.name)
        queue = sqs.get_queue_by_name(QueueName=klass.name)
        for message in queue.receive_messages(MaxNumberOfMessages=100):
            message.delete()
        return klass()

    def setup_class(cls):
        """Setup test class."""
        mock_sqs()

    def get_payload(self):
        """Return a payload for this queue."""
        return {
            'foo': 'bar'
        }

    def test_init(self):
        """Test queue name."""
        queue = self._make_one()
        assert isinstance(queue, self.queue)

    def test_repr(self):
        """Test str representation of this tool."""
        queue = self._make_one()
        assert "<{0}(name='{1}'".format(queue.__class__.__name__, queue.name) in queue.__repr__()

    def test_write_message(self):
        """Test write_message."""
        queue = self._make_one()
        payload = self.get_payload()
        resp = queue.write_message(payload)
        assert isinstance(resp, str)

    def test_marshall_message(self):
        """Test _marshall_message."""
        queue = self._make_one()
        payload = self.get_payload()
        message = queue._message_klass(schema=queue.schema, body=payload)
        resp = queue._prepare_sqs_payload(message)
        assert isinstance(resp, dict)
        assert isinstance(resp['MessageBody'], str)

    def test_get_messages(self):
        """Test get_messages."""
        queue = self._make_one()
        payload = self.get_payload()
        resp = queue.write_message(payload)
        messages = queue.get_messages(num_messages=10)
        assert isinstance(messages, list)
        assert len(messages) == 1
        assert messages[0].message.message_id == resp
        assert messages[0].body == payload
