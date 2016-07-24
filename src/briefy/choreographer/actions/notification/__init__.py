"""Notification actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction


class INotification(IAction):
    """Action that deals with a notification."""


class Notification(Action):
    """Action that deals with a notification."""

    weight = 100
    _queue_name = 'notification.queue'

    @property
    def available(self):
        """Check if this action is available."""
        return True

    def transform(self):
        """Transform data."""
        event = self.event
        data = self.data
        payload = {
            'id': event.guid,
            'type': self.entity,
            'fullname': '',
            'address': '',
            'subject': '',
            'gateway': data.gateway,
            'gateway_id': data.gateway_id,
            'status': data.status,
            'additional_info': data.additional_info,
            'entity': data.entity,
            'guid': data.guid,
            'event_name': data.event_name,
        }
        return payload
