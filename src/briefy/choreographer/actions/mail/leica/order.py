"""Mail action for Orders."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import LeicaMail
from briefy.choreographer.events.leica import order as events
from zope.component import adapter
from zope.interface import implementer


class OrderMail(LeicaMail):
    """Base class for emails sent on Order events."""""

    entity = 'Order'
    """Name of the entity to be processed here."""

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        assignment = data.get('assignment', {})
        scheduled_datetime = assignment.get('scheduled_datetime', '')
        if scheduled_datetime:
            scheduled_datetime = self._format_datetime(scheduled_datetime)
        recipient = self.recipient
        payload['fullname'] = recipient.get('fullname')
        payload['email'] = recipient.get('email')
        payload['data'] = {
            'ID': data.get('id'),
            'ACTION_URL': data.get('id'),
            'TITLE': data.get('title'),
            'EMAIL': recipient.get('email'),
            'FULLNAME': recipient.get('fullname'),
            'CUSTOMER': data.get('customer', {}).get('title'),
            'PROJECT': data.get('project', {}).get('title'),
            'FORMATTED_ADDRESS': data.get('location', {}).get('formatted_address'),
            'SCHEDULED_SHOOT_TIME': scheduled_datetime,
            'SUBJECT': self.subject,
        }
        return payload


class OrderCustomerMail(OrderMail):
    """Base class for emails sent to Customer on Order events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        data = self.data
        return {
            'fullname': data['customer_user']['fullname'],
            'email': data['customer_user']['email'],
        }


class OrderPMMail(OrderMail):
    """Base class for emails sent to the PM on Order events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        data = self.data
        return {
            'fullname': data['project_manager']['fullname'],
            'email': data['project_manager']['email'],
        }


class OrderScoutMail(OrderMail):
    """Base class for emails sent to the Scouters on Order events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return {
            'fullname': 'Briefy Scouters',
            'email': 'scouting@briefy.co',
        }


@adapter(events.IOrderCreated)
@implementer(IMail)
class OrderCreatedScoutMail(OrderScoutMail):
    """Email to scouters on order created."""

    template_name = 'platform-order-created-scouting'
    subject = '''New order created by *|CUSTOMER|*'''
