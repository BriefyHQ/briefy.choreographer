"""Slack actions."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction
from briefy.choreographer.config import is_production


class ISlack(IAction):
    """Action that queue slack messages."""


class Slack(Action):
    """Action that queue messages to be sent with Slack."""

    weight = 100
    _queue_name = 'slack.queue'
    entity = ''
    _channel = '#tests'
    """Channel to receive the message."""

    color = 'good'
    """Color of the attachment."""

    icon = ':briefy:'
    """Icon to be used on the message."""

    @property
    def channel(self) -> str:
        """Return the channel to be receive this message.

        If we are in not in production, send to #tests.
        """
        if is_production():
            return self._channel
        else:
            return '#tests'

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        return True

    def transform(self) -> dict:
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
