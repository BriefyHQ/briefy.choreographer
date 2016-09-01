"""Briefy Lead Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent


class ILeadEvent(IInternalEvent):
    """An event of a Lead."""


class ILeadCreated(ILeadEvent):
    """A new Lead was created."""


class LeadEvent(InternalEvent):
    """An event used by briefy.choreographer."""
    entity = 'Lead'


class IQuoteEvent(IInternalEvent):
    """An event of a Quote."""


class IQuoteCreated(IQuoteEvent):
    """A new Quote was created."""


class QuoteEvent(InternalEvent):
    """An event used by briefy.choreographer."""
    entity = 'Quote'
