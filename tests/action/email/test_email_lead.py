"""Briefy email action for Lead events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.lead import LeadCreated
from briefy.choreographer.data.lead import LeadDTO
from briefy.choreographer.events.lead import lead as events
from conftest import BaseActionCase


class TestLeadCreated(BaseActionCase):
    """Test for email sent on Lead creation."""

    action_class = LeadCreated
    action_interface = IMail
    event_class = events.LeadCreated
    data_class = LeadDTO
    data_file = 'lead.json'

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload = obj.transform()
        data = payload['data']
        assert isinstance(payload['fullname'], str)
        assert isinstance(payload['email'], str)
        assert isinstance(payload['subject'], str)
        assert isinstance(payload['template'], str)
        assert isinstance(payload['data'], dict)
        assert isinstance(data['FULLNAME'], str)
        assert isinstance(data['EMAIL'], str)
        assert isinstance(data['CATEGORY'], str)
        assert isinstance(data['SUBJECT'], str)

        assert payload['fullname'] == 'Leo'
        assert payload['email'] == 'leo@picsastock.com'
        assert payload['template'] == 'birefy-new-lead-en-gb'
        assert payload['subject'] == 'Briefy is coming soon!'

        assert data['FULLNAME'] == 'Leo'
        assert data['EMAIL'] == 'leo@picsastock.com'
        assert data['SUBJECT'] == 'Briefy is coming soon!'
        assert data['CATEGORY'] == 'other'
