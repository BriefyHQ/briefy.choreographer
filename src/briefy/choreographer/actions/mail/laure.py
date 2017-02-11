"""Mail action for Lead."""
from briefy.common.utils.data import Objectify
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_NAME
from briefy.choreographer.events import laure
from zope.component import adapter
from zope.interface import implementer

import uuid

class LaureMail(Mail):
    """Base class for emails sent on Lead events."""

    weight = 100
    """Weight of the action.

    A lower number takes precedence over a higher number.
    """

    entity = 'Assignment'
    """Name of the entity to be processed here."""

    @property
    def sender(self) -> dict:
        """Return sender information for this action.

        :returns: Dictionary with two keys - name, email
        """
        return {
            'name': MAIL_ACTION_LEICA_SENDER_NAME,
            'email': MAIL_ACTION_LEICA_SENDER_EMAIL,
        }

    def transform(self) -> dict:
        payload = Objectify(super().transform())

        payload.sender_email = MAIL_ACTION_LEICA_SENDER_EMAIL
        payload.sender_name = MAIL_ACTION_LEICA_SENDER_NAME
        payload.entity = 'Assignment'
        payload.guid = str(uuid.uuid4())

        return payload.dct

'''
# Message not implemented - mostly, missing a template.

@adapter(laure.ILaureAssignmentValidated)
@implementer(IMail)
class LaureValidates(LaureMail):
    """Sends e-mail to QA team on set automatic aproval"""

    template_name = 'qa-automatic-reject-en-gb'
    # template = 'qa-automatic-not-enough-en-gb'
'''

@adapter(laure.ILaureAssignmentRejected)
@implementer(IMail)
class LaureInvalidates(LaureMail):
    """Email to be sent when automatic validation failed."""

    template_name = 'qa-automatic-reject-en-gb'
    # template = 'qa-automatic-not-enough-en-gb'
    subject = ''
    @property
    def subject(self):

        subject = ''''{id}' Automatic Check for images failed: re-submission needed!'''.format(
            id=self.assignment_title)

    def transform(self)->dict:

        payload = Objectify(super().transform())
        data = Objectify(self.data)

        # Details format: List of 2-tuples with image name/reason string
        image_details = '<ul>\n    {0}\n</ul>'.format('\n    '.join([
            '<li>{0}</li>'.format(
                '{name} - {reason}'.join(name=v[0], reason=v[1]))
                for v in data.validation_info.failed.dct
            ])
        )

        details = data.validation_info.complete_feedback + '\n\n' + image_details

        payload.subject = ''''{id}' Automatic Check for images failed: re-submission needed!'''.format(
            id=self.assignment_title)


        payload.fullname = data.assignment_info.professional_name,
        payload.email = data.assignment_info.professional_email
        payload.subject = ''''{id}' Automatic Check for images failed: '''\
            '''re-submission needed!'''.format(
                id=data.assigment_info.code)
        payload.event_name = 'assigment.invalidate'
        payload.data = {}
        payload.data.SUBJECT = payload.subject
        payload.data.JOB_ID = data.assigment_info.id
        payload.data.ERRORS = details

        return payload.dct
