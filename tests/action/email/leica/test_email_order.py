"""Briefy email action for Quote events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import order as actions
from briefy.choreographer.events.leica import order as events
from conftest import BaseActionCase


class MailTest:
    """Base class to set common info for these tests."""

    action_interface = IMail
    data_file = 'leica/order.created.json'


class TestOrderCreatedCustomerMail(MailTest, BaseActionCase):
    """Test for email sent to customer on Order creation."""

    action_class = actions.OrderSubmitCustomerMail
    event_class = events.OrderWfSubmit

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload = obj.transform()
        data = payload['data']
        assert isinstance(payload['sender_name'], str)
        assert isinstance(payload['sender_email'], str)
        assert isinstance(payload['fullname'], str)
        assert isinstance(payload['email'], str)
        assert isinstance(payload['subject'], str)
        assert isinstance(payload['template'], str)
        assert isinstance(payload['data'], dict)
        assert isinstance(data['ID'], str)
        assert isinstance(data['ACTION_URL'], str)
        assert isinstance(data['EMAIL'], str)
        assert isinstance(data['FULLNAME'], str)
        assert isinstance(data['SLUG'], str)
        assert isinstance(data['ASSIGNMENT_ID'], str)
        assert isinstance(data['CUSTOMER'], str)
        assert isinstance(data['CUSTOMER_ORDER_ID'], str)
        assert isinstance(data['PROJECT'], str)
        assert isinstance(data['FORMATTED_ADDRESS'], str)
        assert isinstance(data['SCHEDULED_SHOOT_TIME'], str)
        assert isinstance(data['SUBJECT'], str)

        assert payload['fullname'] == 'Eyal Schondorf'
        assert payload['email'] == 'eyal.schondorf_agoda.com@briefy.co'
        assert payload['template'] == 'platform-order-created-en-gb'
        assert payload['subject']

        assert data['FULLNAME'] == 'Eyal Schondorf'
        assert data['EMAIL'] == 'eyal.schondorf_agoda.com@briefy.co'
        assert data['SUBJECT']


class OrderCreatedScoutMail(MailTest, BaseActionCase):
    """Test for email sent to scout on Order creation."""

    action_class = actions.OrderSubmitScoutMail
    event_class = events.OrderWfSubmit

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload = obj.transform()
        data = payload['data']
        assert payload['fullname'] == 'Briefy Scouters'
        assert payload['email'] == 'scouting@briefy.co'
        assert payload['template'] == 'platform-order-created-scouting-en-gb'
        assert data['FULLNAME'] == 'Briefy Scouters'
        assert data['EMAIL'] == 'scouting@briefy.co'
        assert data['SUBJECT'] == '''New order created by *|CUSTOMER|*'''
