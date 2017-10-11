"""Route actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction
from uuid import uuid4

import typing as t


class IRouteAction(IAction):
    """Action that route message to another queue."""


class RouteAction(Action):
    """Action that route message event to another queue."""

    category = 'service_message'

    weight = 100

    _queue_name = None
    """Should be defined by subclass."""

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        return True and available

    def transform(self) -> t.List[dict]:
        """Transform data."""
        event = self.event
        payload = [
            {
                'id': str(uuid4()),
                'created_at': event.created_at,
                'data': event.data,
                'guid': event.guid,
                'event_name': event.event_name,
            },
        ]
        return payload


class LaureDeliveryAction(RouteAction):
    """Action that deals with Ms. Laure delivery process."""

    _queue_name = 'delivery.queue'


class LaureValidationAction(RouteAction):
    """Action that deals with Ms. Laure validation process."""

    _queue_name = 'laure.queue'


class ReflexAction(RouteAction):
    """Action that deals with Ms. Laure validation process."""

    _queue_name = 'reflex.queue'
