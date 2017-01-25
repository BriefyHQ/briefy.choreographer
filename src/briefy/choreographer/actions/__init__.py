"""Module that implements possible actions."""
from briefy.choreographer.config import PLATFORM_URL
from briefy.choreographer.events import InternalEvent
from briefy.common.queue import IQueue
from briefy.common.queue import Queue
from zope.component import getUtility
from zope.interface import Attribute
from zope.interface import Interface

import dateutil.parser
import logging

logger = logging.getLogger('briefy.choreographer')


class IAction(Interface):
    """An action."""

    weight = Attribute("""Weight of the action. Lower will be processed first""")
    entity = Attribute("""Name of the entity to be processed here""")

    def transform():
        """Execute the action."""

    def __call__():
        """Execute the action."""


class Action:
    """An action."""

    weight = 100
    """Weight of the action.

    A lower number takes precedence over a higher number.
    """
    _queue_name = ''
    """Name of the queue to be used."""

    _queue = None
    """Queue to be used."""

    entity = ''
    """Name of the entity to be processed here."""

    def __init__(self, event: InternalEvent):
        """Initialize the Action."""
        self.data = event.data
        self.event = event

    @property
    def _action_url(self) -> str:
        """Return the action URL for the object."""
        data = self.data
        entity = self.entity
        if 'id' in data and entity:
            return '{base}{entity}s/{id}'.format(
                base=PLATFORM_URL,
                entity=entity.lower(),
                id=data['id']
            )

    def _format_date(self, value: str) -> str:
        """Format a date."""
        response = ''
        if value:
            value = dateutil.parser.parse(value)
            response = '{0:%d-%m-%Y}'.format(value)
        return response

    def _format_datetime(self, value: str) -> str:
        """Format a datetime."""
        response = ''
        if value:
            value = dateutil.parser.parse(value)
            response = '{0:%d-%m-%Y %H:%M}'.format(value)
        return response

    @property
    def available(self) -> bool:
        """Check if this action is available."""
        return True

    @property
    def queue(self) -> Queue:
        """Retrieve the queue to be used on this action."""
        queue = self._queue
        if not queue and self._queue_name:
            queue = getUtility(IQueue, self._queue_name)
            self._queue = queue
        return queue

    def transform(self):
        """Transform data."""
        raise NotImplementedError()

    def log(self, payload: dict, response: str) -> None:
        """Log results from this action."""
        event = self.event
        logger.info(
            '{event}: {queue} action {action} with response {response}'.format(
                event=event.event_name if event else '',
                queue=self._queue_name if self._queue_name else '',
                action=self.__class__.__name__,
                response=response
            ),
            extra={
                'action': {
                    'guid': event.guid,
                    'actor': event.actor,
                    'request_id': event.request_id,
                    'entity': self.entity,
                    'event_name': event.event_name,
                    'payload': payload
                }
            }
        )

    def __call__(self) -> None:
        """Execute the action."""
        event = self.event
        logger.info(
            '{event}: action {action}'.format(
                event=event.event_name if event else '',
                action=self.__class__.__name__,
            )
        )
        if self.available:
            payload = self.transform()
            queue = self.queue
            if not queue:
                raise ValueError('Queue not available')
            response = queue.write_message(payload)
            self.log(payload, response)

    def __repr__(self) -> str:
        """Representation of the Action object."""
        return (
            """<{0}(weight='{1}')>""").format(
                self.__class__.__name__,
                self.weight,
        )
