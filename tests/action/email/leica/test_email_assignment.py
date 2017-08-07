"""Briefy email action for Assignment events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import assignment as actions
from briefy.choreographer.events.leica import assignment as events
from conftest import BaseActionCase


class MailTest:
    """Base class to set common info for these tests."""

    action_interface = IMail


class TestAssignmentScheduleCreativeMail(MailTest, BaseActionCase):
    """Test for email sent to creative on Assignment schedule."""

    data_file = 'leica/assigment.workflow.schedule.json'
    action_class = actions.AssignmentScheduleCreativeMail
    event_class = events.AssignmentWfSchedule

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
            assert isinstance(payload['attachments'], list)
            assert isinstance(data['ACTION_URL'], str)
            assert isinstance(data['CONTACT_FULLNAME'], str)
            assert isinstance(data['CONTACT_PHONE'], str)
            assert isinstance(data['EMAIL'], str)
            assert isinstance(data['FIRSTNAME'], str)
            assert isinstance(data['FORMATTED_ADDRESS'], str)
            assert isinstance(data['FULLNAME'], str)
            assert isinstance(data['ID'], str)
            assert isinstance(data['NUMBER_REQUIRED_ASSETS'], int)
            assert isinstance(data['PROJECT'], str)
            assert isinstance(data['REQUIREMENTS'], str)
            assert isinstance(data['SCHEDULED_SHOOT_TIME'], str)
            assert isinstance(data['SLUG'], str)
            assert isinstance(data['SUBJECT'], str)
            assert isinstance(data['TITLE'], str)

            assert payload['email'].endswith('@email.briefy.co')
            assert payload['template'] == 'platform-assignment-scheduled-en-gb'
            assert payload['subject']

            assert data['EMAIL'].endswith('@email.briefy.co')
            assert data['SUBJECT']

    def test_ics_attachment(self):
        """Test ics attachment."""
        import base64
        import icalendar

        obj = self.obj
        payload_list = obj.transform()
        payload = payload_list[0]
        assert isinstance(payload['attachments'], list)
        assert len(payload['attachments']) == 1
        ics_attachment = payload['attachments'][0]

        assert isinstance(ics_attachment, dict)
        assert ics_attachment['name'] == '{slug}.ics'.format(slug=obj.data['slug'])
        assert ics_attachment['type'] == 'text/calendar'
        assert isinstance(ics_attachment['content'], str)
        decoded = base64.b64decode(ics_attachment['content'])
        assert isinstance(decoded, bytes)
        calendar = icalendar.Calendar.from_ical(decoded)
        assert isinstance(calendar, icalendar.Calendar)
        event = calendar.subcomponents[0]
        assert isinstance(event, icalendar.Event)
        assert event['status'] == 'CONFIRMED'
        assert event['uid'] == obj.data['id']


class TestAssignmentRescheduleCreativeMail(TestAssignmentScheduleCreativeMail):
    """Test for email sent to creative on Assignment reschedule."""

    action_class = actions.AssignmentRescheduleCreativeMail
    event_class = events.AssignmentWfReschedule

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload_list = obj.transform()
        for payload in payload_list:
            assert payload['template'] == 'platform-assignment-rescheduled-en-gb'


class TestAssignmentCancelledCreativeMail(MailTest, BaseActionCase):
    """Test for email sent to creative on Assignment cancellation."""

    data_file = 'leica/assignment.workflow.cancel.json'
    action_class = actions.AssignmentCancelledCreativeMail
    event_class = events.AssignmentWfCancel

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload_list = obj.transform()
        for payload in payload_list:
            assert isinstance(payload['attachments'], list)
            assert payload['template'] == 'platform-order-cancellation-creative-en-gb'

    def test_ics_attachment(self):
        """Test ics attachment."""
        import base64
        import icalendar

        obj = self.obj
        payload_list = obj.transform()
        payload = payload_list[0]
        ics_attachment = payload['attachments'][0]
        decoded = base64.b64decode(ics_attachment['content'])
        calendar = icalendar.Calendar.from_ical(decoded)
        event = calendar.subcomponents[0]
        assert event['status'] == 'CANCELLED'
        assert event['uid'] == obj.data['id']
