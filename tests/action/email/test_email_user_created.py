"""Briefy email action for Lead events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.user import UserDeliveryCreated
from briefy.choreographer.events.user import user as events
from conftest import BaseActionCase


class TestUserDeliveryCreated(BaseActionCase):
    """Test for email sent on User creation."""

    action_class = UserDeliveryCreated
    action_interface = IMail
    action_info = 'notification - mail.queue - 100 - User - UserDeliveryCreated'
    event_class = events.UserCreated
    data_file = 'user.created.json'

    def test_available(self):
        """Test data transform."""
        obj = self.obj
        assert obj.available is True

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload = obj.transform()
        assert isinstance(payload, list)
        assert len(payload) == 1
        payload = payload[0]
        data = payload['data']
        assert isinstance(payload['sender_name'], str)
        assert isinstance(payload['sender_email'], str)
        assert isinstance(payload['fullname'], str)
        assert isinstance(payload['email'], str)
        assert isinstance(payload['subject'], str)
        assert isinstance(payload['template'], str)
        assert isinstance(payload['data'], dict)
        assert isinstance(data['FULLNAME'], str)
        assert isinstance(data['EMAIL'], str)
        assert isinstance(data['SUBJECT'], str)

        assert payload['sender_name'] == 'Briefy Team'  # Comes from default config
        assert payload['sender_email'] == 'site@briefy.co'  # Comes from default config
        assert payload['fullname'] == 'Foo Var'
        assert payload['email'] == 'foobar@briefy.co'
        assert payload['template'] == 'delivery-welcome-email-en-gb'
        assert payload['subject'] == 'Login to Briefy\'s platform and download your images'

        assert data['FULLNAME'] == 'Foo Var'
        assert data['EMAIL'] == 'foobar@briefy.co'
        assert data['PASSWORD'] == 'ZusPvN7'
        assert data['URL'] == 'https://delivery.stg.briefy.co/'
        assert data['SUBJECT'] == 'Login to Briefy\'s platform and download your images'
