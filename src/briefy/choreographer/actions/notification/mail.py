"""Mail action for Event."""
from briefy.choreographer.actions.notification import Notification
from briefy.choreographer.actions.notification import INotification
from briefy.choreographer.events import mail as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.IMailSent)
@implementer(INotification)
class MailSent(Notification):
    """Deal with emails sent by our solution."""

    entity = 'Mail'
    weight = 100

    def transform(self):
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['fullname'] = data.get('to_name')
        payload['address'] = data.get('to_email')
        payload['subject'] = data.get('subject')
        return payload
