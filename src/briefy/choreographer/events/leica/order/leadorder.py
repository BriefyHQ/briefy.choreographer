"""Briefy Order Events."""
from briefy.choreographer.events.leica.order import order
from zope.interface import implementer


class ILeadOrderEvent(order.IOrderEvent):
    """An event of a Order."""


class ILeadOrderWfEvent(ILeadOrderEvent, order.IOrderWfEvent):
    """A workflow event of a Order."""


class ILeadOrderCreated(ILeadOrderEvent, order.IOrderCreated):
    """Interface for leadorder.created."""


class ILeadOrderUpdated(ILeadOrderEvent, order.IOrderUpdated):
    """Interface for leadorder.updated."""


class ILeadOrderWfConfirm(ILeadOrderWfEvent):
    """Interface for leadorder.workflow.confirm."""


class ILeadOrderWfRemoveConfirmation(ILeadOrderWfEvent):
    """Interface for leadorder.workflow.remove_confirmation."""


class ILeadOrderWfAccept(ILeadOrderWfEvent, order.IOrderWfAccept):
    """Interface for leadorder.workflow.accept."""


class ILeadOrderWfAssign(ILeadOrderWfEvent, order.IOrderWfAssign):
    """Interface for leadorder.workflow.assign."""


class ILeadOrderWfCancel(ILeadOrderWfEvent, order.IOrderWfCancel):
    """Interface for leadorder.workflow.cancel."""


class ILeadOrderWfDeliver(ILeadOrderWfEvent, order.IOrderWfDeliver):
    """Interface for leadorder.workflow.deliver."""


class ILeadOrderWfNewShoot(ILeadOrderWfEvent, order.IOrderWfNewShoot):
    """Interface for leadorder.workflow.new_shoot."""


class ILeadOrderWfPermRefuse(ILeadOrderWfEvent, order.IOrderWfPermRefuse):
    """Interface for leadorder.workflow.perm_refuse."""


class ILeadOrderWfReassign(ILeadOrderWfEvent, order.IOrderWfReassign):
    """Interface for leadorder.workflow.reassign."""


class ILeadOrderWfRefuse(ILeadOrderWfEvent, order.IOrderWfRefuse):
    """Interface for leadorder.workflow.refuse."""


class ILeadOrderWfRemoveAvailability(ILeadOrderWfEvent, order.IOrderWfRemoveAvailability):
    """Interface for leadorder.workflow.remove_availability."""


class ILeadOrderWfRemoveSchedule(ILeadOrderWfEvent, order.IOrderWfRemoveSchedule):
    """Interface for leadorder.workflow.remove_schedule."""


class ILeadOrderWfRequireRevision(ILeadOrderWfEvent, order.IOrderWfRequireRevision):
    """Interface for leadorder.workflow.require_revision."""


class ILeadOrderWfReshoot(ILeadOrderWfEvent, order.IOrderWfReshoot):
    """Interface for leadorder.workflow.reshoot."""


class ILeadOrderWfSchedule(ILeadOrderWfEvent, order.IOrderWfSchedule):
    """Interface for leadorder.workflow.schedule."""


class ILeadOrderWfStartQa(ILeadOrderWfEvent, order.IOrderWfStartQa):
    """Interface for leadorder.workflow.start_qa."""


class ILeadOrderWfSubmit(ILeadOrderWfEvent, order.IOrderWfSubmit):
    """Interface for leadorder.workflow.submit."""


class ILeadOrderWfUnassign(ILeadOrderWfEvent, order.IOrderWfUnassign):
    """Interface for leadorder.workflow.unassign."""


class ILeadOrderWfSetAvailability(ILeadOrderWfEvent, order.IOrderWfSetAvailability):
    """Interface for leadorder.workflow.set_availability."""


class ILeadOrderWfEditLocation(ILeadOrderWfEvent, order.IOrderWfEditLocation):
    """Interface for leadorder.workflow.edit_location."""


class ILeadOrderWfEditRequirements(ILeadOrderWfEvent, order.IOrderWfEditRequirements):
    """Interface for leadorder.workflow.edit_requirements."""


class LeadOrderEvent(order.OrderEvent):
    """An event of a Order."""

    entity = 'LeadOrder'


class LeadOrderWfEvent(LeadOrderEvent, order.OrderWfEvent):
    """A workflow event of a LeadOrder."""


@implementer(ILeadOrderCreated)
class LeadOrderCreated(LeadOrderEvent, order.OrderCreated):
    """Implement LeadOrderCreated."""

    event_name = 'leadorder.created'


@implementer(ILeadOrderUpdated)
class LeadOrderUpdated(LeadOrderEvent, order.OrderUpdated):
    """Implement LeadOrderUpdated."""

    event_name = 'leadorder.updated'


@implementer(ILeadOrderWfConfirm)
class LeadOrderWfConfirm(LeadOrderWfEvent):
    """Implement ILeadOrderWfConfirm."""

    event_name = 'leadorder.workflow.confirm'


