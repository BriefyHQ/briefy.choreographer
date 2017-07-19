"""Actions to dispatch e-mail notifications for leica.tasks events."""

from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica.assignment import AssignmentCreativeMail
from briefy.choreographer.events.leica import task as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.IAssignmentNotifyLateSubmissionSuccess)
@implementer(IMail)
class AssignmentNotifyLateSubmissionSuccess(AssignmentCreativeMail):
    """Email to Creative when late submission detected."""

    template_name = 'platform-assignment-reminder-late-submission'
    subject = 'Reminder: Late submission for Assignment {SLUG}'


@adapter(events.IAssignmentNotifyBeforeShootingSuccess)
@implementer(IMail)
class AssignmentNotifyBeforeShootingSuccess(AssignmentCreativeMail):
    """Email to Creative before shooting."""

    template_name = 'platform-assignment-reminder'
    subject = 'Reminder: Your Briefy shoot tomorrow for Assignment {SLUG}'
