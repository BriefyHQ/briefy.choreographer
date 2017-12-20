"""Slack action for User."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.events import user
from zope.component import adapter
from zope.interface import implementer

import typing as t


class UserSlack(Slack):
    """Base class for Slack message sent on User events."""

    entity = 'User'
    weight = 100
    _channel = '#leica-users'


@adapter(user.IUserCreated)
@implementer(ISlack)
class UserCreated(UserSlack):
    """After creating a new User, post on Slack."""

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload_item = payload[0]
        payload_item['title'] = 'New User created!'
        payload_item['text'] = 'New User was created, please take a look into the details:'
        payload_item['username'] = 'Briefy Bot'
        payload_item['data'] = {
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

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        username = data.get('email')
        payload_item = payload[0]
        payload_item['title'] = 'Password reset request'
        payload_item['text'] = f'The user {username} requested a password reset'
        payload_item['username'] = 'Briefy Bot'
        payload_item['data'] = {
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


@adapter(user.IUserPasswordChanged)
@implementer(ISlack)
class UserPasswordChanged(UserSlack):
    """Post on slack on an user password changed."""

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        username = data.get('email')
        payload_item = payload[0]
        payload_item['title'] = 'User changed password'
        payload_item['text'] = f'The user {username} changed its password'
        payload_item['username'] = 'Briefy Bot'
        return payload


@adapter(user.IUserLogin)
@implementer(ISlack)
class UserLogin(UserSlack):
    """Post on slack on a user login."""

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        username = data.get('email')
        groups = ''
        if isinstance(data.get('groups'), list):
            groups = ', '.join([g['slug'] for g in data['groups']])
        payload_item = payload[0]
        payload_item['title'] = 'User login'
        payload_item['text'] = f'The user {username} just logged in on Leica'
        payload_item['username'] = 'Briefy Bot'
        payload_item['data'] = {
            'fields': [
                {'title': 'Fullname',
                 'value': data.get('fullname'),
                 'short': True,
                 },
                {'title': 'Username',
                 'value': data.get('email'),
                 'short': True,
                 },
                {'title': 'Groups',
                 'value': groups,
                 'short': True,
                 },
            ]
        }
        return payload


@adapter(user.IUserFirstLogin)
@implementer(ISlack)
class UserFirstLogin(UserSlack):
    """Post on slack on a user firstlogin."""

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        username = data.get('email')
        groups = ''
        if isinstance(data.get('groups'), list):
            groups = ', '.join([g['slug'] for g in data['groups']])
        payload_item = payload[0]
        payload_item['title'] = 'First User login'
        payload_item['text'] = f'The user {username} just logged in on Leica for the first time'
        payload_item['username'] = 'Briefy Bot'
        payload_item['data'] = {
            'fields': [
                {'title': 'Fullname',
                 'value': data.get('fullname'),
                 'short': True,
                 },
                {'title': 'Username',
                 'value': data.get('email'),
                 'short': True,
                 },
                {'title': 'Groups',
                 'value': groups,
                 'short': True,
                 },
            ]
        }
        return payload
