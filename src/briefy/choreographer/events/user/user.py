"""Briefy User Events."""
from briefy.choreographer.events.user import IUserCreated
from briefy.choreographer.events.user import IUserPasswordChanged
from briefy.choreographer.events.user import IUserPasswordReset
from briefy.choreographer.events.user import UserEvent
from zope.interface import implementer


@implementer(IUserCreated)
class UserCreated(UserEvent):
    """A new User was created."""

    event_name = 'user.created'


@implementer(IUserPasswordChanged)
class UserPasswordChanged(UserEvent):
    """A user changed the password."""

    event_name = 'user.password.changed'


@implementer(IUserPasswordReset)
class UserPasswordReset(UserEvent):
    """A reset password request for a user."""

    event_name = 'user.password.reset'
