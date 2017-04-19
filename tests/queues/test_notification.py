"""Tests for `briefy.choreographer.queues.notification` module."""
from briefy.choreographer.queues.notification import SQSQueue
from conftest import BaseQueueCase


class TestChoreographerQueue(BaseQueueCase):
    """Tests for ChoreographerQueue."""

    queue = SQSQueue
    utility_name = 'notification.queue'

    def get_payload(self):
        """Payload for the notification queue."""
        return {
            'additional_info': '-',
            'address': 'foo@bar.com',
            'entity': 'Customer',
            'event_name': 'customer.event.created',
            'fullname': 'Foo Bar',
            'gateway': 'mandrill',
            'gateway_id': '7af0375da4024523816e0637a9051208',
            'guid': 'eebd5265-7201-4316-b996-722b977dbf32',
            'id': 'bc3e06f4-0a87-4184-bbf4-a4caa4200f38',
            'status': 'sent',
            'subject': 'Briefy is coming soon!',
            'type': 'Mail',
        }

    def test_interfaces(self):
        """Test that this queue provides IQueue interfaces."""
        from briefy.common.queue import IQueue
        queue = self.queue()
        assert IQueue.providedBy(queue)

    def test_utility_lookup(self):
        """Test that this queue provides IQueue interfaces."""
        from briefy.common.queue import IQueue
        from zope.component import getUtility
        queue = getUtility(IQueue, self.utility_name)
        assert isinstance(queue, self.queue)
