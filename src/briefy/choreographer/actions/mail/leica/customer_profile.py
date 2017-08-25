"""Mail actions for CustomerUserProfiles."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import LeicaMail
from briefy.choreographer.config import PLATFORM_URL
from briefy.choreographer.events.leica.profiles import customer_profile as events
from zope.component import adapter
from zope.interface import implementer

import typing as t


class CustomerUserProfileMail(LeicaMail):
    """Base class for emails sent on CustomerProfile events."""

    entity = 'CustomerUserProfile'
    """Name of the entity to be processed here."""

    @property
    def action_url(self) -> str:
        """Action URL."""
        return self._action_url

    def transform(self) -> t.List[dict]:
        """Transform data."""
        base_payload = super().transform()[0]
        data = self.data
        recipients = self.recipients
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


@adapter(events.ICustomerUserProfileWfActivate)
@implementer(IMail)
class CustomerUserProfileWfActivate(CustomerUserProfileMail):
    """After activating a new CustomerUserProfile, send a welcome email."""

    template_name = 'platform-customer-onboarding'
    subject = 'Your Login Details to Briefy\'s Platform'

    @property
    def action_url(self) -> str:
        """Action URL."""
        return f'{PLATFORM_URL}login'

    @property
    def recipients(self) -> t.List[dict]:
        """Return the data to be used as the recipient of this message."""
        data = self.data
        return [
            {'first_name': data['first_name'], 'fullname': data['fullname'], 'email': data['email']}
        ]

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        data = self.data
        payload_item['data']['PASSWORD'] = data['initial_password']
        return payload