@implementer(ILeadOrderWfRemoveConfirmation)
class LeadOrderWfRemoveConfirmation(LeadOrderWfEvent):
    """Implement ILeadOrderWfRemoveConfirmation."""

    event_name = 'leadorder.workflow.accept'


@implementer(ILeadOrderWfAccept)
class LeadOrderWfAccept(LeadOrderWfEvent, order.OrderWfAccept):
    """Implement LeadOrderWfAccept."""

    event_name = 'leadorder.workflow.accept'


@implementer(ILeadOrderWfAssign)
class LeadOrderWfAssign(LeadOrderWfEvent, order.OrderWfAssign):
    """Implement LeadOrderWfAssign."""

    event_name = 'leadorder.workflow.assign'


@implementer(ILeadOrderWfCancel)
class LeadOrderWfCancel(LeadOrderWfEvent, order.OrderWfCancel):
    """Implement LeadOrderWfCancel."""

    event_name = 'leadorder.workflow.cancel'


@implementer(ILeadOrderWfDeliver)
class LeadOrderWfDeliver(LeadOrderWfEvent, order.OrderWfDeliver):
    """Implement LeadOrderWfDeliver."""

    event_name = 'leadorder.workflow.deliver'


@implementer(ILeadOrderWfNewShoot)
class LeadOrderWfNewShoot(LeadOrderWfEvent, order.OrderWfNewShoot):
    """Implement LeadOrderWfNewShoot."""

    event_name = 'leadorder.workflow.new_shoot'


@implementer(ILeadOrderWfPermRefuse)
class LeadOrderWfPermRefuse(LeadOrderWfEvent, order.OrderWfPermRefuse):
    """Implement LeadOrderWfPermRefuse."""

    event_name = 'leadorder.workflow.perm_refuse'


@implementer(ILeadOrderWfReassign)
class LeadOrderWfReassign(LeadOrderWfEvent, order.OrderWfReassign):
    """Implement LeadOrderWfReassign."""

    event_name = 'leadorder.workflow.reassign'


@implementer(ILeadOrderWfRefuse)
class LeadOrderWfRefuse(LeadOrderWfEvent, order.OrderWfRefuse):
    """Implement LeadOrderWfRefuse."""

    event_name = 'leadorder.workflow.refuse'


@implementer(ILeadOrderWfRemoveAvailability)
class LeadOrderWfRemoveAvailability(LeadOrderWfEvent, order.OrderWfRemoveAvailability):
    """Implement LeadOrderWfRemoveAvailability."""

    event_name = 'leadorder.workflow.remove_availability'


@implementer(ILeadOrderWfRemoveSchedule)
class LeadOrderWfRemoveSchedule(LeadOrderWfEvent, order.OrderWfRemoveSchedule):
    """Implement LeadOrderWfRemoveSchedule."""

    event_name = 'leadorder.workflow.remove_schedule'


@implementer(ILeadOrderWfRequireRevision)
class LeadOrderWfRequireRevision(LeadOrderWfEvent, order.OrderWfRequireRevision):
    """Implement LeadOrderWfRequireRevision."""

    event_name = 'leadorder.workflow.require_revision'


@implementer(ILeadOrderWfReshoot)
class LeadOrderWfReshoot(LeadOrderWfEvent, order.OrderWfReshoot):
    """Implement LeadOrderWfReshoot."""

    event_name = 'leadorder.workflow.reshoot'


@implementer(ILeadOrderWfSchedule)
class LeadOrderWfSchedule(LeadOrderWfEvent, order.OrderWfSchedule):
    """Implement LeadOrderWfSchedule."""

    event_name = 'leadorder.workflow.schedule'


@implementer(ILeadOrderWfStartQa)
class LeadOrderWfStartQa(LeadOrderWfEvent, order.OrderWfStartQa):
    """Implement LeadOrderWfStartQa."""

    event_name = 'leadorder.workflow.start_qa'


@implementer(ILeadOrderWfSubmit)
class LeadOrderWfSubmit(LeadOrderWfEvent, order.OrderWfSubmit):
    """Implement LeadOrderWfSubmit."""

    event_name = 'leadorder.workflow.submit'


@implementer(ILeadOrderWfUnassign)
class LeadOrderWfUnassign(LeadOrderWfEvent, order.OrderWfUnassign):
    """Implement LeadOrderWfUnassign."""

    event_name = 'leadorder.workflow.unassign'


@implementer(ILeadOrderWfSetAvailability)
class LeadOrderWfSetAvailability(LeadOrderWfEvent, order.OrderWfSetAvailability):
    """Implement LeadOrderWfSetAvailability."""

    event_name = 'leadorder.workflow.set_availability'


@implementer(ILeadOrderWfEditLocation)
class LeadOrderWfEditLocation(LeadOrderWfEvent, order.OrderWfEditLocation):
    """Implement LeadOrderWfEditLocation."""

    event_name = 'leadorder.workflow.edit_location'


@implementer(ILeadOrderWfEditRequirements)
class LeadOrderWfEditRequirements(LeadOrderWfEvent, order.OrderWfEditRequirements):
    """Implement LeadOrderWfEditRequirements."""

    event_name = 'leadorder.workflow.edit_requirements'
