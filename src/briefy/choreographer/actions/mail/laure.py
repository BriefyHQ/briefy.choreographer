"""Mail action for Lead."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.events import laure
from zope.component import adapter
from zope.interface import implementer

import typing as t


class LaureMail(Mail):
    """Base class for emails sent on Lead events."""

    weight = 100
    """Weight of the action.

    A lower number takes precedence over a higher number.
    """

    entity = 'Assignment'
    """Name of the entity to be processed here."""


class LaureAssignmentRejected(LaureMail):
    """Email to be sent when automatic validation failed."""

    @property
    def action_url(self) -> str:
        """Action URL."""
        return self._action_url

    @property
    def recipients(self) -> t.Sequence[dict]:
        """Return the data to be used as the recipient of this message."""
        recipients = []
        data = self.data
        assignment = data.get('assignment', {})
        fullname = assignment.get('professional_name', '')
        first_name = fullname.split(' ')[0]
        email = assignment.get('email', '')
        if fullname and email:
            recipients = [{'first_name': first_name, 'fullname': fullname, 'email': email}]
        return recipients

    def transform(self) -> t.List[dict]:
        """Transform data."""
        base_payload = super().transform()[0]
        data = self.data
        recipients = self.recipients
        assignment = data.get('assignment', {})
        validation = data.get('validation', {})
        feedback = validation.get('complete_feedback', '')
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
                'ERRORS': feedback,
                'FULLNAME': recipient.get('fullname'),
                'FIRSTNAME': recipient.get('first_name', recipient.get('fullname')),
                'SLUG': assignment.get('code', ''),
                'ASSIGNMENT_ID': assignment.get('id', ''),
            }
            subject = self.subject.format(**payload_item['data'])
            payload_item['subject'] = subject
            payload_item['data']['SUBJECT'] = subject
            payload.append(payload_item)
        return payload


@adapter(laure.ILaureAssignmentRejected)
@implementer(IMail)
class LaureAssignmentRejectedTech(LaureAssignmentRejected):
    """Email to be sent when automatic validation failed due to failing requirements."""

    template_name = 'qa-automatic-reject-tech'
    subject = 'Please re-submit your images for assignment {SLUG}: Technical check failed'

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        validation = data.get('validation', {})
        total_images = validation.get('total_images', 0)
        number_of_photos = validation.get('number_of_photos', 0)
        return (total_images >= number_of_photos) and available


@adapter(laure.ILaureAssignmentRejected)
@implementer(IMail)
class LaureAssignmentRejectedLessImages(LaureAssignmentRejected):
    """Email to be sent when automatic validation failed due to less pictures than required."""

    template_name = 'qa-automatic-not-enough'
    subject = 'Please re-submit your images for assignment {SLUG}: Technical check failed'

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        validation = data.get('validation', {})
        total_images = validation.get('total_images', 0)
        number_of_photos = validation.get('number_of_photos', 0)
        return (total_images < number_of_photos) and available
