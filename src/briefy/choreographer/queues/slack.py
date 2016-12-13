"""Briefy Mail Queue."""
from briefy.choreographer.config import SLACK_QUEUE
from briefy.common.queue import IQueue
from briefy.common.queue import Queue as BaseQueue
from briefy.common.utils.schema import Dictionary
from briefy.common.validators import EventName
from zope.interface import implementer

import colander
import logging

logger = logging.getLogger('briefy.choreographer')


class Schema(colander.MappingSchema):
    """Payload for the Slack queue."""

    event_name = colander.SchemaNode(colander.String(), validator=EventName)
    """Event name."""

    entity = colander.SchemaNode(colander.String())
    """Entity name."""

    guid = colander.SchemaNode(colander.String(), validator=colander.uuid)
    """GUID for the event."""

    channel = colander.SchemaNode(colander.String(), missing='')
    """Channel that will receive the message."""

    title = colander.SchemaNode(colander.String(), missing='')
    """Title of the message attachment."""

    text = colander.SchemaNode(colander.String())
    """Text of the message."""

    color = colander.SchemaNode(colander.String())
    """Color of the message attachment."""

    icon = colander.SchemaNode(colander.String(), missing='')
    """Icon of the integration.

    The icon that will appear when the integration posts a message on Slack.
    """

    username = colander.SchemaNode(colander.String())
    """Username of the integration.

    The name that will appear when the integration posts a message on Slack.
    """

    data = colander.SchemaNode(Dictionary())
    """Payload to be sent with the slack message."""


@implementer(IQueue)
class Queue(BaseQueue):
    """A Queue to handle messages to Slack."""

    name = SLACK_QUEUE
    _schema = Schema

    @property
    def payload(self) -> dict:
        """Return an example payload for this queue.

        :returns: Dictionary representing the payload for this queue
        :rtype: dict
        """
        return {
            'event_name': '',
            'entity': '',
            'guid': '',
            'channel': '',
            'title': '',
            'text': '',
            'color': '',
            'icon': '',
            'username': '',
            'data': {},
        }


SlackQueue = Queue()
