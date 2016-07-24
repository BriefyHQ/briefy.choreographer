"""Briefy notification action for mail sent events tests."""
from briefy.choreographer.actions.notification import INotification
from briefy.choreographer.actions.notification.mail import MailSent
from briefy.choreographer.data.mail import MailDTO
from briefy.choreographer.events import mail as events
from conftest import BaseActionCase


class TestMailSent(BaseActionCase):
    """Test for notification handling on Mail sent."""

    action_class = MailSent
    action_interface = INotification
    event_class = events.MailSent
    data_class = MailDTO
    data_file = 'mail.json'

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload = obj.transform()
        assert isinstance(payload['fullname'], str)
        assert isinstance(payload['address'], str)
        assert isinstance(payload['subject'], str)
        assert isinstance(payload['gateway'], str)
        assert isinstance(payload['gateway_id'], str)
        assert isinstance(payload['type'], str)

        assert payload['fullname'] == 'Foo Bar'
        assert payload['address'] == 'foo@bar.com'
        assert payload['entity'] == 'Lead'
        assert payload['gateway'] == 'mandrill'
        assert payload['gateway_id'] == '7af0375da4024523816e0637a9051208'
        assert payload['subject'] == 'Briefy is coming soon!'
        assert payload['status'] == 'sent'
