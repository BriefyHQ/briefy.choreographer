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
        data = self.data
        payload = {
            'id': event.guid,
            'type': self.entity,
            'channel': self.channel,
            'title': '',
            'text': '',
            'color': self.color,
            'icon': self.icon,
            'username': '',
            'guid': data.guid,
            'event_name': data.event_name,
        }
        return payload
