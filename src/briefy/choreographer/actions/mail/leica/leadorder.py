"""Mail action for LeadOrders."""
from .order import OrderPMMail
from .order import OrderScoutMail
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.events.leica.order import leadorder as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.ILeadOrderWfConfirm)
@implementer(IMail)
class LeadOrderWfConfirmScoutMail(OrderScoutMail):
    """Email scouters when the lead order is confirmed."""

    template_name = 'platform-lead-confirmed-scouting'
    subject = 'New lead {SLUG} confirmed by {CUSTOMER}'


@adapter(events.ILeadOrderWfConfirm)
@implementer(IMail)
class LeadOrderWfConfirmPMMail(OrderPMMail):
    """Email PM when the lead order is confirmed."""

    template_name = 'platform-lead-confirmed-pm'
    subject = 'New lead {SLUG} confirmed by {CUSTOMER}'
