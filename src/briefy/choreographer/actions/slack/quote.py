"""Slack action for Quote."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer

import typing as t


class QuoteSlack(Slack):
    """Base class used for Slack message sent on Quote events."""

    entity = 'Quote'
    weight = 100
    _channel = '#briefy-co-quotes'


@adapter(lead.IQuoteCreated)
@implementer(ISlack)
class QuoteCreated(QuoteSlack):
    """After creating a new Quote, post on slack."""

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload_item = payload[0]
        first_name = data['first_name']
        last_name = data['last_name']
        fullname = f'{first_name} {last_name}'
        payload_item['title'] = 'New Quote created!'
        payload_item['text'] = 'New Quote request was created, please take a look into the details:'
        payload_item['username'] = 'Briefy Bot'
        payload_item['data'] = {
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
