"""Briefy email action for Lead events tests."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack.lead import LeadCreated
from briefy.choreographer.events.lead import lead as events
from conftest import BaseActionCase


class TestLeadCreated(BaseActionCase):
    """Test for email sent on Lead creation."""

    action_class = LeadCreated
    action_interface = ISlack
    event_class = events.LeadCreated
    data_file = 'lead.json'

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload = obj.transform()
        assert isinstance(payload, list)
        assert len(payload) == 1
        payload = payload[0]
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
        category = fields[2]
        sub_category = fields[3]

        assert isinstance(fullname, dict)
        assert isinstance(email, dict)
        assert isinstance(category, dict)
        assert isinstance(sub_category, dict)

        assert 'title' in fullname.keys() and fullname['title'] == 'Fullname'
        assert 'value' in fullname.keys() and fullname['value'] == 'Leo'
        assert 'short' in fullname.keys() and fullname['short'] is True

        assert 'title' in email.keys() and email['title'] == 'Email'
        assert 'value' in email.keys() and email['value'] == 'leo@picsastock.com'
        assert 'short' in email.keys() and email['short'] is True

        assert 'title' in category.keys() and category['title'] == 'Category'
        assert 'value' in category.keys() and category['value'] == 'other'
        assert 'short' in category.keys() and category['short'] is True

        assert 'title' in sub_category.keys() and sub_category['title'] == 'Subcategory'
        assert 'value' in sub_category.keys() and sub_category['value'] == 'i am leo'
        assert 'short' in sub_category.keys() and sub_category['short'] is True
