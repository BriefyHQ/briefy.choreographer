"""Module that implements possible actions."""
from briefy.common.queue import IQueue
from zope.component import getUtility
from zope.interface import Attribute
from zope.interface import Interface

import logging

logger = logging.getLogger('briefy.choreographer')


class IAction(Interface):
    """An action."""

    weight = Attribute("""Weight of the action. Lower will be processed first""")

    def transform():
        """Execute the action."""

    def __call__():
        """Execute the action."""


class Action:
    """An action."""

    weight = 100
    _queue_name = ''
    _queue = None

    def __init__(self, event):
        """Initialize the Action."""
        self.data = event.data
        self.event = event

    @property
    def available(self):
        """Check if this action is available."""
        return True

    @property
    def queue(self):
        """Retrieve the queue to be used."""
        queue = self._queue
        if not queue and self._queue_name:
            queue = getUtility(IQueue, self._queue_name)
            self._queue = queue
        return queue

    def transform(self):
        """Transform data."""
        raise NotImplementedError()

    def log(self, payload, response):
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
                'guid': event.guid,
                'actor': event.actor,
                'request_id': event.request_id,
                'entity': self.entity,
                'event_name': event.event_name,
                'payload': payload
            }
        )

    def __call__(self):
        """Execute the action."""
        if self.available:
            payload = self.transform()
            queue = self.queue
            if not queue:
                raise ValueError('Queue not available')
            response = queue.write_message(payload)
            self.log(payload, response)

    def __repr__(self):
        """Representation of an Action."""
        return (
            """<{0}(weight='{1}')>""").format(
                self.__class__.__name__,
                self.weight,
        )
