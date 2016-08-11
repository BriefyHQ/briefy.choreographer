"""Briefy email action for Lead events tests."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack.lead import LeadCreated
from briefy.choreographer.data.lead import LeadDTO
from briefy.choreographer.events.lead import lead as events
from conftest import BaseActionCase


class TestLeadCreated(BaseActionCase):
    """Test for email sent on Lead creation."""

    action_class = LeadCreated
    action_interface = ISlack
    event_class = events.LeadCreated
    data_class = LeadDTO
    data_file = 'lead.json'

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
        assert isinstance(payload['data'], dict)
        assert isinstance(data['FULLNAME'], str)
        assert isinstance(data['EMAIL'], str)
        assert isinstance(data['CATEGORY'], str)
        assert isinstance(data['SUBCATEGORY'], str)

        #assert payload['sender_name'] == 'Andre from Briefy'  # Comes from default config
        #assert payload['sender_email'] == 'hello@briefy.co'  # Comes from default config
        #assert payload['fullname'] == 'Leo'
        #assert payload['email'] == 'leo@picsastock.com'
        #assert payload['template'] == 'briefy-new-lead-en-gb'
        #assert payload['subject'] == '''You're Officially a Briefy Insider!'''

        #assert data['FULLNAME'] == 'Leo'
        #assert data['EMAIL'] == 'leo@picsastock.com'
        #assert data['SUBJECT'] == '''You're Officially a Briefy Insider!'''
        #assert data['CATEGORY'] == 'other'
