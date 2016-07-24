"""Briefy Notification Queue."""
from briefy.choreographer.config import NOTIFICATION_QUEUE
from briefy.common.queue import IQueue
from briefy.common.queue import Queue as BaseQueue
from briefy.common.validators import EventName
from zope.interface import implementer

import colander
import logging

logger = logging.getLogger('briefy.choreographer')


class Schema(colander.MappingSchema):
    """Payload for the notification queue."""

    id = colander.SchemaNode(colander.String(), validator=colander.uuid)
    type = colander.SchemaNode(colander.String())
    event_name = colander.SchemaNode(colander.String(), validator=EventName)
    entity = colander.SchemaNode(colander.String())
    guid = colander.SchemaNode(colander.String(), validator=colander.uuid)
    fullname = colander.SchemaNode(colander.String())
    subject = colander.SchemaNode(colander.String(), missing='')
    address = colander.SchemaNode(colander.String(), missing='')
    gateway = colander.SchemaNode(colander.String(), missing='')
    gateway_id = colander.SchemaNode(colander.String(), missing='')
    status = colander.SchemaNode(colander.String(), missing='')
    additional_info = colander.SchemaNode(colander.String(), missing='')


@implementer(IQueue)
class Queue(BaseQueue):
    """A Queue to handle messages to send emails."""

    name = NOTIFICATION_QUEUE
    _schema = Schema

    @property
    def payload(self):
        """Return an example payload for this queue.

        :returns: Dictionary representing the payload for this queue
        :rtype: dict
        """
        return {
            'id': '',
            'type': '',
            'event_name': '',
            'entity': '',
            'guid': '',
            'fullname': '',
            'subject': '',
            'address': '',
            'gateway': '',
            'gateway_id': '',
            'status': '',
            'additional_info': '',
        }

NotificationQueue = Queue()
