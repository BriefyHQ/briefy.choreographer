"""Briefy User Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent


class IUserEvent(IInternalEvent):
    """An event of a User."""


class IUserCreated(IUserEvent):
    """A new User was created."""


class IUserPasswordReset(IUserEvent):
    """A reset password request for a user."""


class UserEvent(InternalEvent):
    """An event of a User."""

    entity = 'User'
