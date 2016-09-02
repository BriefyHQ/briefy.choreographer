"""Slack actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction
from briefy.choreographer.config import is_production


class ISlack(IAction):
    """Action that queue slack messages."""


class Slack(Action):
    """Action that queue slack messages."""

    weight = 100
    _queue_name = 'slack.queue'
    entity = ''
    _channel = '#tests'
    color = 'good'
    icon = ':briefy:'

    @property
    def channel(self):
        if is_production():
            return self._channel
        else:
            return '#tests'

    @property
    def available(self):
        """Check if this action is available."""
        return True

    def transform(self):
        """Transform data."""
        event = self.event
        payload = {
            'channel': self.channel,
            'title': '',
            'text': '',
            'color': self.color,
            'icon': self.icon,
            'username': '',
            'entity': self.entity,
            'guid': event.guid,
            'event_name': event.event_name,
            'data': {}
        }
        return payload
