"""Mail action for Orders."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import LeicaMail
from briefy.choreographer.config import PLATFORM_URL
from briefy.choreographer.events.leica.order import order as events
from briefy.choreographer.utils.user_data import users_data_by_role
from zope.component import adapter
from zope.interface import implementer


class OrderMail(LeicaMail):
    """Base class for emails sent on Order events."""

    entity = 'Order'
    """Name of the entity to be processed here."""

    @property
    def action_url(self):
        """Action URL."""
        return self._action_url

    def transform(self) -> list:
        """Transform data."""
        base_payload = super().transform()
        data = self.data
        assignment = data.get('assignment', {})
        assignment_id = ''
        if assignment:
            assignment_id = assignment.get('slug', '')
        timezone = assignment.get('timezone', '')
        scheduled_datetime = assignment.get(
            'scheduled_datetime',
            data.get('scheduled_datetime', '')
        )
        if scheduled_datetime:
            scheduled_datetime = self._format_datetime(scheduled_datetime, timezone=timezone)
        recipients = self.recipient
        if isinstance(recipients, dict):
            recipients = [recipients, ]
        elif not recipients:
            return []
        payload = []
        for recipient in recipients:
            payload_item = {}
            payload_item.update(base_payload)
            payload_item['fullname'] = recipient.get('fullname')
            payload_item['email'] = recipient.get('email')
            payload_item['data'] = {
                'ID': data.get('id'),
                'ACTION_URL': self.action_url,
                'TITLE': data.get('title'),
                'EMAIL': recipient.get('email'),
                'FULLNAME': recipient.get('fullname'),
                'FIRSTNAME': recipient.get('first_name', recipient.get('fullname')),
                'SLUG': data.get('slug'),
                'ASSIGNMENT_ID': assignment_id,
                'CUSTOMER': data.get('customer', {}).get('title'),
                'CUSTOMER_ORDER_ID': data.get('customer_order_id', ''),
                'PROJECT': data.get('project', {}).get('title'),
                'FORMATTED_ADDRESS': data.get('location', {}).get('formatted_address'),
                'SCHEDULED_SHOOT_TIME': scheduled_datetime,
                'SUBJECT': self.subject,
            }
            subject = self.subject.format(**payload_item['data'])
            payload_item['subject'] = subject
            payload_item['data']['SUBJECT'] = subject
            payload.append(payload_item)
        return payload


class OrderCustomerMail(OrderMail):
    """Base class for emails sent to Customer on Order events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return self._recipients('customer_users')


class OrderPMMail(OrderMail):
    """Base class for emails sent to the PM on Order events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return self._recipients('project_managers')


class OrderScoutMail(OrderMail):
    """Base class for emails sent to the Scouters on Order events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return [
            {
                'first_name': 'Scouters',
                'fullname': 'Briefy Scouters',
                'email': 'scouting@briefy.co',
            }
        ]


class OrderCreativeMail(OrderMail):
    """Base class for emails sent to the Creative on Order events."""

    @property
    def professional(self):
        """Professional assigned to this Order."""
        professional = users_data_by_role(self.event, 'professional_user')
        return professional[0] if professional else None

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        professional = self.professional
        return True if (professional and available) else False

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        professional = self.professional
        return [
            {
                'first_name': professional['first_name'],
                'fullname': professional['fullname'],
                'email': professional['email'],
            }
        ]


# Order Created by Customer
@adapter(events.IOrderWfSubmit)
@implementer(IMail)
class OrderSubmitScoutMail(OrderScoutMail):
    """Email to scouters on order created."""

    template_name = 'platform-order-created-scouting'
    subject = 'New order created by {CUSTOMER}'

    @property
    def action_url(self):
        """Action URL."""
        return '{base}dashboard'.format(base=PLATFORM_URL)

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        source = data['source']
        return (source == 'customer') and available


@adapter(events.IOrderWfSubmit)
@implementer(IMail)
class OrderSubmitCustomerMail(OrderCustomerMail):
    """Email to customer on order created."""

    template_name = 'platform-order-created'
    subject = 'We received your Briefy order {SLUG}'

    @property
    def action_url(self):
        """Action URL."""
        return '{base}dashboard'.format(base=PLATFORM_URL)

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return self._recipients('last_transition')

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        source = data['source']
        return (source == 'customer') and available


# Customer Cancels an Order
@adapter(events.IOrderWfCancel)
@implementer(IMail)
class OrderCancelledCustomerMail(OrderCustomerMail):
    """Email to customer on order cancelled."""

    template_name = 'platform-order-cancellation'
    subject = 'Your order is now cancelled'

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return self._recipients('last_transition')


@adapter(events.IOrderWfCancel)
@implementer(IMail)
class OrderCancelledPMMail(OrderPMMail):
    """Email to PM on order cancelled."""

    template_name = 'platform-order-cancellation-pm'
    subject = 'Order {SLUG} was cancelled by {CUSTOMER}'


# Customer Refuses a Set
@adapter(events.IOrderWfRefuse)
@implementer(IMail)
class OrderSetRefusedCustomerMail(OrderCustomerMail):
    """Email to customer on order refusal."""

    template_name = 'platform-set-refused'
    subject = 'Your set has been sent for further revision'

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        return self._recipients('last_transition')


@adapter(events.IOrderWfRefuse)
@implementer(IMail)
class OrderSetRefusedPMMail(OrderPMMail):
    """Email to Project Managers on order refusal."""

    template_name = 'platform-set-refused-pm'
    subject = '{CUSTOMER} has requested further revision on order {SLUG}'


# Set delivered by QA
@adapter(events.IOrderWfDeliver)
@implementer(IMail)
class OrderSetDeliveredCustomerMail(OrderCustomerMail):
    """Email to customer on order delivered."""

    template_name = 'platform-order-set-delivered'
    subject = 'A new Briefy set is ready for you!'


# Order has been assigned
@adapter(events.IOrderWfAssign)
@implementer(IMail)
class OrderAssignedCustomerMail(OrderCustomerMail):
    """Email to customer on order assigned."""

    template_name = 'platform-order-assigned'
    subject = 'A Briefy content creator has been assigned to your order {SLUG}'


# Order has been scheduled
@adapter(events.IOrderWfSchedule)
@implementer(IMail)
class OrderScheduledCustomerMail(OrderCustomerMail):
    """Email to customer on order scheduled."""

    template_name = 'platform-order-scheduled'
    subject = 'A shooting for order {SLUG} is now scheduled'


# Availability was removed
@adapter(events.IOrderWfRemoveAvailability)
@implementer(IMail)
class OrderRemoveAvailabilityCreativeMail(OrderCreativeMail):
    """Email to creative on remove availability."""

    template_name = 'platform-order-cancellation-creative'
    subject = 'Important: Assignment {ASSIGNMENT_ID} cancelled'
