"""Ms Laure actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction


class ILaureAction(IAction):
    """Action that deals with Ms. Laure."""


class LaureAction(Action):
    """Action that deals with Ms. Laure."""

    weight = 100
    _queue_name = 'laure.queue'

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        return True and available

    def transform(self) -> dict:
        """Transform data."""
        event = self.event
        payload = {
            'created_at': event.created_at,
            'data': event.data,
            'guid': event.guid,
            'event_name': event.event_name,
        }
        return payload
