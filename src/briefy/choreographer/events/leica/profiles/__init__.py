"""Briefy Profile Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent


class IUserProfileEvent(IInternalEvent):
    """An event of a UserProfile."""


class UserProfileEvent(InternalEvent):
    """An event of a UserProfile."""

    entity = 'UserProfile'
