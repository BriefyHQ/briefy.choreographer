"""Briefy Leica actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction
from uuid import uuid4


class ILeicaAction(IAction):
    """Action that deals with Briefy Leica."""

    pass


class LeicaAction(Action):
    """Action that deals with Ms. Laure."""

    category = 'service_message'

    weight = 100
    _queue_name = 'leica.queue'

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        return True and available

    def transform(self) -> dict:
        """Transform data."""
        event = self.event
        payload = {
            'id': str(uuid4()),
            'created_at': event.created_at,
            'data': event.data,
            'guid': event.guid,
            'event_name': event.event_name,
        }
        return payload
