"""Leica entities."""
from briefy.choreographer.subscribers import BaseHandler


class LeicaHandler(BaseHandler):
    """Handler for Leica events."""


def handler(event):
    """Handle Leica events.

    :param event: Event
    :type event: briefy.choreographer.events.leica.ILeicaEvent
    """
    handler = LeicaHandler(event)
    handler()

