"""Briefy Lead Events."""
from briefy.choreographer.events.lead import ILeadCreated
from briefy.choreographer.events.lead import IQuoteCreated
from briefy.choreographer.events.lead import LeadEvent
from briefy.choreographer.events.lead import QuoteEvent
from zope.interface import implementer


@implementer(ILeadCreated)
class LeadCreated(LeadEvent):
    """A new Lead was created."""
    event_name = 'lead.created'


@implementer(IQuoteCreated)
class QuoteCreated(QuoteEvent):
    """A new Quote was created."""
    event_name = 'quote.created'
