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
    title = 'Order!'
    text = 'An Order'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = self.title
        payload['text'] = self.text
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
                {'title': 'ID',
                 'value': data.get('slug'),
                 'short': True,
                 },
            ]
        }
        return payload


@adapter(events.IOrderCreated)
@implementer(ISlack)
class OrderSubmit(OrderSlack):
    """After creating a new Order, post on Slack."""

    title = 'New order!'
    text = 'New Order was created, please take a look into the details:'


@adapter(events.IOrderWfCancel)
@implementer(ISlack)
class OrderWfCancel(OrderSlack):
    """After cancelling an Order, post on Slack."""

    title = 'Order Cancelled!'
    text = 'An Order was cancelled'


@adapter(events.IOrderWfRefuse)
@implementer(ISlack)
class OrderWfRefuse(OrderSlack):
    """After refusing an Order, post on Slack."""

    title = 'Set was refused!'
    text = 'A set was refused by a customer.'


@adapter(events.IOrderWfDeliver)
@implementer(ISlack)
class OrderWfDeliver(OrderSlack):
    """After delivering an Order, post on Slack."""

    title = 'Set was delivered!'
    text = 'A set was delivered by a customer.'


@adapter(events.IOrderWfAssign)
@implementer(ISlack)
class OrderWfAssign(OrderSlack):
    """After assigning an Order, post on Slack."""

    title = 'Order was assigned!'
    text = 'An order was assigned.'


@adapter(events.IOrderWfSchedule)
@implementer(ISlack)
class OrderWfSchedule(OrderSlack):
    """After scheduling an Order, post on Slack."""

    title = 'Order was scheduled!'
    text = 'An order was scheduled.'


@adapter(events.IOrderWfRemoveAvailability)
@implementer(ISlack)
class OrderWfRemoveAvailability(OrderSlack):
    """Slack after removing availability of an Order."""

    title = 'Order had availabilities removed'
    text = 'Order has no availabilities'