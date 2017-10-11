"""Briefy notification action for mail sent events tests."""
from briefy.choreographer.actions.route import IRouteAction
from briefy.choreographer.actions.route.assignment import AssignmentWfReadyForUpload
from briefy.choreographer.events.leica import assignment as events
from conftest import BaseActionCase


class TestMailSent(BaseActionCase):
    """Test for laure handling on Mail sent."""

    action_class = AssignmentWfReadyForUpload
    action_interface = IRouteAction
    action_info = 'service_message - delivery.queue - 100 - Assignment - AssignmentWfReadyForUpload'
    event_class = events.AssignmentWfReadyForUpload
    data_file = 'leica/assignment.workflow.ready_for_upload.json'

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload = obj.transform()
        assert isinstance(payload, list)
        assert len(payload) == 1
        payload = payload[0]
        keys = ['id', 'created_at', 'data', 'guid', 'event_name']
        for item in keys:
            assert item in payload

        assert isinstance(payload['id'], str)
        assert isinstance(payload['created_at'], str)
        assert isinstance(payload['data'], dict)
        assert isinstance(payload['guid'], str)
        assert isinstance(payload['event_name'], str)

        assert payload['created_at'] == '2016-07-01T12:32:45'
        assert payload['guid'] == 'c04dc102-7d3b-4574-a261-4bf72db571db'
        assert payload['event_name'] == 'assignment.workflow.ready_for_upload'
