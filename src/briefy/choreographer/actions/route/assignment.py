"""Route actions to move Assignment events to ms.laure queues."""
from briefy.choreographer.actions.route import IRouteAction
from briefy.choreographer.actions.route import LaureDeliveryAction
from briefy.choreographer.actions.route import LaureValidationAction
from briefy.choreographer.events.leica import assignment as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.IAssignmentWfUpload)
@implementer(IRouteAction)
class AssignmentWfUpload(LaureValidationAction):
    """Send assignment uploaded to Ms. Laure validation queue."""

    entity = 'Assignment'


@adapter(events.IAssignmentWfApprove)
@implementer(IRouteAction)
class AssignmentWfApprove(LaureDeliveryAction):
    """Send assignment approved to Ms. Laure delivery queue."""

    entity = 'Assignment'


@adapter(events.IAssignmentWfStartPostProcess)
@implementer(IRouteAction)
class AssignmentWfStartPostProcess(LaureDeliveryAction):
    """Send assignment start post process to Ms. Laure delivery queue."""

    entity = 'Assignment'


@adapter(events.IAssignmentWfReadyForUpload)
@implementer(IRouteAction)
class AssignmentWfReadyForUpload(LaureDeliveryAction):
    """Send assignment ready for upload event to Ms. Laure delivery queue."""

    entity = 'Assignment'
