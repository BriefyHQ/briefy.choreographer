"""Mail action for Lead."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_NAME
from briefy.choreographer.events import laure
from zope.component import adapter
from zope.interface import implementer


class LaureMail(Mail):
    """Base class for emails sent on Lead events."""

    weight = 100
    """Weight of the action.

    A lower number takes precedence over a higher number.
    """

    entity = 'Assignment'
    """Name of the entity to be processed here."""

    @property
    def sender(self) -> dict:
        """Return sender information for this action.

        :returns: Dictionary with two keys - name, email
        """
        return {
            'name': MAIL_ACTION_LEICA_SENDER_NAME,
            'email': MAIL_ACTION_LEICA_SENDER_EMAIL,
        }


@adapter(laure.ILaureAssignmentRejected)
@implementer(IMail)
class LaureAssignmentRejectedCreative(LaureMail):
    """Email to be sent when automatic validation failed."""

    template_name = 'qa-automatic-reject'
    subject = '''Please re-submit your images for assignment {SLUG}: Technical check failed'''

    @property
    def action_url(self):
        """Action URL."""
        return self._action_url

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        recipients = []
        data = self.data
        assignment = data.get('assignment', {})
        fullname = assignment.get('professional_name', '')
        first_name = fullname.split(' ')[0]
        email = assignment.get('email', '')
        if fullname and email:
            recipients = [
                {
                    'first_name': first_name,
                    'fullname': fullname,
                    'email': email,
                }
            ]
        return recipients

    def transform(self) -> list:
        """Transform data."""
        base_payload = super().transform()
        data = self.data
        recipients = self.recipient
        assignment = data.get('assignment', {})
        validation = data.get('validation', {})
        feedback = validation.get('complete_feedback', '')
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
