"""Slack actions for Ms. Laure."""
from briefy.choreographer.actions.slack import Slack


class LaureSlack(Slack):
    """Base class for Slack message sent on Ms. Laure events."""

    entity = 'Ms.Laure'
    weight = 100
    _channel = '#ms_laure'
