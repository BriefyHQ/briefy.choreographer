"""Slack actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction


class ISlack(IAction):
    """Action that queue slack messages."""


class Slack(Action):
    """Action that queue slack messages."""

    weight = 100
    _queue_name = 'slack.queue'
    entity = ''
    channel = '#tests'
    color = 'good'
    icon = ':briefy:'

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
        }
        return payload
