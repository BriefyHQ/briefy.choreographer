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

    @property
    def is_resubmission(self) -> bool:
        """Check if this is a re-submission.

        :return: Boolean indicating if this is a re-submission.
        """
        data = self.data
        return True if data.get('submission_path', '') else False

    @property
    def template_name(self) -> str:
        """Return the appropriate template name."""
        template_name = 'platform-assignment-reminder-late-submission'
        resubmission = self.is_resubmission
        if resubmission:
            template_name = 'platform-assignment-reminder-late-resubmission'
        return template_name

    @property
    def subject(self) -> str:
        """Return the appropriate subject."""
        subject = 'Reminder: Late submission for Assignment {SLUG}'
        resubmission = self.is_resubmission
        if resubmission:
            subject = 'Reminder: Late re-submission for Assignment {SLUG}'
        return subject


@adapter(events.IAssignmentNotifyBeforeShootingSuccess)
@implementer(IMail)
class AssignmentNotifyBeforeShootingSuccess(AssignmentCreativeMail):
    """Email to Creative before shooting."""

    template_name = 'platform-assignment-reminder'
    subject = 'Reminder: Your Briefy shoot tomorrow for Assignment {SLUG}'
