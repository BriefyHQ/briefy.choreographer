"""Mail action for Lead."""
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.config import MAIL_ACTION_QUOTE_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_QUOTE_SENDER_NAME
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer


class QuoteMail(Mail):
    """Base class for emails sent on Quote events."""

    weight = 100
    entity = 'Quote'

    @property
    def sender(self) -> dict:
        """Return sender information for this action.

        :returns: Dictionary with two keys - name, email
        """
        return {
            'name': MAIL_ACTION_QUOTE_SENDER_NAME,
            'email': MAIL_ACTION_QUOTE_SENDER_EMAIL,
        }

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        fullname = '{first} {last}'.format(
            first=data['first_name'],
            last=data['last_name']
        )
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
