"""Slack actions for BriefyUserProfiles."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events.leica.profiles import briefy_profile as events
from zope.component import adapter
from zope.interface import implementer


class BriefyUserProfileSlack(Slack):
    """Base class for Slack message sent on BriefyUserProfile events."""

    entity = 'BriefyUserProfile'
    weight = 100
    _channel = '#leica-internal'
    title = 'BriefyUserProfile'
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


@adapter(events.IBriefyUserProfileCreated)
@implementer(ISlack)
class BriefyUserProfileCreated(BriefyUserProfileSlack):
    """After creating a new BriefyUserProfile, post on Slack."""

    title = 'New Customer User!'
    text = 'New customer user was created:'


@adapter(events.IBriefyUserProfileUpdated)
@implementer(ISlack)
class BriefyUserProfileUpdated(BriefyUserProfileSlack):
    """After updated a new BriefyUserProfile, post on Slack."""

    title = 'Briefy user info was updated'
    text = 'Briefy user info was updated'


@adapter(events.IBriefyUserProfileWfActivate)
@implementer(ISlack)
class BriefyUserProfileWfActivate(BriefyUserProfileSlack):
    """After activating a new BriefyUserProfile, post on Slack."""

    title = 'Briefy user was activated'
    text = 'Briefy user was activated'


@adapter(events.IBriefyUserProfileWfInactivate)
@implementer(ISlack)
class BriefyUserProfileWfInactivate(BriefyUserProfileSlack):
    """After activating a new BriefyUserProfile, post on Slack."""

    title = 'Briefy user was inactivated'
    text = 'Briefy user was inactivated'
