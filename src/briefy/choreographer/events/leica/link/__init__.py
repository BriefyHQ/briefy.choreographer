"""Briefy Link Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class ILinkEvent(IInternalEvent):
    """An event of a Link."""


class ILinkWfEvent(ILinkEvent):
    """A workflow event of a Link."""


class ILinkWfDelete(ILinkWfEvent):
    """Interface for link.workflow.delete."""


class LinkEvent(InternalEvent):
    """An event of a Link."""

    entity = 'Link'


class LinkWfEvent(LinkEvent):
    """A workflow event of a Link."""


@implementer(ILinkWfDelete)
class LinkWfDelete(LinkWfEvent):
    """Implement LinkWfDelete."""

    event_name = 'link.workflow.delete'
