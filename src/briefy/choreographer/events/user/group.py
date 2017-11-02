"""Briefy Group Events."""
from briefy.choreographer.events.user import GroupEvent
from briefy.choreographer.events.user import IGroupCreated
from briefy.choreographer.events.user import IGroupUpdated
from zope.interface import implementer


@implementer(IGroupCreated)
class GroupCreated(GroupEvent):
    """A new Group was created."""

    event_name = 'group.created'


@implementer(IGroupUpdated)
class GroupUpdated(GroupEvent):
    """A new Group was updated."""

    event_name = 'group.updated'
