"""Leica Actions for Assignment."""
from briefy.choreographer.actions.notification import Notification
from briefy.choreographer.actions.notification import INotification
from briefy.choreographer.events.leica import assignment as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.IAssignmentWfUpload)
@implementer(INotification)
class AssignmentWfUpload(Notification):
    """Send assignment uploaded to Ms. Laure."""

    entity = 'Assignment'
    weight = 100


@adapter(events.IAssignmentWfApprove)
@implementer(INotification)
class AssignmentWfApprove(Notification):
    """Send assignment approved to Ms. Laure."""

    entity = 'Assignment'
    weight = 100
