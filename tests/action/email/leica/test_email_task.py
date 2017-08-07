"""Briefy email action for Assignment events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import task as actions
from briefy.choreographer.events.leica import task as events
from conftest import BaseActionCase


class MailTest:
    """Base class to set common info for these tests."""

    action_interface = IMail


class TestAssignmentNotifyLateSubmissionSuccess(MailTest, BaseActionCase):
    """Test for email sent to creative on Assignment late submissions."""

    data_file = 'leica/leica.task.assignment.notify_late_submission.success.json'
    action_class = actions.AssignmentNotifyLateSubmissionSuccess
    event_class = events.AssignmentNotifyLateSubmissionSuccess

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload_list = obj.transform()
        subject = 'Reminder: Late submission for Assignment 1707-Z1C-02H_01'
        for payload in payload_list:
            data = payload['data']
            assert isinstance(payload['sender_name'], str)
            assert isinstance(payload['sender_email'], str)
            assert isinstance(payload['fullname'], str)
            assert isinstance(payload['email'], str)
            assert isinstance(payload['subject'], str)
            assert isinstance(payload['template'], str)
            assert isinstance(payload['data'], dict)
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
            assert payload['template'] == 'platform-assignment-reminder-late-submission-en-gb'
            assert payload['subject'] == subject

            assert data['EMAIL'].endswith('@email.briefy.co')
            assert data['SUBJECT'] == subject


class TestAssignmentNotifyLateReSubmissionSuccess(TestAssignmentNotifyLateSubmissionSuccess):
    """Test for email sent to creative on Assignment late re submissions."""

    data_file = 'leica/leica.task.assignment.notify_late_resubmission.success.json'

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        payload_list = obj.transform()
        subject = 'Reminder: Late re-submission for Assignment 1707-Z1C-02H_01'
        for payload in payload_list:
            data = payload['data']
            assert isinstance(payload['sender_name'], str)
            assert isinstance(payload['sender_email'], str)
            assert isinstance(payload['fullname'], str)
            assert isinstance(payload['email'], str)
            assert isinstance(payload['subject'], str)
            assert isinstance(payload['template'], str)
            assert isinstance(payload['data'], dict)
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
            assert payload['template'] == 'platform-assignment-reminder-late-resubmission-en-gb'
            assert payload['subject'] == subject

            assert data['EMAIL'].endswith('@email.briefy.co')
            assert data['SUBJECT'] == subject
