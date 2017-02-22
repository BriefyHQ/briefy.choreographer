"""Mail action for Professional."""
from briefy.choreographer.config import PLATFORM_URL
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import LeicaMail
from briefy.choreographer.events.leica import professional as events
from zope.component import adapter
from zope.interface import implementer


class ProfessionalMail(LeicaMail):
    """Base class for emails sent on Professional events."""""

    entity = 'Professional'
    """Name of the entity to be processed here."""

    @property
    def action_url(self):
        """Action URL."""
        return self._action_url

    def _recipients(self, field_name: str):
        """Return a list of valid recipients."""
        data = self.data['entity']
        recipients = []
        if field_name == 'last_transition':
            history = data['state_history']
            actor = history[0]['actor']
            users = [actor, ]
        else:
            users = data[field_name]
        for user in users:
            if not user['internal']:
                continue
            recipients.append(
                {
                    'first_name': user['first_name'],
                    'fullname': user['fullname'],
                    'email': user['email'],
                }
            )
        return recipients

    def transform(self) -> list:
        """Transform data."""
        base_payload = super().transform()
        data = self.data
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
                'EMAIL': recipient.get('email'),
                'FULLNAME': recipient.get('fullname'),
                'FIRSTNAME': recipient.get('first_name'),
                'SUBJECT': self.subject,
            }
            subject = self.subject.format(**payload_item['data'])
            payload_item['subject'] = subject
            payload_item['data']['SUBJECT'] = subject
            payload.append(payload_item)
        return payload


class ProfessionalCreativeMail(ProfessionalMail):
    """Base class for emails sent to the Creative on Professional events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        data = self.data
        return [
            {
                'first_name': data['first_name'],
                'fullname': data['fullname'],
                'email': data['email'],
            }
        ]


# Email sent on account creation
@adapter(events.IProfessionalWfApprove)
@implementer(IMail)
class ProfessionalWfApproveCreative(ProfessionalCreativeMail):
    """Email to creative when their account is approved."""

    template_name = 'platform-creative-onboarding'
    subject = '''Your Login Details to Briefy's Platform'''

    @property
    def action_url(self):
        """Action URL."""
        return '{base}login'.format(base=PLATFORM_URL)

    def transform(self) -> list:
        """Transform data."""
        base_payload = super().transform()
        data = self.data
        payload = base_payload[0]
        payload['data']['PASSWORD'] = data['initial_password']
        return base_payload
