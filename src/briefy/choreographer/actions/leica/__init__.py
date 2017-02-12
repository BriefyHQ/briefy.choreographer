"""Briefy Leica actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction


class ILeicaAction(IAction):
    """Action that deals with Briefy Leica."""

    pass


class LeicaAction(Action):
    """Action that deals with Ms. Laure."""

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
            'created_at': event.get('created_at'),
            'data': event.get('data'),
            'guid': event.get('guid'),
            'event_name': event.get('event_name'),
        }
        return payload
