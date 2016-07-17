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

    def __init__(self, message):
        """Initialize the event with a SQS Message."""
        self.actor = message.actor
        self.guid = message.guid
        self.request_id = message.request_id
        self.created_at = message.created_at
        self.data = message.data
