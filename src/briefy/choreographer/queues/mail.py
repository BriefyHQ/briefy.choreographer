"""Briefy Mail Queue."""
from briefy.choreographer.config import MAIL_QUEUE
from briefy.common.queue import IQueue
from briefy.common.queue import Queue as BaseQueue
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
    entity = colander.SchemaNode(colander.String())
    guid = colander.SchemaNode(colander.String(), validator=colander.uuid)
    fullname = colander.SchemaNode(colander.String())
    email = colander.SchemaNode(colander.String())
    subject = colander.SchemaNode(colander.String(), missing='')
    template = colander.SchemaNode(colander.String())
    data = colander.SchemaNode(Dictionary())
    attachments = colander.SchemaNode(List(), missing=None)


@implementer(IQueue)
class Queue(BaseQueue):
    """A Queue to handle messages to send emails."""

    name = MAIL_QUEUE
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
            'fullname': '',
            'email': '',
            'subject': '',
            'template': '',
            'data': {},
            'attachments': []
        }

MailQueue = Queue()
