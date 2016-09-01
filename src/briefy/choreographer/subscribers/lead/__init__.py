"""Module that implements Briefy subscribers for Lead events."""
from briefy.choreographer.subscribers import BaseHandler


class Handler(BaseHandler):
    """Handler for Lead events."""


def handler(event):
    """Handle Lead events.

    :param event: Event
    :type event: briefy.choreographer.events.lead.ILeadEvent
    """
    handler = Handler(event)
    handler()
