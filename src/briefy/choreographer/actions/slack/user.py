"""Slack action for User."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events import user
from zope.component import adapter
from zope.interface import implementer


class UserSlack(Slack):
    """Base class for Slack message sent on User events."""

    entity = 'User'
    weight = 100
    _channel = '#test'


@adapter(user.IUserCreated)
@implementer(ISlack)
class UserCreated(UserSlack):
    """After creating a new User, post on Slack."""

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = 'New User created!'
        payload['text'] = 'New User was created, please take a look into the details:'
        payload['username'] = 'Briefy Bot'
        payload['data'] = {
            'fields': [
                {'title': 'Fullname',
                 'value': data.get('fullname'),
                 'short': True,
                 },
                {'title': 'Email',
                 'value': data.get('email'),
                 'short': True,
                 },
            ]
        }
        return payload


@adapter(user.IUserPasswordReset)
@implementer(ISlack)
class PasswordReset(UserSlack):
    """Post on slack the details of a password reset request."""

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = 'Password reset request'
        payload['text'] = 'The user {username} requested a password reset'.format(
            username=data.get('username')
        )
        payload['username'] = 'Briefy Bot'
        payload['data'] = {
            'fields': [
                {'title': 'Code',
                 'value': data.get('code'),
                 'short': True,
                 },
                {'title': 'IP Address',
                 'value': data.get('requested_from'),
                 'short': True,
                 },
                {'title': 'Expiration date',
                 'value': data.get('expiration_date'),
                 'short': True,
                 },
            ]
        }
        return payload
