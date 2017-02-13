"""Module that implements Briefy subscribers for Laure and Quote events."""
from briefy.choreographer.subscribers import BaseHandler


class LaureHandler(BaseHandler):
    """Handler for Laure events."""


def laure_handler(event):
    """Handle Laure events.

    :param event: Event
    :type event: briefy.choreographer.events.laure.ILaureEvent
    """
    handler = LaureHandler(event)
    handler()
