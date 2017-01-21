"""Slack actions for Orders."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events.leica import order as events
from zope.component import adapter
from zope.interface import implementer


class OrderSlack(Slack):
    """Base class for Slack message sent on Lead events."""

    entity = 'Lead'
    weight = 100
    _channel = '#tests'


@adapter(events.IOrderCreated)
@implementer(ISlack)
class OrderCreated(OrderSlack):
    """After creating a new Order, post on Slack."""

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = 'New Order created!'
        payload['text'] = 'New Order was created, please take a look into the details:'
        payload['username'] = 'Briefy Bot'
        payload['data'] = {
            'fields': [
                {'title': 'Customer',
                 'value': data.get('customer', {}).get('title'),
                 'short': True,
                 },
                {'title': 'Project',
                 'value': data.get('project', {}).get('title'),
                 'short': True,
                 },
                {'title': 'Title',
                 'value': data.get('title'),
                 'short': True,
                 },
            ]
        }
        return payload
