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
        payload['title'] = 'New Lead: {}'.format(data.subject)
        payload['text'] = """
        New lead create!

        Name: {}
        Email: {}
        Category: {}
        Sub category: {}
        """.format(data.fullname, data.email, data.category. data.sub_category)
        payload['username'] = 'New Lead bot'
        payload['data'] = {
            'FULLNAME': data.fullname,
            'EMAIL': data.email,
            'CATEGORY': data.category,
            'SUBCATEGORY': data.sub_category,
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
