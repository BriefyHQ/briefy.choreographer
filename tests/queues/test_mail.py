"""Tests for `briefy.choreographer.queue` module."""
from briefy.choreographer.queues.mail import Queue
from conftest import BaseQueueCase


class TestChoreographerQueue(BaseQueueCase):
    """Tests for ChoreographerQueue."""

    queue = Queue
    utility_name = 'mail.queue'

    def get_payload(self):
        """Payload for the mail queue."""
        return {
            'event_name': 'customer.event.created',
            'entity': 'customer',
            'guid': 'eebd5265-7201-4316-b996-722b977dbf32',
            'fullname': 'New Customer',
            'email': 'customer@fake.domain',
            'template': 'welcome-en-gb',
            'subject': 'Foo bar',
            'data': {
                'foo': 'bar',
                'bar': 'foo'
            },
            'attachments': None
        }

    def test_interfaces(self):
        """Test that this queue provides IQueue interfaces."""
        from briefy.common.queue import IQueue
        queue = self.queue()
        assert IQueue.providedBy(queue)

    def test_utility_lookup(self):
        """Test that this queue provides IQueue interfaces."""
        from briefy import choreographer
        from briefy.common.queue import IQueue
        from zope.component import getUtility
        from zope.configuration.xmlconfig import XMLConfig

        XMLConfig('configure.zcml', choreographer)()
        queue = getUtility(IQueue, self.utility_name)
        assert isinstance(queue, self.queue)
