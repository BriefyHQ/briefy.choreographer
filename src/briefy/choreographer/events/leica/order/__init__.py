"""Briefy Order Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class IOrderEvent(IInternalEvent):
    """An event of a Order."""


class IOrderWfEvent(IOrderEvent):
    """A workflow event of a Order."""


class IOrderCreated(IOrderEvent):
    """Interface for order.created."""


class IOrderUpdated(IOrderEvent):
    """Interface for order.updated."""


class IOrderWfAccept(IOrderWfEvent):
    """Interface for order.workflow.accept."""


class IOrderWfAssign(IOrderWfEvent):
    """Interface for order.workflow.assign."""


class IOrderWfCancel(IOrderWfEvent):
    """Interface for order.workflow.cancel."""


class IOrderWfDeliver(IOrderWfEvent):
    """Interface for order.workflow.deliver."""


class IOrderWfNewShoot(IOrderWfEvent):
    """Interface for order.workflow.new_shoot."""


class IOrderWfPermRefuse(IOrderWfEvent):
    """Interface for order.workflow.perm_refuse."""


class IOrderWfReassign(IOrderWfEvent):
    """Interface for order.workflow.reassign."""


class IOrderWfRefuse(IOrderWfEvent):
    """Interface for order.workflow.refuse."""


class IOrderWfRemoveAvailability(IOrderWfEvent):
    """Interface for order.workflow.remove_availability."""


class IOrderWfRemoveSchedule(IOrderWfEvent):
    """Interface for order.workflow.remove_schedule."""


class IOrderWfRequireRevision(IOrderWfEvent):
    """Interface for order.workflow.require_revision."""


class IOrderWfReshoot(IOrderWfEvent):
    """Interface for order.workflow.reshoot."""


class IOrderWfSchedule(IOrderWfEvent):
    """Interface for order.workflow.schedule."""


class IOrderWfStartQa(IOrderWfEvent):
    """Interface for order.workflow.start_qa."""


class IOrderWfSubmit(IOrderWfEvent):
    """Interface for order.workflow.submit."""


class IOrderWfUnassign(IOrderWfEvent):
    """Interface for order.workflow.unassign."""


class IOrderWfSetAvailability(IOrderWfEvent):
    """Interface for order.workflow.set_availability."""


class IOrderWfEditLocation(IOrderWfEvent):
    """Interface for order.workflow.edit_location."""


class OrderEvent(InternalEvent):
    """An event of a Order."""

    entity = 'Order'


class OrderWfEvent(OrderEvent):
    """A workflow event of a Order."""


@implementer(IOrderCreated)
class OrderCreated(OrderEvent):
    """Implement OrderCreated."""

    event_name = 'order.created'


@implementer(IOrderUpdated)
class OrderUpdated(OrderEvent):
    """Implement OrderUpdated."""

    event_name = 'order.updated'


@implementer(IOrderWfAccept)
class OrderWfAccept(OrderWfEvent):
    """Implement OrderWfAccept."""

    event_name = 'order.workflow.accept'


@implementer(IOrderWfAssign)
class OrderWfAssign(OrderWfEvent):
    """Implement OrderWfAssign."""

    event_name = 'order.workflow.assign'


@implementer(IOrderWfCancel)
class OrderWfCancel(OrderWfEvent):
    """Implement OrderWfCancel."""

    event_name = 'order.workflow.cancel'


@implementer(IOrderWfDeliver)
class OrderWfDeliver(OrderWfEvent):
    """Implement OrderWfDeliver."""

    event_name = 'order.workflow.deliver'


@implementer(IOrderWfNewShoot)
class OrderWfNewShoot(OrderWfEvent):
    """Implement OrderWfNewShoot."""

    event_name = 'order.workflow.new_shoot'


@implementer(IOrderWfPermRefuse)
class OrderWfPermRefuse(OrderWfEvent):
    """Implement OrderWfPermRefuse."""

    event_name = 'order.workflow.perm_refuse'


@implementer(IOrderWfReassign)
class OrderWfReassign(OrderWfEvent):
    """Implement OrderWfReassign."""

    event_name = 'order.workflow.reassign'


@implementer(IOrderWfRefuse)
class OrderWfRefuse(OrderWfEvent):
    """Implement OrderWfRefuse."""

    event_name = 'order.workflow.refuse'


@implementer(IOrderWfRemoveAvailability)
class OrderWfRemoveAvailability(OrderWfEvent):
    """Implement OrderWfRemoveAvailability."""

    event_name = 'order.workflow.remove_availability'


@implementer(IOrderWfRemoveSchedule)
class OrderWfRemoveSchedule(OrderWfEvent):
    """Implement OrderWfRemoveSchedule."""

    event_name = 'order.workflow.remove_schedule'


@implementer(IOrderWfRequireRevision)
class OrderWfRequireRevision(OrderWfEvent):
    """Implement OrderWfRequireRevision."""

    event_name = 'order.workflow.require_revision'


@implementer(IOrderWfReshoot)
class OrderWfReshoot(OrderWfEvent):
    """Implement OrderWfReshoot."""

    event_name = 'order.workflow.reshoot'


@implementer(IOrderWfSchedule)
class OrderWfSchedule(OrderWfEvent):
    """Implement OrderWfSchedule."""

    event_name = 'order.workflow.schedule'


@implementer(IOrderWfStartQa)
class OrderWfStartQa(OrderWfEvent):
    """Implement OrderWfStartQa."""

    event_name = 'order.workflow.start_qa'


@implementer(IOrderWfSubmit)
class OrderWfSubmit(OrderWfEvent):
    """Implement OrderWfSubmit."""

    event_name = 'order.workflow.submit'


@implementer(IOrderWfUnassign)
class OrderWfUnassign(OrderWfEvent):
    """Implement OrderWfUnassign."""

    event_name = 'order.workflow.unassign'


@implementer(IOrderWfSetAvailability)
class OrderWfSetAvailability(OrderWfEvent):
    """Implement OrderWfSetAvailability."""

    event_name = 'order.workflow.set_availability'


@implementer(IOrderWfEditLocation)
class OrderWfEditLocation(OrderWfEvent):
    """Implement OrderWfEditLocation."""

    event_name = 'order.workflow.edit_location'
