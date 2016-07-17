"""Module that implements Briefy subscribers for Lead events."""
from briefy.choreographer.data.lead import LeadDTO
from briefy.choreographer.subscribers import BaseHandler


class Handler(BaseHandler):
    """Handler for Lead events."""

    _info_class_ = LeadDTO


def handler(event):
    """Handle Lead events.

    :param event: Event
    :type event: briefy.choreographer.events.lead.ILeadEvent
    """
    handler = Handler(event)
    handler()
