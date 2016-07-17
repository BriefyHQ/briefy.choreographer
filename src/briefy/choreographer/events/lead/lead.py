"""Briefy Lead Events."""
from briefy.choreographer.events.lead import ILeadCreated
from briefy.choreographer.events.lead import LeadEvent
from zope.interface import implementer


@implementer(ILeadCreated)
class LeadCreated(LeadEvent):
    """A new Lead was created."""

    event_name = 'lead.created'
