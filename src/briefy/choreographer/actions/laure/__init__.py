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
        data = self.data
        payload = {
            'id': event.guid,
            'created_at': data.get('created_at'),
            'data': data.get('data'),
            'guid': data.get('guid'),
            'event_name': data.get('event_name'),
        }
        return payload
