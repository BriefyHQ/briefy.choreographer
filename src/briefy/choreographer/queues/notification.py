"""Briefy Notification Queue."""
from briefy.choreographer.config import NOTIFICATION_QUEUE
from briefy.common.queue import IQueue
from briefy.common.queue import Queue
from briefy.common.validators import EventName
from zope.interface import implementer

import colander
import logging


logger = logging.getLogger('briefy.choreographer')


class Schema(colander.MappingSchema):
    """Payload for the notification queue."""

    id = colander.SchemaNode(colander.String(), validator=colander.uuid)
    """ID of notification."""

    type = colander.SchemaNode(colander.String())
    """Type of notification."""

    event_name = colander.SchemaNode(colander.String(), validator=EventName)
    """Event name."""

    entity = colander.SchemaNode(colander.String())
    """Entity name."""

    guid = colander.SchemaNode(colander.String(), validator=colander.uuid)
    """Event GUID."""

    fullname = colander.SchemaNode(colander.String())
    """Fullname of recipient."""

    subject = colander.SchemaNode(colander.String(), missing='')
    """Subject of notification."""

    address = colander.SchemaNode(colander.String(), missing='')
    """Address of recipient."""

    gateway = colander.SchemaNode(colander.String(), missing='')
    """Gateway used."""

    gateway_id = colander.SchemaNode(colander.String(), missing='')
    """Gateway notification ID."""

    status = colander.SchemaNode(colander.String(), missing='')
    """Notification status."""

    additional_info = colander.SchemaNode(colander.String(), missing='')
    """Additional information."""


@implementer(IQueue)
class SQSQueue(Queue):
    """A Queue to handle messages to send emails."""

    name = NOTIFICATION_QUEUE
    _schema = Schema

    @property
    def payload(self) -> dict:
        """Return an example payload for this queue.

        :returns: Dictionary representing the payload for this queue
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


NotificationQueue = SQSQueue()
