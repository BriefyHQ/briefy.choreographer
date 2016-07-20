"""Mail actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction


class IMail(IAction):
    """Action that sends an email."""


class Mail(Action):
    """Action that sends an email."""

    weight = 100
    _queue_name = 'mail.queue'
    template_name = ''
    entity = ''
    subject = 'Briefy!'

    @property
    def recipient(self):
        """Return the data to be used as the recipient of this message."""
        raise NotImplementedError('Not implemented error')

    @property
    def available(self):
        """Check if this action is available."""
        return True

    def get_template(self, language='en-gb'):
        """Return the template name for this email."""
        return '{}-{}'.format(self.template_name, language)

    def transform(self):
        """Transform data."""
        language = 'en-gb'
        event = self.event
        payload = {
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
