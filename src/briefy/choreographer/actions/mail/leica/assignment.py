"""Mail action for Assignments."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import LeicaMail
from briefy.choreographer.events.leica import assignment as events
from zope.component import adapter
from zope.interface import implementer


class AssignmentMail(LeicaMail):
    """Base class for emails sent on Assignment events."""""

    entity = 'Assignment'
    """Name of the entity to be processed here."""

    @property
    def action_url(self):
        """Action URL."""
        return self._action_url

    def transform(self) -> list:
        """Transform data."""
        base_payload = super().transform()
        data = self.data
        scheduled_datetime = data.get('scheduled_datetime', '')
        if scheduled_datetime:
            scheduled_datetime = self._format_datetime(scheduled_datetime)
        recipients = self.recipient
        if isinstance(recipients, dict):
            recipients = [recipients, ]
        elif not recipients:
            return []
        payload = []
        for recipient in recipients:
            payload_item = {}
            payload_item.update(base_payload)
            payload_item['fullname'] = recipient.get('fullname')
            payload_item['email'] = recipient.get('email')
            payload_item['data'] = {
                'ID': data.get('id'),
                'ACTION_URL': self.action_url,
                'TITLE': data.get('title'),
                'EMAIL': recipient.get('email'),
                'FIRSTNAME': recipient.get('fullname'),
                'FULLNAME': recipient.get('fullname'),
                'SLUG': data.get('slug'),
                'PROJECT': data.get('project', {}).get('title'),
                'FORMATTED_ADDRESS': data.get('location', {}).get('formatted_address'),
                'CONTACT_FULLNAME': data.get('location', {}).get('fullname'),
                'CONTACT_PHONE': data.get('location', {}).get('mobile'),
                'SCHEDULED_SHOOT_TIME': scheduled_datetime,
                'SUBJECT': self.subject,
            }
            subject = self.subject.format(**payload_item['data'])
            payload_item['subject'] = subject
            payload_item['data']['SUBJECT'] = subject
            payload.append(payload_item)
        return payload


class AssignmentPMMail(AssignmentMail):
    """Base class for emails sent to the PM on Order events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return self._recipients('project_managers')


class AssignmentScoutMail(AssignmentMail):
    """Base class for emails sent to the Scouters on Order events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return [
            {
                'first_name': 'Scouters',
                'fullname': 'Briefy Scouters',
                'email': 'scouting@briefy.co',
            }
        ]


class AssignmentCreativeMail(AssignmentMail):
    """Base class for emails sent to the Creative on Order events."""

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        recipient = self.recipient
        return (True if recipient else False)and available

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return self._recipients('professional_user')


@adapter(events.IAssignmentWfCancel)
@implementer(IMail)
class AssignmentCancelledCreativeMail(AssignmentCreativeMail):
    """Email to Creative on assignment is cancelled."""

    template_name = 'platform-order-cancellation-creative'
    subject = '''Important: Assignment {SLUG} cancelled'''


@adapter(events.IAssignmentWfAssign)
@implementer(IMail)
class AssignmentAssignedCreativeMail(AssignmentCreativeMail):
    """Email to Creative on assignment is assigned."""

    template_name = 'platform-assignment-assigned'
    subject = '''Your Briefy Assignment {SLUG}'''


@adapter(events.IAssignmentWfSelfAssign)
@implementer(IMail)
class AssignmentSelfCreativeMail(AssignmentCreativeMail):
    """Email to Creative when they self-assign."""

    template_name = 'platform-pool-assigned'
    subject = '''Your Briefy Assignment {SLUG}'''


@adapter(events.IAssignmentWfApprove)
@implementer(IMail)
class AssignmentApproveCreativeMail(AssignmentCreativeMail):
    """Email to Creative when the set is approved."""

    template_name = 'platform-set-approved'
    subject = '''Good job! Your set has been approved!'''


@adapter(events.IAssignmentWfSchedule)
@implementer(IMail)
class AssignmentScheduleCreativeMail(AssignmentCreativeMail):
    """Email to Creative when the assignment is scheduled."""

    template_name = 'platform-assignment-scheduled'
    subject = '''Hurray! Assignment {SLUG} is Now Scheduled!'''


@adapter(events.IAssignmentWfReschedule)
@implementer(IMail)
class AssignmentRescheduleCreativeMail(AssignmentCreativeMail):
    """Email to Creative when the assignment is re-scheduled."""

    template_name = 'platform-assignment-rescheduled'
    subject = '''Your New Shooting Time for Assignment {SLUG}"'''
