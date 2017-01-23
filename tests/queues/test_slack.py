"""Tests for `briefy.choreographer.queues` module."""
from briefy.choreographer.queues.slack import Queue
from conftest import BaseQueueCase


class TestChoreographerQueue(BaseQueueCase):
    """Tests for Choreographer Slack Queue."""

    queue = Queue
    utility_name = 'slack.queue'

    def get_payload(self):
        """Payload for the slack queue."""
        return {
            'event_name': 'customer.event.created',
            'entity': 'customer',
            'guid': 'eebd5265-7201-4316-b996-722b977dbf32',
            'channel': '',
            'title': 'New Lead',
            'text': 'Test',
            'color': 'good',
            'icon': ':briefy:',
            'username': 'New Lead bot',
            'data': {
                'fields': '[]',
            },
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
