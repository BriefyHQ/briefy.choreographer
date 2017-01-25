"""Mail action for Comments."""
from briefy.choreographer.config import PLATFORM_URL
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import LeicaMail
from briefy.choreographer.events.leica import comment as events
from zope.component import adapter
from zope.interface import implementer


class CommentMail(LeicaMail):
    """Base class for emails sent on Comment events."""""

    entity = 'Comment'
    """Name of the entity to be processed here."""

    @property
    def action_url(self):
        """Action URL."""
        return self._action_url

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        recipient = self.recipient
        payload['fullname'] = recipient.get('fullname')
        payload['email'] = recipient.get('email')
        author = data.get('author', {})
        payload['data'] = {
            'ID': data.get('id'),
            'ACTION_URL': self.action_url,
            'COMMENTER_FIRSTNAME': author.get('first_name', ),
            'EMAIL': recipient.get('email'),
            'FULLNAME': recipient.get('fullname'),
            'FIRSTNAME': recipient.get('first_name'),
            'SLUG': recipient.get('slug'),
            'COMMENT': data.get('content'),
            'SUBJECT': self.subject,
        }
        return payload


class CommentCustomerMail(CommentMail):
    """Base class for emails sent to the Customer on Comment events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        data = self.data['entity']
        return {
            'first_name': data['customer_user']['first_name'],
            'fullname': data['customer_user']['fullname'],
            'email': data['customer_user']['email'],
        }


class CommentCreativeMail(CommentMail):
    """Base class for emails sent to the Creative on Comment events."""

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        data = self.data['entity']
        return {
            'first_name': data['professional_user']['first_name'],
            'fullname': data['professional_user']['fullname'],
            'email': data['professional_user']['email'],
        }


# Order Created by Customer
@adapter(events.ICommentCreated)
@implementer(IMail)
class CommentCreatedToCreative(CommentCreativeMail):
    """Email to creative on new comment created."""

    template_name = 'platform-comment-created'
    subject = '''*|COMMENTER_FIRSTNAME|* has commented on your assignment'''

    @property
    def action_url(self):
        """Action URL."""
        data = self.data
        return '{base}assignments/{id}'.format(
            id=data['entity']['id'],
            base=PLATFORM_URL
        )

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        to_role = data['to_role']
        return (to_role == 'professional_user') and available


# Order Created by Customer
@adapter(events.ICommentCreated)
@implementer(IMail)
class CommentCreatedToCustomer(CommentCustomerMail):
    """Email to customer on comment created."""

    template_name = 'platform-comment-created-to-customer'
    subject = '''*|COMMENTER_FIRSTNAME|* has commented on your order'''

    @property
    def action_url(self):
        """Action URL."""
        data = self.data
        return '{base}orders/{id}'.format(
            id=data['entity']['id'],
            base=PLATFORM_URL
        )

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        to_role = data['to_role']
        return (to_role == 'customer_user') and available
