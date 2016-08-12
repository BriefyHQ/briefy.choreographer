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
            'gateway': data.get('gateway'),
            'gateway_id': data.get('gateway_id'),
            'status': data.get('status'),
            'additional_info': data.get('additional_info'),
            'entity': data.get('entity'),
            'guid': data.get('guid'),
            'event_name': data.get('event_name'),
        }
        return payload
