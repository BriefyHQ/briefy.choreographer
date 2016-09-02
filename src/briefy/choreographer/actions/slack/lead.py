"""Slack action for Lead."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer


class LeadSlack(Slack):
    """Slack message sent on Lead events."""

    entity = 'Lead'
    weight = 100
    _channel = '#briefy-co-leads'

    def transform(self):
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = 'New Lead created!'
        payload['text'] = 'New Lead was created, please take a look into the details:'
        payload['username'] = 'Briefy Bot'
        payload['data'] = {
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


@adapter(lead.ILeadCreated)
@implementer(ISlack)
class LeadCreated(LeadSlack):
    """After creating a new Lead, post on Slack."""

    @property
    def available(self):
        return True
