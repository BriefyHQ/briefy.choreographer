"""Mail action for Assignments."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import LeicaMail
from briefy.choreographer.events.leica import assignment as events
from briefy.choreographer.utils.calendar import assignment_to_ical_attachment
from zope.component import adapter
from zope.interface import implementer

import typing as t


class AssignmentMail(LeicaMail):
    """Base class for emails sent on Assignment events."""

    entity = 'Assignment'
    """Name of the entity to be processed here."""

    @property
    def action_url(self) -> str:
        """Action URL."""
        return self._action_url

    def _extract_scheduled_datetime(self) -> str:
        """Extract scheduled_datetime in the correct timezone for this assignment.

        :return: A string representation of scheduled_datetime already in the correct timezone.
        """
        data = self.data
        scheduled_datetime = data.get('scheduled_datetime', '')
        timezone = data.get('timezone', '')
        if scheduled_datetime:
            scheduled_datetime = self._format_datetime(scheduled_datetime, timezone=timezone)
        return scheduled_datetime

    def payload_recipient(self, base_payload: dict, data: dict, recipient: dict) -> dict:
        """Return the payload for a recipient.

        :param base_payload: Sane default values for the payload.
        :param data: Serialization of the Assignment.
        :param recipient: Dictionary with recipient information.
        :return: Payload to be added to the queue.
        """
        scheduled_datetime = self._extract_scheduled_datetime()
        payload_item = {}
        payload_item.update(base_payload)
        payload_item['fullname'] = recipient.get('fullname')
        payload_item['email'] = recipient.get('email')
        payload_item['data'] = {
            'ID': data.get('id'),
            'ACTION_URL': self.action_url,
            'TITLE': data.get('title'),
            'EMAIL': recipient.get('email'),
            'FIRSTNAME': recipient.get('first_name', ),
            'FULLNAME': recipient.get('fullname'),
            'SLUG': data.get('slug'),
            'PROJECT': data.get('project', {}).get('title', ''),
            'FORMATTED_ADDRESS': data.get('location', {}).get('formatted_address', ''),
            'CONTACT_FULLNAME': data.get('location', {}).get('fullname', ''),
            'CONTACT_PHONE': data.get('location', {}).get('mobile', ''),
            'SCHEDULED_SHOOT_TIME': scheduled_datetime,
            'NUMBER_REQUIRED_ASSETS': data.get('number_required_assets'),
            'REQUIREMENTS': data.get('requirements')
        }
        subject = self.subject.format(**payload_item['data'])
        payload_item['subject'] = subject
        payload_item['data']['SUBJECT'] = subject
        return payload_item

    def transform(self) -> t.List[dict]:
        """Transform data."""
        base_payload = super().transform()[0]
        data = self.data
        payload = []
        recipients = self.recipients
        for recipient in recipients:
            payload_item = self.payload_recipient(base_payload, data, recipient)
            payload.append(payload_item)
        return payload


class AssignmentPMMail(AssignmentMail):
    """Base class for emails sent to the PM on Order events."""

    @property
    def recipients(self) -> t.List[dict]:
        """Return the data to be used as the recipient of this message."""
        return self._recipients('project_managers')


class AssignmentScoutMail(AssignmentMail):
    """Base class for emails sent to the Scouters on Order events."""

    @property
    def recipients(self) -> t.List[dict]:
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

    def get_ics_attachment(self) -> t.Optional[dict]:
        """Generate a dict with the ics attachment from this assignment."""
        data = self.data
        attachment = assignment_to_ical_attachment(data)
        return attachment

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        recipients = self.recipients
        return (True if recipients else False) and available

    @property
    def recipients(self) -> t.List[dict]:
        """Return the data to be used as the recipient of this message."""
        return self._recipients('professional_user')


class AssignmentCreativeMailWithICS(AssignmentCreativeMail):
    """Email to Creative containing an ICS attachment."""

    def payload_recipient(self, base_payload: dict, data: dict, recipient: dict) -> dict:
        """Return the payload for a recipient.

        :param base_payload: Sane default values for the payload.
        :param data: Serialization of the Assignment.
        :param recipient: Dictionary with recipient information.
        :return: Payload to be added to the queue.
        """
        payload = super().payload_recipient(base_payload, data, recipient)
        ics_attachment = self.get_ics_attachment()
        attachments = [ics_attachment, ] if ics_attachment else []
        payload['attachments'] = attachments
        return payload


@adapter(events.IAssignmentWfCancel)
@implementer(IMail)
class AssignmentCancelledCreativeMail(AssignmentCreativeMailWithICS):
    """Email to Creative on assignment is cancelled."""

    template_name = 'platform-order-cancellation-creative'
    subject = 'Important: Assignment {SLUG} cancelled'


@adapter(events.IAssignmentWfAssign)
@implementer(IMail)
class AssignmentAssignedCreativeMail(AssignmentCreativeMail):
    """Email to Creative on assignment is assigned."""

    template_name = 'platform-assignment-assigned'
    subject = 'Your Briefy Assignment {SLUG}'


@adapter(events.IAssignmentWfSelfAssign)
@implementer(IMail)
class AssignmentSelfCreativeMail(AssignmentCreativeMail):
    """Email to Creative when they self-assign."""

    template_name = 'platform-pool-assigned'
    subject = 'Your Briefy Assignment {SLUG}'


@adapter(events.IAssignmentWfApprove)
@implementer(IMail)
class AssignmentApproveCreativeMail(AssignmentCreativeMail):
    """Email to Creative when the set is approved."""

    template_name = 'platform-set-approved'
    subject = 'Good job! Your set has been approved!'


@adapter(events.IAssignmentWfReject)
@implementer(IMail)
class AssignmentWfRejectCreative(AssignmentCreativeMail):
    """Email to Creative when the set is rejected."""

    template_name = 'platform-set-rejected'
    subject = 'Important: Your set did not pass our Quality Assurance check'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        base_payload = super().transform()
        data = self.data
        history = data['state_history']
        last_transition = history[-1]
        payload = base_payload[0]
        payload['data']['FEEDBACK'] = last_transition['message']
        return base_payload


@adapter(events.IAssignmentWfSchedule)
@implementer(IMail)
class AssignmentScheduleCreativeMail(AssignmentCreativeMailWithICS):
    """Email to Creative when the assignment is scheduled."""

    template_name = 'platform-assignment-scheduled'
    subject = 'Hurray! Assignment {SLUG} is Now Scheduled!'


@adapter(events.IAssignmentWfReschedule)
@implementer(IMail)
class AssignmentRescheduleCreativeMail(AssignmentCreativeMailWithICS):
    """Email to Creative when the assignment is re-scheduled."""

    template_name = 'platform-assignment-rescheduled'
    subject = 'Your New Shooting Time for Assignment {SLUG}'


@adapter(events.IAssignmentWfPermReject)
@implementer(IMail)
class AssignmentWfPermRejectCreativeMail(AssignmentCreativeMail):
    """Email to creative when QA permanently reject an assignment."""

    template_name = 'platform-set-permanently-rejected'
    subject = 'Important: Your set {SLUG} was permanently rejected'


@adapter(events.IAssignmentWfPermReject)
@implementer(IMail)
class AssignmentWfPermRejectPMMail(AssignmentPMMail):
    """Email to PM when QA permanently reject an assignment."""

    template_name = 'platform-set-permanently-rejected'
    subject = 'Important: Your set {SLUG} was permanently rejected'
