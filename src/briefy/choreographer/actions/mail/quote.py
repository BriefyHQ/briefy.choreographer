"""Mail action for Lead."""
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.config import MAIL_ACTION_QUOTE_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_QUOTE_SENDER_NAME
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer


class QuoteMail(Mail):
    """Mail sent on Lead events."""

    entity = 'Quote'
    weight = 100

    @property
    def sender(self):
        """Return sender information for this action.

        :returns: Dictionary with two keys - name, email
        :rtype: dict
        """
        return {
            'name': MAIL_ACTION_QUOTE_SENDER_NAME,
            'email': MAIL_ACTION_QUOTE_SENDER_EMAIL,
        }

    def transform(self):
        """Transform data."""
        payload = super().transform()
        data = self.data
        fullname = '{} {}'.format(data['first_name'], data['last_name'])
        payload['fullname'] = fullname
        payload['email'] = data['email']
        payload['company'] = data['company']
        payload['phone_number'] = data['phone_number']
        payload['company_site'] = data.get('company_site', '')

        payload['data'] = {
            'FULLNAME': fullname,
            'EMAIL': data['email'],
            'SUBJECT': self.subject,
        }
        return payload


@adapter(lead.IQuoteCreated)
@implementer(IMail)
class QuoteCreated(QuoteMail):
    """After creating a new Quote, send an email."""

    template_name = 'briefy-new-quote'
    subject = '''Your Quote has been Requested!'''

    @property
    def available(self):
        return True
