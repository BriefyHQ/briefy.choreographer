"""Leica Actions for Assignment."""
from briefy.choreographer.actions.laure import ILaureAction
from briefy.choreographer.actions.laure import LaureAction
from briefy.choreographer.events.leica import assignment as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.IAssignmentWfUpload)
@implementer(ILaureAction)
class AssignmentWfUpload(LaureAction):
    """Send assignment uploaded to Ms. Laure."""

    entity = 'Assignment'
    weight = 100


@adapter(events.IAssignmentWfApprove)
@implementer(ILaureAction)
class AssignmentWfApprove(LaureAction):
    """Send assignment approved to Ms. Laure."""

    entity = 'Assignment'
    weight = 100


@adapter(events.IAssignmentWfStartPostProcess)
@implementer(ILaureAction)
class AssignmentWfStartPostProcess(LaureAction):
    """Send assignment start post process to Ms. Laure."""

    _queue_name = 'delivery.queue'
    entity = 'Assignment'
    weight = 100
