"""Mail action for User."""
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.config import DELIVERY_URL
from briefy.choreographer.config import PLATFORM_URL
from briefy.choreographer.events import user
from zope.component import adapter
from zope.interface import implementer

import typing as t


class UserMail(Mail):
    """Base class for emails sent on User events."""

    weight = 100
    """Weight of the action.

    A lower number takes precedence over a higher number.
    """

    entity = 'User'
    """Name of the entity to be processed here."""

    def user_groups_slugs(self) -> t.Sequence[str]:
        """Given the event data, return a sequence of group slugs.

        :return: Sequence of group slugs
        """
        data = self.data
        groups = data.get('groups', [])
        slugs = {g.get('slug', '') for g in groups}
        return tuple(slugs)

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload[0]['fullname'] = data.get('fullname')
        payload[0]['email'] = data.get('email')
        payload[0]['data'] = {
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
        in_delivery = 'g:delivery' in self.user_groups_slugs()
        return available and data.get('internal') and not in_delivery


@adapter(user.IUserCreated)
@implementer(IMail)
class UserDeliveryCreated(UserMail):
    """After creating a new User with access to the delivery system, send an welcome email."""

    template_name = 'delivery-welcome-email'
    subject = 'Login to Briefy\'s platform and download your images'

    @property
    def available(self) -> bool:
        """Send email only if internal attribute is set on the payload and g:delivery is one ."""
        available = super().available
        in_delivery = 'g:delivery' in self.user_groups_slugs()
        return available and in_delivery

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload[0]['data'] = {
            'FIRSTNAME': data.get('first_name'),
            'FULLNAME': data.get('fullname'),
            'EMAIL': data.get('email'),
            'PASSWORD': data.get('initial_password'),
            'SUBJECT': self.subject,
            'URL': DELIVERY_URL,
        }
        return payload


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
        code = data['code']
        return f'{PLATFORM_URL}reset-password/{code}'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        expires = data.get('expiration_date')
        if expires.endswith('Z'):
            expires = expires[:-1]
        expires = self._format_datetime(expires)
        payload[0]['data']['CODE'] = data.get('code')
        payload[0]['data']['REQUESTED_FROM'] = data.get('requested_from')
        payload[0]['data']['EXPIRES'] = expires
        payload[0]['data']['ACTION_URL'] = self._action_url
        return payload
