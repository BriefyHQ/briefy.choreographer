"""Mail action for Event."""
from briefy.choreographer.actions.notification import INotification
from briefy.choreographer.actions.notification import Notification
from briefy.choreographer.events import mail as events
from zope.component import adapter
from zope.interface import implementer

import typing as t


@adapter(events.IMailSent)
@implementer(INotification)
class MailSent(Notification):
    """Deal with emails sent by Briefy."""

    entity = 'Mail'
    weight = 100

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload[0]['fullname'] = data.get('to_name')
        payload[0]['address'] = data.get('to_email')
        payload[0]['subject'] = data.get('subject')
        return payload
