"""Mail action for User."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.config import MAIL_ACTION_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_SENDER_NAME
from briefy.choreographer.config import PLATFORM_URL
from briefy.choreographer.events import user
from zope.component import adapter
from zope.interface import implementer


class UserMail(Mail):
    """Base class for emails sent on User events."""

    weight = 100
    """Weight of the action.

    A lower number takes precedence over a higher number.
    """

    entity = 'User'
    """Name of the entity to be processed here."""

    @property
    def sender(self) -> dict:
        """Return sender information for this action.

        :returns: Dictionary with two keys - name, email
        """
        return {
            'name': MAIL_ACTION_SENDER_NAME,
            'email': MAIL_ACTION_SENDER_EMAIL,
        }

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['fullname'] = data.get('fullname')
        payload['email'] = data.get('email')
        payload['data'] = {
            'FIRSTNAME': data.get('first_name'),
            'FULLNAME': data.get('fullname'),
            'EMAIL': data.get('email'),
            'SUBJECT': self.subject,
            'PLATFORM': PLATFORM_URL,
        }
        return payload


@adapter(user.IUserCreated)
@implementer(IMail)
class UserCreated(UserMail):
    """After creating a new User, send an email."""

    template_name = 'platform-user-created'
    subject = 'Welcome to Briefy!'

    @property
    def available(self) -> bool:
        """Send email only if internal attribute is set on the payload."""
        available = super().available
        data = self.data
        return available and data.get('internal')


@adapter(user.IUserPasswordReset)
@implementer(IMail)
class PasswordReset(UserMail):
    """Send an email to the user the details of a password reset request."""

    template_name = 'platform-user-password-request'
    subject = 'Reset your password'

    @property
    def _action_url(self) -> str:
        """Return the action URL for the object."""
        data = self.data
        return '{base}reset-password/{code}'.format(
            base=PLATFORM_URL,
            code=data['code']
        )

    @property
    def available(self) -> bool:
        """Send email only if internal attribute is set on the payload."""
        available = super().available
        return available

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        expires = data.get('expiration_date')
        if expires.endswith('Z'):
            expires = expires[:-1]
        expires = self._format_datetime(expires)
        payload['data']['CODE'] = data.get('code')
        payload['data']['REQUESTED_FROM'] = data.get('requested_from')
        payload['data']['EXPIRES'] = expires
        payload['data']['ACTION_URL'] = self._action_url
        return payload
