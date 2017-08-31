"""Briefy email action for Quote events tests."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail.leica import comment as actions
from briefy.choreographer.events.leica import comment as events
from conftest import BaseActionCase


class MailTest:
    """Base class to set common info for these tests."""

    action_interface = IMail
    data_file = 'leica/order.comment.created.json'


class TestCommentCreatedByCustomerToPM(MailTest, BaseActionCase):
    """Test for email sent to Project Manager on Comment creation."""

    action_class = actions.CommentCreatedByCustomerToPM
    action_info = 'notification - mail.queue - 100 - Comment - CommentCreatedByCustomerToPM'
    event_class = events.CommentCreated

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
            assert isinstance(data['ID'], str)
            assert isinstance(data['ACTION_URL'], str)
            assert isinstance(data['EMAIL'], str)
            assert isinstance(data['FULLNAME'], str)
            assert isinstance(data['SLUG'], str)
            assert isinstance(data['COMMENTER_FIRSTNAME'], str)
            assert isinstance(data['COMMENT'], str)

            assert payload['email'].endswith('briefy.co')
            assert payload['template'] == 'platform-comment-created-to-pm-en-gb'
            assert payload['subject']

            assert data['EMAIL'].endswith('briefy.co')
            assert data['SUBJECT']
