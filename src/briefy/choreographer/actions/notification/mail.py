"""Mail action for Lead."""
from briefy.choreographer.actions.notification import Notification
from briefy.choreographer.actions.notification import INotification
from briefy.choreographer.data.mail import IMailDTO
from briefy.choreographer.events import mail as events
from zope.component import adapter
from zope.interface import implementer


@adapter(IMailDTO, events.IMailSent)
@implementer(INotification)
class MailSent(Notification):
    """Deal with emails sent by our solution."""

    entity = 'Mail'
    weight = 100

    def transform(self):
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['fullname'] = data.to_name
        payload['address'] = data.to_email
        payload['subject'] = data.subject
        return payload
