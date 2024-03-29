"""Briefy Lead Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class ILeadEvent(IInternalEvent):
    """An event of a Lead."""


class ILeadCreated(ILeadEvent):
    """A new Lead was created."""


class LeadEvent(InternalEvent):
    """An event of a Lead."""

    entity = 'Lead'


class IQuoteEvent(IInternalEvent):
    """An event of a Quote."""


class IQuoteCreated(IQuoteEvent):
    """A new Quote was created."""


class QuoteEvent(InternalEvent):
    """An event of a Quote."""

    entity = 'Quote'


class IPackageOrderEvent(IInternalEvent):
    """An event of a PackageOrder."""


class IPackageOrderCreated(ILeadEvent):
    """A new PackageOrder was created."""


class PackageOrderEvent(InternalEvent):
    """An event of a PackageOrder."""

    entity = 'PackageOrder'


@implementer(ILeadCreated)
class LeadCreated(LeadEvent):
    """A new Lead was created."""

    event_name = 'lead.created'


@implementer(IQuoteCreated)
class QuoteCreated(QuoteEvent):
    """A new Quote was created."""

    event_name = 'quote.created'


@implementer(IPackageOrderCreated)
class PackageOrderCreated(PackageOrderEvent):
    """A new PackageOrder was created."""

    event_name = 'package_order.created'
