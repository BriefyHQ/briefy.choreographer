"""Slack action for Lead."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer

import typing as t


class LeadSlack(Slack):
    """Base class for Slack message sent on Lead events."""

    entity = 'Lead'
    weight = 100
    _channel = '#briefy-co-leads'


@adapter(lead.ILeadCreated)
@implementer(ISlack)
class LeadCreated(LeadSlack):
    """After creating a new Lead, post on Slack."""

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload_item = payload[0]
        payload_item['title'] = 'New Lead created!'
        payload_item['text'] = 'New Lead was created, please take a look into the details:'
        payload_item['username'] = 'Briefy Bot'
        payload_item['data'] = {
            'fields': [
                {'title': 'Fullname',
                 'value': data.get('fullname'),
                 'short': True,
                 },
                {'title': 'Email',
                 'value': data.get('email'),
                 'short': True,
                 },
                {'title': 'Category',
                 'value': data.get('category'),
                 'short': True,
                 },
                {'title': 'Subcategory',
                 'value': data.get('sub_category'),
                 'short': True,
                 },
            ]
        }
        return payload
