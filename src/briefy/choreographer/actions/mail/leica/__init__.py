"""Mail action for Leica."""
from briefy.choreographer import logger
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_LEICA_SENDER_NAME
from briefy.choreographer.utils.user_data import users_data_by_group

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
        if field_name == 'last_transition':
            history = data['state_history']
            actor = history[-1]['actor']
            recipients = [actor, ]
        else:
            recipients = users_data_by_group(
                self.event,
                field_name,
                check_notification=True
            )
        if not recipients:
            metadata = self.metadata
            event_name = metadata['event_name']
            queue_name = metadata['queue_name']
            action_name = metadata['action_name']
            log_extra = metadata['log_extra']
            logger.warn(
                f'No recipients for {event_name}: {queue_name} action {action_name}',
                extra=log_extra
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
