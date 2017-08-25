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
import pytz
import typing as t


logger = logging.getLogger('briefy.choreographer')


class IAction(Interface):
    """An action."""

    category = Attribute("""Category of this action. i.e.: notification, service_message""")
    weight = Attribute("""Weight of the action. Lower will be processed first""")
    entity = Attribute("""Name of the entity to be processed here""")

    def transform():
        """Execute the action."""

    def __call__():
        """Execute the action."""


class Action:
    """An action."""

    category = ''
    """Category of this action.

    Should be one of:

        * notification
        * service_message

    """

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
        url = ''
        data = self.data
        entity = self.entity
        id_ = data.get('id', data.get('guid', None))
        if id_ and entity:
            entity_name = entity.lower()
            url = f'{PLATFORM_URL}{entity_name}s/{id_}'
        return url

    def _format_date(self, value: str, timezone: str = '') -> str:
        """Format a date."""
        response = ''
        if value:
            value = dateutil.parser.parse(value)
            if timezone:
                tz_info = pytz.timezone(timezone)
                value = value.astimezone(tz_info)
            response = f'{value:%d-%m-%Y}'
        return response

    def _format_datetime(self, value: str,  timezone: str = '') -> str:
        """Format a datetime."""
        response = ''
        if value:
            value = dateutil.parser.parse(value)
            if timezone:
                tz_info = pytz.timezone(timezone)
                value = value.astimezone(tz_info)
            response = f'{value:%d-%m-%Y %H:%M}'
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

    def transform(self) -> t.List[dict]:
        """Transform data."""
        raise NotImplementedError()

    def _get_log_extra(self, payload: t.List[dict]) -> dict:
        """Return extra information to be passed to log."""
        event = self.event
        extra = {
            'action': {
                'guid': event.guid,
                'actor': event.actor,
                'request_id': event.request_id,
                'entity': self.entity,
                'event_name': event.event_name,
                'payload': payload
            }
        }
        return extra

    def __call__(self) -> None:
        """Execute the action."""
        queue = self.queue
        if not queue:
            raise ValueError('Queue not available')
        if self.available:
            response = 'No Payload'
            payload = self.transform()
            log_extra = self._get_log_extra(payload=payload)
            event_name = self.event.event_name if self.event else ''
            queue_name = self._queue_name if self._queue_name else ''
            action = self.__class__.__name__
            if payload:
                try:
                    response = queue.write_messages(payload)
                except Exception as exc:
                    logger.error(
                        f'{event_name}: {queue_name} action {action} with response',
                        extra=log_extra
                    )
                    return None
            logger.info(
                f'{event_name}: {queue_name} action {action} with response {response}',
                extra=log_extra
            )

    @classmethod
    def action_info(cls) -> str:
        """Action information.

        A friendly display of this action.
        :return: A string representing this action.
        """
        name = cls.__name__
        category = cls.category
        entity = cls.entity
        weight = cls.weight
        queue = cls._queue_name
        return f'{category} - {queue} - {weight} - {entity} - {name}'

    def __repr__(self) -> str:
        """Representation of the Action object."""
        klass_name = self.__class__.__name__
        return f'<{klass_name} (weight={self.weight}, category="{self.category}")>'
