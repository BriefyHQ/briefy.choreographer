"""Briefy base worker."""
from briefy.choreographer.config import NEW_RELIC_LICENSE_KEY
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from briefy.common.queue import IQueue
from briefy.common.queue import Queue
from briefy.common.queue.message import SQSMessage
from briefy.common.worker import QueueWorker
from uuid import uuid4
from zope.component import getUtility
from zope.component import queryUtility
from zope.event import notify

import logging
import newrelic.agent
import typing as t


logger = logging.getLogger('briefy.choreographer')


class Worker(QueueWorker):
    """Choreographer queue worker."""

    name = 'choreographer.worker'
    """Worker name."""

    input_queue = None
    """Queue to read event messages from."""

    run_interval = None
    """Interval to fetch new messages from the queue."""

    def __init__(
        self,
        input_queue: Queue,
        logger_: t.Optional[logging.Logger]=None,
        run_interval: float=.5,
        *args,
        **kw
    ):
        """Initialize the worker."""
        if logger_ is None:
            logger_ = logger
        super().__init__(input_queue, logger_, run_interval, *args, **kw)

    @newrelic.agent.background_task(name='process_message', group='Task')
    def process_message(self, message: SQSMessage) -> bool:
        """Process a message retrieved from the input_queue.

        :param message: A message from the queue
        :returns: Status from the process
        """
        body = message.body
        id_ = body.get('id', str(uuid4()))
        event_name = body['event_name']
        guid = body['guid']

        if not event_name or not guid:
            self.logger.info('Event without name or guid on queue')
            # This will delete the message
            return True

        # Always fallback to InternalEvent, meaning, at least, we will have it logged
        event_factory = queryUtility(IInternalEvent, event_name, default=InternalEvent)

        try:
            event = event_factory(
                id=id_,
                guid=guid,
                data=body['data'],
                actor=body['actor'],
                request_id=body['request_id'],
                created_at=body['created_at']
            )
        except Exception as exc:
            self.logger.exception(
                f'Error creating event for object with id {guid}: {exc}'
            )
            # This will delete the message
            return True

        if event.event_name == '':
            event.event_name = event_name

        notify(event)
        self.logger.debug(f'Event {event_name} notified')
        return True


def main():
    """Initialize and execute the Worker."""
    queue = getUtility(IQueue, 'events.queue')
    worker = Worker(input_queue=queue, logger_=logger)
    if NEW_RELIC_LICENSE_KEY:
        newrelic.agent.register_application(timeout=10.0)
    try:
        worker()
    except Exception as exc:
        logger.exception(f'{Worker.name} exiting due to an exception.')
        raise
