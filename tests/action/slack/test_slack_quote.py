"""Briefy email action for Lead events tests."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack.quote import QuoteCreated
from briefy.choreographer.events.lead import lead as events
from conftest import BaseActionCase


class TestQuoteCreated(BaseActionCase):
    """Test for email sent on Lead creation."""

    action_class = QuoteCreated
    action_interface = ISlack
    event_class = events.QuoteCreated
    data_file = 'quote.json'

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload = obj.transform()
        data = payload['data']
        assert isinstance(payload['channel'], str)
        assert isinstance(payload['title'], str)
        assert isinstance(payload['text'], str)
        assert isinstance(payload['color'], str)
        assert isinstance(payload['icon'], str)
        assert isinstance(payload['username'], str)
        assert isinstance(data, dict)

        fields = data['fields']
        assert isinstance(fields, list)

        fullname = fields[0]
        email = fields[1]
        phone_number = fields[2]
        company = fields[3]
        company_site = fields[4]

        assert all(isinstance(field, dict) and field['short'] is True for field in fields)

        assert fullname['title'] == 'Fullname'
        assert fullname['value'] == 'Leo Aslam'

        assert email['title'] == 'Email'
        assert email['value'] == 'leo@picsastock.com'

        assert phone_number['title'] == 'Phone Number'
        assert phone_number['value'] == '+49 151 456 4444'

        assert company['title'] == 'Company'
        assert company['value'] == 'Briefy'

        assert company_site['title'] == 'Company Site'
        assert company_site['value'] == 'https://briefy.co'
