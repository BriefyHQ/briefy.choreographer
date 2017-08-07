"""Mail actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_NAME

import typing as t


class IMail(IAction):
    """An Action that sends an email."""


class Mail(Action):
    """An Action that sends an email."""

    weight = 100
    _queue_name = 'mail.queue'
    template_name = ''
    """Name of the template to be used by this action."""
    entity = ''
    subject = 'Briefy!'
    """Subject to be used on the email."""

    @property
    def sender(self) -> dict:
        """Return sender information for this action.

        :returns: Dictionary with two keys - name, email
        """
        return {'name': MAIL_ACTION_LEICA_SENDER_NAME, 'email': MAIL_ACTION_LEICA_SENDER_EMAIL}

    @property
    def recipients(self) -> t.List[dict]:
        """Return a list of recipients for this action.

        :return: List of recipients to be receive a message.
        """
        raise NotImplementedError('Not implemented error')

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        available = super().available
        return True and available

    def get_template(self, language: str='en-gb') -> str:
        """Return the template name to be used on this action."""
        return f'{self.template_name}-{language}'

    def transform(self) -> t.List[dict]:
        """Transform data from the event.

        :returns: Dictionary with the event data transformed to be used on this action.
        """
        language = 'en-gb'
        event = self.event
        sender = self.sender
        payload = {
            'sender_name': sender.get('name'),
            'sender_email': sender.get('email'),
            'fullname': '',
            'email': '',
            'subject': self.subject,
            'template': self.get_template(language),
            'entity': self.entity,
            'guid': event.guid,
            'event_name': event.event_name,
            'data': {
            }
        }
        return [payload, ]
