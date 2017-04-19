"""Briefy Mail Queue."""
from briefy.choreographer.config import MAIL_QUEUE
from briefy.common.queue import IQueue
from briefy.common.queue import Queue
from briefy.common.utils.schema import Dictionary
from briefy.common.utils.schema import List
from briefy.common.validators import EventName
from zope.interface import implementer

import colander
import logging


logger = logging.getLogger('briefy.choreographer')


class Schema(colander.MappingSchema):
    """Payload for the mail queue."""

    event_name = colander.SchemaNode(colander.String(), validator=EventName)
    """Event name."""

    entity = colander.SchemaNode(colander.String())
    """Entity name."""

    guid = colander.SchemaNode(colander.String(), validator=colander.uuid)
    """GUID for the event."""

    sender_name = colander.SchemaNode(colander.String(), missing='')
    """Name of the sender."""

    sender_email = colander.SchemaNode(colander.String(), missing='')
    """Email of the sender."""

    fullname = colander.SchemaNode(colander.String())
    """Fullname of the recipient."""

    email = colander.SchemaNode(colander.String())
    """Email of the recipient."""

    subject = colander.SchemaNode(colander.String(), missing='')
    """Subject of the email."""

    template = colander.SchemaNode(colander.String())
    """Template to be used."""

    data = colander.SchemaNode(Dictionary())
    """Payload -- for interpolation -- to be used on the email."""

    attachments = colander.SchemaNode(List(), missing=None)
    """Attachments to be sent with this mesage -- a list of urls."""


@implementer(IQueue)
class SQSQueue(Queue):
    """A Queue to handle messages to send emails."""

    name = MAIL_QUEUE
    _schema = Schema

    @property
    def payload(self) -> dict:
        """Return an example payload for this queue.

        :returns: Dictionary representing the payload for this queue
        """
        return {
            'event_name': '',
            'entity': '',
            'guid': '',
            'sender_name': '',
            'sender_email': '',
            'fullname': '',
            'email': '',
            'subject': '',
            'template': '',
            'data': {},
            'attachments': []
        }


MailQueue = SQSQueue()
