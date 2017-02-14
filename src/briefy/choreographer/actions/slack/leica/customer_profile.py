"""Slack actions for CustomerUserProfiles."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events.leica.profiles import customer_profile as events
from zope.component import adapter
from zope.interface import implementer


class CustomerUserProfileSlack(Slack):
    """Base class for Slack message sent on CustomerUserProfile events."""

    entity = 'CustomerUserProfile'
    weight = 100
    _channel = '#leica-customers'
    title = 'CustomerUserProfile'
    text = 'New Customer User Profile!!'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = self.title
        payload['text'] = self.text
        payload['username'] = 'Briefy Bot'
        payload['data'] = {
            'fields': [
                {
                    'title': 'Fullname',
                    'value': data['title'],
                    'short': True,
                },
                {
                    'title': 'Email',
                    'value': data['email'],
                    'short': True,
                 },
                {
                    'title': 'Phone',
                    'value': data['mobile'],
                    'short': True,
                 },
                {
                    'title': 'State',
                    'value': data['state'],
                    'short': True,
                },
            ]
        }
        return payload


@adapter(events.ICustomerUserProfileCreated)
@implementer(ISlack)
class CustomerUserProfileCreated(CustomerUserProfileSlack):
    """After creating a new CustomerUserProfile, post on Slack."""

    title = 'New Customer User!'
    text = 'New customer user was created:'


@adapter(events.ICustomerUserProfileUpdated)
@implementer(ISlack)
class CustomerUserProfileUpdated(CustomerUserProfileSlack):
    """After updated a new CustomerUserProfile, post on Slack."""

    title = 'Customer user info was updated'
    text = 'Customer user info was updated'


@adapter(events.ICustomerUserProfileWfActivate)
@implementer(ISlack)
class CustomerUserProfileWfActivate(CustomerUserProfileSlack):
    """After activating a new CustomerUserProfile, post on Slack."""

    title = 'Customer user was activated'
    text = 'Customer user was activated'


@adapter(events.ICustomerUserProfileWfInactivate)
@implementer(ISlack)
class CustomerUserProfileWfInactivate(CustomerUserProfileSlack):
    """After activating a new CustomerUserProfile, post on Slack."""

    title = 'Customer user was inactivated'
    text = 'Customer user was inactivated'
