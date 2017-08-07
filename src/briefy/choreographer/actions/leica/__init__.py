"""Briefy Leica actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction
from uuid import uuid4

import typing as t


class ILeicaAction(IAction):
    """Action that deals with Briefy Leica."""


class LeicaAction(Action):
    """Action that deals with Ms. Laure."""

    weight = 100
    _queue_name = 'leica.queue'

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
            }
        ]
        return payload
