"""Mail action for Leica."""
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_NAME


class LeicaMail(Mail):
    """Base class for emails sent on Leica events."""

    weight = 100
    """Weight of the action.

    A lower number takes precedence over a higher number.
    """

    entity = ''
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
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['fullname'] = data.get('fullname')
        payload['email'] = data.get('email')
        payload['data'] = {
            'FULLNAME': data.get('fullname'),
            'EMAIL': data.get('email'),
            'CATEGORY': data.get('category'),
            'SUBJECT': self.subject,
            'ACTION_URL': self._action_url
        }
        return payload
