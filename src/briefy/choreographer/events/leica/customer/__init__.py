"""Briefy Customer Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class ICustomerEvent(IInternalEvent):
    """An event of a Customer."""


class ICustomerWfEvent(ICustomerEvent):
    """A workflow event of a Customer."""


class ICustomerCreated(ICustomerEvent):
    """Interface for customer.created."""


class ICustomerUpdated(ICustomerEvent):
    """Interface for customer.updated."""


class ICustomerWfActivate(ICustomerWfEvent):
    """Interface for customer.workflow.activate."""


class ICustomerWfInactivate(ICustomerWfEvent):
    """Interface for customer.workflow.inactivate."""


class ICustomerWfSubmit(ICustomerWfEvent):
    """Interface for customer.workflow.submit."""


class CustomerEvent(InternalEvent):
    """An event of a Customer."""

    entity = 'Customer'


class CustomerWfEvent(CustomerEvent):
    """A workflow event of a Customer."""


@implementer(ICustomerCreated)
class CustomerCreated(CustomerEvent):
    """Implement CustomerCreated."""

    event_name = 'customer.created'


@implementer(ICustomerUpdated)
class CustomerUpdated(CustomerEvent):
    """Implement CustomerUpdated."""

    event_name = 'customer.updated'


@implementer(ICustomerWfActivate)
class CustomerWfActivate(CustomerWfEvent):
    """Implement CustomerWfActivate."""

    event_name = 'customer.workflow.activate'


@implementer(ICustomerWfInactivate)
class CustomerWfInactivate(CustomerWfEvent):
    """Implement CustomerWfInactivate."""

    event_name = 'customer.workflow.inactivate'


@implementer(ICustomerWfSubmit)
class CustomerWfSubmit(CustomerWfEvent):
    """Implement CustomerWfSubmit."""

    event_name = 'customer.workflow.submit'
