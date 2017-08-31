"""Briefy email action for Lead events tests."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack.package_order import PackageOrderCreated
from briefy.choreographer.events import lead as events
from conftest import BaseActionCase


class TestPackageOrderCreated(BaseActionCase):
    """Test for email sent on Lead creation."""

    action_class = PackageOrderCreated
    action_interface = ISlack
    action_info = 'notification - slack.queue - 100 - PackageOrder - PackageOrderCreated'
    event_class = events.PackageOrderCreated
    data_file = 'package_order.created.json'

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

        to_check = [
            ('Company', 'Briefy', False),
            ('Fullname', 'Érico Andrei', True),
            ('Email', 'erico@briefy.co', True),
            ('Contact Role', 'CTO', True),
            ('Package', 'chalet', False),
            ('Total shoots', 100, True),
            ('Category', 'Apartments', True),
            ('Locations', '2: au-sydney, br-rio-janeiro', False),
            (
                'Add ons',
                'scheduling: Selected, quality-check: Selected, post_processing: Selected',
                False
            ),
        ]
        for idx, item in enumerate(to_check):
            field = fields[idx]
            assert field['title'] == item[0]
            assert field['value'] == item[1]
            assert field['short'] == item[2]
