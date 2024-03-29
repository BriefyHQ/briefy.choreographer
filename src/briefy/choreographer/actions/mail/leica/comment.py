"""Mail action for Comments."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import LeicaMail
from briefy.choreographer.config import PLATFORM_URL
from briefy.choreographer.events.leica import comment as events
from zope.component import adapter
from zope.interface import implementer

import typing as t


class CommentMail(LeicaMail):
    """Base class for emails sent on Comment events."""

    entity = 'Comment'
    """Name of the entity to be processed here."""

    @property
    def action_url(self) -> str:
        """Action URL."""
        return self._action_url

    def transform(self) -> t.List[dict]:
        """Transform data."""
        base_payload = super().transform()[0]
        data = self.data
        recipients = self.recipients
        payload = []
        for recipient in recipients:
            payload_item = {}
            payload_item.update(base_payload)
            payload_item['fullname'] = recipient.get('fullname')
            payload_item['email'] = recipient.get('email')
            author = data.get('author', {})
            payload_item['data'] = {
                'ID': data.get('id'),
                'ACTION_URL': self.action_url,
                'COMMENTER_FIRSTNAME': author.get('first_name', ),
                'EMAIL': recipient.get('email'),
                'FULLNAME': recipient.get('fullname'),
                'FIRSTNAME': recipient.get('first_name'),
                'SLUG': data['entity']['slug'],
                'COMMENT': data.get('content'),
                'SUBJECT': self.subject,
            }
            subject = self.subject.format(**payload_item['data'])
            payload_item['subject'] = subject
            payload_item['data']['SUBJECT'] = subject
            payload.append(payload_item)
        return payload


class CommentCustomerMail(CommentMail):
    """Base class for emails sent to the Customer on Comment events."""

    @property
    def recipients(self) -> t.List[dict]:
        """Return the data to be used as the recipient of this message."""
        return self._recipients('customer_users')


class CommentCreativeMail(CommentMail):
    """Base class for emails sent to the Creative on Comment events."""

    @property
    def recipients(self) -> t.List[dict]:
        """Return the data to be used as the recipient of this message."""
        return self._recipients('professional_user')


class CommentPMMail(CommentMail):
    """Base class for emails sent to the PMs on Comment events."""

    @property
    def recipients(self) -> t.List[dict]:
        """Return the data to be used as the recipient of this message."""
        return self._recipients('project_managers')


# Comment Created to Customer
@adapter(events.ICommentCreated)
@implementer(IMail)
class CommentCreatedToCreative(CommentCreativeMail):
    """Email to creative on new comment created."""

    template_name = 'platform-comment-created'
    subject = '{COMMENTER_FIRSTNAME} has commented on your assignment'

    @property
    def action_url(self) -> str:
        """Action URL."""
        data = self.data
        id_ = data['entity']['id']
        return f'{PLATFORM_URL}assignments/{id_}'

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        to_role = data['to_role']
        return (to_role == 'professional_user') and available


# Comment Created to Customer
@adapter(events.ICommentCreated)
@implementer(IMail)
class CommentCreatedToCustomer(CommentCustomerMail):
    """Email to customer on comment created."""

    template_name = 'platform-comment-created-to-customer'
    subject = '{COMMENTER_FIRSTNAME} has commented on your order'

    @property
    def action_url(self) -> str:
        """Action URL."""
        data = self.data
        id_ = data['entity']['id']
        return f'{PLATFORM_URL}orders/{id_}'

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        to_role = data['to_role']
        return (to_role == 'customer_user') and available


# Comment Created by Customer to PM
@adapter(events.ICommentCreated)
@implementer(IMail)
class CommentCreatedByCustomerToPM(CommentPMMail):
    """Email to PM on comment created."""

    template_name = 'platform-comment-created-to-pm'
    subject = '{COMMENTER_FIRSTNAME} commented on an order'

    @property
    def action_url(self) -> str:
        """Action URL."""
        data = self.data
        id_ = data['entity']['id']
        return f'{PLATFORM_URL}orders/{id_}'

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        data = self.data
        from_role = data['author_role']
        to_role = data['to_role']
        return (from_role == 'customer_user') and (to_role == 'project_manager') and available
