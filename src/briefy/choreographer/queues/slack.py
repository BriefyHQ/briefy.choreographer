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
    """Payload for the mail queue."""

    event_name = colander.SchemaNode(colander.String(), validator=EventName)
    entity = colander.SchemaNode(colander.String())
    guid = colander.SchemaNode(colander.String(), validator=colander.uuid)
    channel = colander.SchemaNode(colander.String(), missing='')
    title = colander.SchemaNode(colander.String(), missing='')
    text = colander.SchemaNode(colander.String())
    color = colander.SchemaNode(colander.String())
    icon = colander.SchemaNode(colander.String(), missing='')
    username = colander.SchemaNode(colander.String())
    data = colander.SchemaNode(Dictionary())


@implementer(IQueue)
class Queue(BaseQueue):
    """A Queue to handle messages to slack."""

    name = SLACK_QUEUE
    _schema = Schema

    @property
    def payload(self):
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
