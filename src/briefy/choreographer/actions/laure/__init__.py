"""Ms Laure actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction
from uuid import uuid4


class ILaureAction(IAction):
    """Action that deals with Ms. Laure."""


class LaureValidationAction(Action):
    """Action that deals with Ms. Laure validation process."""

    category = 'service_message'

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
            'id': str(uuid4()),
            'created_at': event.created_at,
            'data': event.data,
            'guid': event.guid,
            'event_name': event.event_name,
        }
        return payload


class LaureDeliveryAction(LaureValidationAction):
    """Action that deals with Ms. Laure delivery process."""

    weight = 100
    _queue_name = 'delivery.queue'
