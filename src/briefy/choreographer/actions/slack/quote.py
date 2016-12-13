"""Slack action for Quote."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer


class QuoteSlack(Slack):
    """Base class used for Slack message sent on Quote events."""

    entity = 'Quote'
    weight = 100
    _channel = '#briefy-co-quotes'


@adapter(lead.IQuoteCreated)
@implementer(ISlack)
class QuoteCreated(QuoteSlack):
    """After creating a new Quote, post on slack."""

    def transform(self):
        """Transform data."""
        payload = super().transform()
        data = self.data
        fullname = '{} {}'.format(data['first_name'], data['last_name'])
        payload['title'] = 'New Quote created!'
        payload['text'] = 'New Quote request was created, please take a look into the details:'
        payload['username'] = 'Briefy Bot'
        payload['data'] = {
            'fields': [
                {'title': 'Fullname',
                 'value': fullname,
                 'short': True,
                 },
                {'title': 'Email',
                 'value': data['email'],
                 'short': True,
                 },
                {'title': 'Phone Number',
                 'value': data['phone_number'],
                 'short': True,
                 },
                {'title': 'Company',
                 'value': data['company'],
                 'short': True,
                 },
                {'title': 'Company Site',
                 'value': data.get('company_site', ''),
                 'short': True,
                 },
            ]
        }
        return payload