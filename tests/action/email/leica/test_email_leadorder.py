"""Briefy email action for Quote events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import order as actions
from briefy.choreographer.events.leica.order import leadorder as events
from conftest import BaseActionCase


class MailTest:
    """Base class to set common info for these tests."""

    action_interface = IMail
    data_file = 'leica/leadorder.workflow.assign.json'


class TestLeadOrderCreatedCustomerMail(MailTest, BaseActionCase):
    """Test for email sent to customer on Order creation."""

    action_class = actions.OrderSubmitCustomerMail
    action_info = 'notification - mail.queue - 100 - Order - OrderSubmitCustomerMail'
    event_class = events.LeadOrderWfSubmit

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload_list = obj.transform()
        for payload in payload_list:
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

            assert payload['email'].endswith('@email.briefy.co')
            assert payload['template'] == 'platform-order-created-en-gb'
            assert payload['subject']

            assert data['EMAIL'].endswith('@email.briefy.co')
            assert data['SUBJECT']


class TestLeadOrderCreatedScoutMail(MailTest, BaseActionCase):
    """Test for email sent to scout on Order creation."""

    action_class = actions.OrderSubmitScoutMail
    action_info = 'notification - mail.queue - 100 - Order - OrderSubmitScoutMail'
    event_class = events.LeadOrderWfSubmit

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload_list = obj.transform()
        for payload in payload_list:
            data = payload['data']
            assert payload['fullname'] == 'Briefy Scouters'
            assert payload['email'] == 'scouting@briefy.co'
            assert payload['template'] == 'platform-order-created-scouting-en-gb'
            assert data['FULLNAME'] == 'Briefy Scouters'
            assert data['EMAIL'] == 'scouting@briefy.co'
            assert data['SUBJECT'].startswith('New order created by')


class TestLeadOrderAssignedCustomerMail(MailTest, BaseActionCase):
    """Test for email sent to customers on Order assigned."""

    action_class = actions.OrderAssignedCustomerMail
    action_info = 'notification - mail.queue - 100 - Order - OrderAssignedCustomerMail'
    event_class = events.LeadOrderWfAssign
    messages = 7

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload_list = obj.transform()
        all_recipients = []
        for payload in payload_list:
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

            assert payload['email'].endswith('@email.briefy.co')
            assert payload['template'] == 'platform-order-assigned-en-gb'
            assert payload['subject'].startswith(
                'A Briefy content creator has been assigned to your order'
            )
            all_recipients.append(payload['fullname'])

        # Eyal Schondorf is set as internal=false
        assert 'Eyal Schondorf' not in all_recipients
