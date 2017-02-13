"""Module that implements Briefy subscribers for User and Quote events."""
from briefy.choreographer.subscribers import BaseHandler


class UserHandler(BaseHandler):
    """Handler for User events."""


def handler(event):
    """Handle User events.

    :param event: Event
    :type event: briefy.choreographer.events.user.IUserEvent
    """
    handler = UserHandler(event)
    handler()
