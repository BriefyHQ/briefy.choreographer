"""Ms Laure Queue."""
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
    """Payload for the Ms. Laure queue."""

    event_name = colander.SchemaNode(colander.String(), validator=EventName)
    """Event name."""

    created_at = colander.SchemaNode(colander.String())
    """Created at."""

    guid = colander.SchemaNode(colander.String(), validator=colander.uuid)
    """GUID for the event."""

    data = colander.SchemaNode(Dictionary())
    """Payload to be sent with the slack message."""


@implementer(IQueue)
class Queue(BaseQueue):
    """A Queue to handle messages to Ms. Laure."""

    name = SLACK_QUEUE
    _schema = Schema

    @property
    def payload(self) -> dict:
        """Return an example payload for this queue.

        :returns: Dictionary representing the payload for this queue
        """
        return {
            'event_name': '',
            'guid': '',
            'created_at': '',
            'data': {},
        }


LaureQueue = Queue()
