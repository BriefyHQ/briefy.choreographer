"""Mail actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction


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
        return {
            'name': '',
            'email': '',
        }

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        raise NotImplementedError('Not implemented error')

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        return True

    def get_template(self, language='en-gb') -> str:
        """Return the template name to be used on this action."""
        return '{name}-{language}'.format(
            name=self.template_name,
            language=language
        )

    def transform(self) -> dict:
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
        return payload
