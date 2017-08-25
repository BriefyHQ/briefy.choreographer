"""Briefy slack action for Leica order events tests."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack.leica.order import OrderWfAssign
from briefy.choreographer.events.leica.order import order as events
from conftest import BaseActionCase


class TestOrderWfAssign(BaseActionCase):
    """Test for slack action on Order assignment."""

    action_class = OrderWfAssign
    action_interface = ISlack
    action_info = 'notification - slack.queue - 100 - Order - OrderWfAssign'
    event_class = events.OrderWfAssign
    data_file = 'leica/order.created.json'

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

        customer = fields[0]
        project = fields[1]
        title = fields[2]
        id_ = fields[3]

        assert 'title' in customer.keys() and customer['title'] == 'Customer'
        assert 'value' in customer.keys() and customer['value'] == 'Agoda'
        assert 'short' in customer.keys() and customer['short'] is True

        assert 'title' in project.keys() and project['title'] == 'Project'
        assert 'value' in project.keys() and project['value'] == 'Agoda Bali'
        assert 'short' in project.keys() and project['short'] is True

        assert 'title' in title.keys() and title['title'] == 'Title'
        assert 'value' in title.keys() and title['value'] == 'Villa Undici Jalak'
        assert 'short' in title.keys() and title['short'] is True

        assert 'title' in id_.keys() and id_['title'] == 'ID'
        assert 'value' in id_.keys() and id_['value'] == '1701-PS1-560'
        assert 'short' in id_.keys() and id_['short'] is True
