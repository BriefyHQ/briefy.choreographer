"""Route actions to move Assignment events to ms.laure queues."""
from briefy.choreographer.actions.route import IRouteAction
from briefy.choreographer.actions.route import ReflexAction
from briefy.choreographer.events.leica.order import order as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.IOrderWfAccept)
@implementer(IRouteAction)
class OrderWfAccept(ReflexAction):
    """Route order payload to briefy.reflex."""

    entity = 'Order'
