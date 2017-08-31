"""Briefy email action for Quote events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.quote import QuoteCreated
from briefy.choreographer.events import lead as events
from conftest import BaseActionCase


class TestQuoteCreated(BaseActionCase):
    """Test for email sent on Lead creation."""

    action_class = QuoteCreated
    action_interface = IMail
    action_info = 'notification - mail.queue - 100 - Quote - QuoteCreated'
    event_class = events.QuoteCreated
    data_file = 'quote.json'

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
        assert isinstance(payload['company'], str)
        assert isinstance(payload['phone_number'], str)
        assert isinstance(payload['company_site'], str)
        assert isinstance(payload['subject'], str)
        assert isinstance(payload['template'], str)
        assert isinstance(payload['data'], dict)
        assert isinstance(data['FULLNAME'], str)
        assert isinstance(data['EMAIL'], str)
        assert isinstance(data['SUBJECT'], str)

        assert payload['sender_name'] == 'Andre from Briefy'  # Comes from default config
        assert payload['sender_email'] == 'hello@briefy.co'  # Comes from default config
        assert payload['fullname'] == 'Leo Aslam'
        assert payload['email'] == 'leo@picsastock.com'
        assert payload['template'] == 'briefy-new-quote-en-gb'
        assert payload['subject']

        assert data['FULLNAME'] == 'Leo Aslam'
        assert data['EMAIL'] == 'leo@picsastock.com'
        assert data['SUBJECT']
