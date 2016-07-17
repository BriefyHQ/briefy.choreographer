"""Briefy email action for Lead events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.lead import LeadCreated
from briefy.choreographer.data.lead import LeadDTO
from briefy.choreographer.events.lead import lead as events
from conftest import BaseActionCase


class LeadCreated(BaseActionCase):
    """Test for email sent on Lead creation."""

    action_class = LeadCreated
    action_interface = IMail
    event_class = events.LeadCreated
    data_class = LeadDTO
    data_file = 'lead.json'

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        data = obj.transform()
        assert isinstance(data['fullName'], str)
        assert isinstance(data['email'], str)
        assert isinstance(data['template'], str)
        assert isinstance(data['data'], dict)
