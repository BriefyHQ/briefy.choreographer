"""Mail action for Lead."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.config import MAIL_ACTION_QUOTE_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_QUOTE_SENDER_NAME
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer

import typing as t


class QuoteMail(Mail):
    """Base class for emails sent on Quote events."""

    weight = 100
    entity = 'Quote'

    @property
    def sender(self) -> dict:
        """Return sender information for this action.

        :returns: Dictionary with two keys - name, email
        """
        return {'name': MAIL_ACTION_QUOTE_SENDER_NAME, 'email': MAIL_ACTION_QUOTE_SENDER_EMAIL}

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        fist_name = data['first_name']
        last_name = data['last_name']
        fullname = f'{fist_name} {last_name}'
        payload[0]['fullname'] = fullname
        payload[0]['email'] = data['email']
        payload[0]['company'] = data['company']
        payload[0]['phone_number'] = data['phone_number']
        payload[0]['company_site'] = data.get('company_site', '')

        payload[0]['data'] = {
            'FULLNAME': fullname, 'EMAIL': data['email'], 'SUBJECT': self.subject
        }
        return payload


@adapter(lead.IQuoteCreated)
@implementer(IMail)
class QuoteCreated(QuoteMail):
    """After creating a new Quote, send an email."""

    @property
    def subject(self):
        """Return the subject line based on the category of this quote."""
        subject = 'Your Quote has been Requested!'
        data = self.data
        category = data.get('category', 'general')
        if category == 'hotels':
            subject = 'Thank you for the interest.'
        return subject

    @property
    def template_name(self):
        """Return the template name based on the category of this quote."""
        template_name = 'briefy-new-quote'
        data = self.data
        category = data.get('category', 'general')
        if category == 'hotels':
            template_name = 'briefy-hotels-new-quote'
        return template_name
