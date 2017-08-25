"""Mail action for Leica."""
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_NAME

import typing as t


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

    def _recipients(self, field_name: str) -> t.List[dict]:
        """Return a list of valid recipients."""
        data = self.data
        recipients = []
        if field_name == 'last_transition':
            history = data['state_history']
            actor = history[-1]['actor']
            users = [actor, ]
        else:
            users = data[field_name]
        for user in users:
            if not user['internal']:
                continue
            recipients.append(
                {
                    'first_name': user['first_name'],
                    'fullname': user['fullname'],
                    'email': user['email'],
                }
            )
        return recipients

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload[0]['fullname'] = data.get('fullname')
        payload[0]['email'] = data.get('email')
        payload[0]['data'] = {
            'FULLNAME': data.get('fullname'),
            'EMAIL': data.get('email'),
            'CATEGORY': data.get('category'),
            'SUBJECT': self.subject,
            'ACTION_URL': self._action_url
        }
        return payload
