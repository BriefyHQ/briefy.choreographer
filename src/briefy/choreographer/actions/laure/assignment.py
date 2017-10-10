"""Leica Actions for Assignment."""
from briefy.choreographer.actions.laure import ILaureAction
from briefy.choreographer.actions.laure import LaureDeliveryAction
from briefy.choreographer.actions.laure import LaureValidationAction
from briefy.choreographer.events.leica import assignment as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.IAssignmentWfUpload)
@implementer(ILaureAction)
class AssignmentWfUpload(LaureValidationAction):
    """Send assignment uploaded to Ms. Laure validation queue."""

    entity = 'Assignment'
    weight = 100


@adapter(events.IAssignmentWfApprove)
@implementer(ILaureAction)
class AssignmentWfApprove(LaureDeliveryAction):
    """Send assignment approved to Ms. Laure delivery queue."""

    entity = 'Assignment'
    weight = 100


@adapter(events.IAssignmentWfStartPostProcess)
@implementer(ILaureAction)
class AssignmentWfStartPostProcess(LaureDeliveryAction):
    """Send assignment start post process to Ms. Laure delivery queue."""

    entity = 'Assignment'
    weight = 100


@adapter(events.IAssignmentWfReadyForUpload)
@implementer(ILaureAction)
class AssignmentWfReadyForUpload(LaureDeliveryAction):
    """Send assignment ready for upload event to Ms. Laure delivery queue."""

    entity = 'Assignment'
    weight = 100
