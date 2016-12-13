"""Module that implements Briefy subscribers for Lead and Quote events."""
from briefy.choreographer.subscribers import BaseHandler


class LeadHandler(BaseHandler):
    """Handler for Lead events."""


def lead_handler(event):
    """Handle Lead events.

    :param event: Event
    :type event: briefy.choreographer.events.lead.ILeadEvent
    """
    handler = LeadHandler(event)
    handler()


class QuoteHandler(BaseHandler):
    """Handler for Quote events."""


def quote_handler(event):
    """Handle Quote events.

    :param event: Event
    :type event: briefy.choreographer.events.lead.IQuoteEvent
    """
    handler = QuoteHandler(event)
    handler()
