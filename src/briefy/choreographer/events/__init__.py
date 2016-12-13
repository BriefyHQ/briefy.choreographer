"""Briefy Choreographer Events."""
from briefy.common.event import IEvent
from datetime import datetime


class IInternalEvent(IEvent):
    """An event used by briefy.choreographer."""


class InternalEvent:
    """An event used by briefy.choreographer."""

    entity = ''
    """Entity triggering this event."""

    event_name = ''
    """Identifier of the event."""

    actor = ''
    """Actor triggering the event."""

    guid = ''
    """GUID of the event."""

    created_at = ''
    """Date when the event was created."""

    request_id = ''
    """ID of the request that triggered the event."""

    data = None
    """Event payload."""

    def __init__(self, actor: str, guid: str, request_id: str, created_at: datetime, data: dict):
        """Initialize the event with Message data."""
        self.actor = actor
        self.guid = guid
        self.request_id = request_id
        self.created_at = created_at
        self.data = data
