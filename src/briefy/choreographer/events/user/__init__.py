"""Briefy User Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent


class IUserEvent(IInternalEvent):
    """An event of a User."""


class IUserLogin(IUserEvent):
    """User has just logged in."""


class IUserFirstLogin(IUserEvent):
    """User has just logged in for the first time."""


class IUserCreated(IUserEvent):
    """A new User was created."""


class IUserUpdated(IUserEvent):
    """An user was updated."""


class IUserPasswordChanged(IUserEvent):
    """User changed its password."""


class IUserPasswordReset(IUserEvent):
    """A reset password request for a user."""


class IGroupEvent(IInternalEvent):
    """An event of a Group."""


class IGroupCreated(IGroupEvent):
    """A new Group was created."""


class IGroupUpdated(IGroupEvent):
    """A Group was updated."""


class UserEvent(InternalEvent):
    """An event of a User."""

    entity = 'User'


class GroupEvent(InternalEvent):
    """An event of a Group."""

    entity = 'Group'
