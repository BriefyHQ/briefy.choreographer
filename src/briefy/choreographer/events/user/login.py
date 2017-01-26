"""Briefy Login Events."""
from briefy.choreographer.events.user import IUserLogin
from briefy.choreographer.events.user import IUserFirstLogin
from briefy.choreographer.events.user import UserEvent
from zope.interface import implementer


@implementer(IUserLogin)
class UserLogin(UserEvent):
    """Login of a user."""

    event_name = 'user.login'


@implementer(IUserFirstLogin)
class UserFirstLogin(UserEvent):
    """First login of a user."""

    event_name = 'user.login.first'
