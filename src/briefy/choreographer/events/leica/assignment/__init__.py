"""Briefy Assignment Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class IAssignmentEvent(IInternalEvent):
    """An event of a Assignment."""


class IAssignmentWfEvent(IAssignmentEvent):
    """A workflow event of a Assignment."""


class IAssignmentCreated(IAssignmentEvent):
    """Interface for assignment.created."""


class IAssignmentUpdated(IAssignmentEvent):
    """Interface for assignment.updated."""


class IAssignmentWfApprove(IAssignmentWfEvent):
    """Interface for assignment.workflow.approve."""


class IAssignmentWfAssign(IAssignmentWfEvent):
    """Interface for assignment.workflow.assign."""


class IAssignmentWfCancel(IAssignmentWfEvent):
    """Interface for assignment.workflow.cancel."""


class IAssignmentWfComplete(IAssignmentWfEvent):
    """Interface for assignment.workflow.complete."""


class IAssignmentWfInvalidateAssets(IAssignmentWfEvent):
    """Interface for assignment.workflow.invalidate_assets."""


class IAssignmentWfPermReject(IAssignmentWfEvent):
    """Interface for assignment.workflow.perm_reject."""


class IAssignmentWfPublish(IAssignmentWfEvent):
    """Interface for assignment.workflow.publish."""


class IAssignmentWfReadyForUpload(IAssignmentWfEvent):
    """Interface for assignment.workflow.ready_for_upload."""


class IAssignmentWfRefuse(IAssignmentWfEvent):
    """Interface for assignment.workflow.refuse."""


class IAssignmentWfReject(IAssignmentWfEvent):
    """Interface for assignment.workflow.reject."""


class IAssignmentWfRemoveSchedule(IAssignmentWfEvent):
    """Interface for assignment.workflow.remove_schedule."""


class IAssignmentWfReschedule(IAssignmentWfEvent):
    """Interface for assignment.workflow.reschedule."""


class IAssignmentWfRetract(IAssignmentWfEvent):
    """Interface for assignment.workflow.retract."""


class IAssignmentWfRetractApproval(IAssignmentWfEvent):
    """Interface for assignment.workflow.retract_approval."""


class IAssignmentWfRetractRejection(IAssignmentWfEvent):
    """Interface for assignment.workflow.retract_rejection."""


class IAssignmentWfReturnToQa(IAssignmentWfEvent):
    """Interface for assignment.workflow.return_to_qa."""


class IAssignmentWfSchedule(IAssignmentWfEvent):
    """Interface for assignment.workflow.schedule."""


class IAssignmentWfSchedulingIssues(IAssignmentWfEvent):
    """Interface for assignment.workflow.scheduling_issues."""


class IAssignmentWfSelfAssign(IAssignmentWfEvent):
    """Interface for assignment.workflow.self_assign."""


class IAssignmentWfSubmit(IAssignmentWfEvent):
    """Interface for assignment.workflow.submit."""


class IAssignmentWfUpload(IAssignmentWfEvent):
    """Interface for assignment.workflow.upload."""


class IAssignmentWfValidateAssets(IAssignmentWfEvent):
    """Interface for assignment.workflow.validate_assets."""


class IAssignmentWfEditPayout(IAssignmentWfEvent):
    """Interface for assignment.workflow.edit_payout."""


class IAssignmentWfEditCompensation(IAssignmentWfEvent):
    """Interface for assignment.workflow.edit_compensation."""


class IAssignmentWfAssignQAManager(IAssignmentWfEvent):
    """Interface for assignment.workflow.assign_qa_manager."""


class IAssignmentWfAssignPool(IAssignmentWfEvent):
    """Interface for assignment.workflow.assign_pool."""


class IAssignmentWfStartPostProcess(IAssignmentWfEvent):
    """Interface for assignment.workflow.start_post_process."""


class AssignmentEvent(InternalEvent):
    """An event of a Assignment."""

    entity = 'Assignment'


class AssignmentWfEvent(AssignmentEvent):
    """A workflow event of a Assignment."""


@implementer(IAssignmentCreated)
class AssignmentCreated(AssignmentEvent):
    """Implement AssignmentCreated."""

    event_name = 'assignment.created'


@implementer(IAssignmentUpdated)
class AssignmentUpdated(AssignmentEvent):
    """Implement AssignmentUpdated."""

    event_name = 'assignment.updated'


@implementer(IAssignmentWfApprove)
class AssignmentWfApprove(AssignmentWfEvent):
    """Implement AssignmentWfApprove."""

    event_name = 'assignment.workflow.approve'


@implementer(IAssignmentWfAssign)
class AssignmentWfAssign(AssignmentWfEvent):
    """Implement AssignmentWfAssign."""

    event_name = 'assignment.workflow.assign'


@implementer(IAssignmentWfCancel)
class AssignmentWfCancel(AssignmentWfEvent):
    """Implement AssignmentWfCancel."""

    event_name = 'assignment.workflow.cancel'


@implementer(IAssignmentWfComplete)
class AssignmentWfComplete(AssignmentWfEvent):
    """Implement AssignmentWfComplete."""

    event_name = 'assignment.workflow.complete'


@implementer(IAssignmentWfInvalidateAssets)
class AssignmentWfInvalidateAssets(AssignmentWfEvent):
    """Implement AssignmentWfInvalidateAssets."""

    event_name = 'assignment.workflow.invalidate_assets'


@implementer(IAssignmentWfPermReject)
class AssignmentWfPermReject(AssignmentWfEvent):
    """Implement AssignmentWfPermReject."""

    event_name = 'assignment.workflow.perm_reject'


@implementer(IAssignmentWfPublish)
class AssignmentWfPublish(AssignmentWfEvent):
    """Implement AssignmentWfPublish."""

    event_name = 'assignment.workflow.publish'


@implementer(IAssignmentWfReadyForUpload)
class AssignmentWfReadyForUpload(AssignmentWfEvent):
    """Implement AssignmentWfReadyForUpload."""

    event_name = 'assignment.workflow.ready_for_upload'


@implementer(IAssignmentWfRefuse)
class AssignmentWfRefuse(AssignmentWfEvent):
    """Implement AssignmentWfRefuse."""

    event_name = 'assignment.workflow.refuse'


@implementer(IAssignmentWfReject)
class AssignmentWfReject(AssignmentWfEvent):
    """Implement AssignmentWfReject."""

    event_name = 'assignment.workflow.reject'


@implementer(IAssignmentWfRemoveSchedule)
class AssignmentWfRemoveSchedule(AssignmentWfEvent):
    """Implement AssignmentWfRemoveSchedule."""

    event_name = 'assignment.workflow.remove_schedule'


@implementer(IAssignmentWfReschedule)
class AssignmentWfReschedule(AssignmentWfEvent):
    """Implement AssignmentWfReschedule."""

    event_name = 'assignment.workflow.reschedule'


@implementer(IAssignmentWfRetract)
class AssignmentWfRetract(AssignmentWfEvent):
    """Implement AssignmentWfRetract."""

    event_name = 'assignment.workflow.retract'


@implementer(IAssignmentWfRetractApproval)
class AssignmentWfRetractApproval(AssignmentWfEvent):
    """Implement AssignmentWfRetractApproval."""

    event_name = 'assignment.workflow.retract_approval'


@implementer(IAssignmentWfRetractRejection)
class AssignmentWfRetractRejection(AssignmentWfEvent):
    """Implement AssignmentWfRetractRejection."""

    event_name = 'assignment.workflow.retract_rejection'


@implementer(IAssignmentWfReturnToQa)
class AssignmentWfReturnToQa(AssignmentWfEvent):
    """Implement AssignmentWfReturnToQa."""

    event_name = 'assignment.workflow.return_to_qa'


@implementer(IAssignmentWfSchedule)
class AssignmentWfSchedule(AssignmentWfEvent):
    """Implement AssignmentWfSchedule."""

    event_name = 'assignment.workflow.schedule'


@implementer(IAssignmentWfSchedulingIssues)
class AssignmentWfSchedulingIssues(AssignmentWfEvent):
    """Implement AssignmentWfSchedulingIssues."""

    event_name = 'assignment.workflow.scheduling_issues'


@implementer(IAssignmentWfSelfAssign)
class AssignmentWfSelfAssign(AssignmentWfEvent):
    """Implement AssignmentWfSelfAssign."""

    event_name = 'assignment.workflow.self_assign'


@implementer(IAssignmentWfSubmit)
class AssignmentWfSubmit(AssignmentWfEvent):
    """Implement AssignmentWfSubmit."""

    event_name = 'assignment.workflow.submit'


@implementer(IAssignmentWfUpload)
class AssignmentWfUpload(AssignmentWfEvent):
    """Implement AssignmentWfUpload."""

    event_name = 'assignment.workflow.upload'


@implementer(IAssignmentWfValidateAssets)
class AssignmentWfValidateAssets(AssignmentWfEvent):
    """Implement AssignmentWfValidateAssets."""

    event_name = 'assignment.workflow.validate_assets'


@implementer(IAssignmentWfEditPayout)
class AssignmentWfEditPayout(AssignmentWfEvent):
    """Implement AssignmentWfEditPayout."""

    event_name = 'assignment.workflow.edit_payout'


@implementer(IAssignmentWfEditCompensation)
class AssignmentWfEditCompensation(AssignmentWfEvent):
    """Implement AssignmentWfEditCompensation."""

    event_name = 'assignment.workflow.edit_compensation'


@implementer(IAssignmentWfAssignQAManager)
class AssignmentWfAssignQAManager(AssignmentWfEvent):
    """Implement AssignmentWfAssignQAManager."""

    event_name = 'assignment.workflow.assign_qa_manager'


@implementer(IAssignmentWfAssignPool)
class AssignmentWfAssignPool(AssignmentWfEvent):
    """Implement AssignmentWfAssignPool."""

    event_name = 'assignment.workflow.assign_pool'


@implementer(IAssignmentWfStartPostProcess)
class AssignmentWfStartPostProcess(AssignmentWfEvent):
    """Implement AssignmentWfStartPostProcess."""

    event_name = 'assignment.workflow.start_post_process'
