"""Briefy Choreographer Events."""
from briefy.common.event import IEvent


class IInternalEvent(IEvent):
    """An event used by briefy.choreographer."""


class InternalEvent:
    """An event used by briefy.choreographer."""

    event_name = ''
    actor = ''
    guid = ''
    created_at = ''
    request_id = ''
    data = None

    def __init__(self, actor, guid, request_id, created_at, data):
        """Initialize the event with a SQS Message."""
        self.actor = actor
        self.guid = guid
        self.request_id = request_id
        self.created_at = created_at
        self.data = data
