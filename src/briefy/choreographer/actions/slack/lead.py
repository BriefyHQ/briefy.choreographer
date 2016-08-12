"""Slack action for Lead."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.data.lead import ILeadDTO
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer


class LeadSlack(Slack):
    """Mail sent on Lead events."""

    entity = 'Lead'
    weight = 100

    def transform(self):
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = 'New Lead created!'
        payload['text'] = 'New Lead was created, please take look into the details:'
        payload['username'] = 'Briefy Bot'
        payload['data'] = {
            'fields': [
                {'title': 'Fullname',
                 'value': data.fullname,
                 'short': True,
                 },
                {'title': 'Email',
                 'value': data.email,
                 'short': True,
                 },
                {'title': 'Category',
                 'value': data.category,
                 'short': True,
                 },
                {'title': 'Subcategory',
                 'value': data.sub_category,
                 'short': True,
                 },
            ]
        }
        return payload


@adapter(ILeadDTO, lead.ILeadCreated)
@implementer(ISlack)
class LeadCreated(LeadSlack):
    """After creating a new Lead, send an email."""

    @property
    def available(self):
        """Should not fire slack message if we are dealing with an instant booking."""
        available = super().available
        data = self.data
        return available and data.internal
