"""Briefy base worker."""
from briefy.common.queue import IQueue
from briefy.common.queue.message import SQSMessage
from briefy.common.worker import QueueWorker
from briefy.choreographer.config import NEW_RELIC_LICENSE_KEY
from briefy.choreographer.events import IInternalEvent
from zope.component import getUtility
from zope.component import queryUtility
from zope.event import notify

import logging
import newrelic.agent


logger = logging.getLogger('briefy.choreographer')


class Worker(QueueWorker):
    """Choreographer queue worker."""

    name = 'choreographer.worker'
    """Worker name."""

    input_queue = None
    """Queue to read event messages from."""

    run_interval = None
    """Interval to fetch new messages from the queue."""

    def __init__(self, input_queue, logger_=None, run_interval=.5, *args, **kw):
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
        event_name = body['event_name']
        guid = body['guid']

        if not event_name or not guid:
            self.logger.info('Event without name or guid on queue')
            return False
        event_factory = queryUtility(IInternalEvent, event_name, None)
        if not event_factory:
            self.logger.info('Event {} has no handler'.format(event_name))
            return False

        event = event_factory(
            guid=guid,
            data=body['data'],
            actor=body['actor'],
            request_id=body['request_id'],
            created_at=body['created_at']
        )
        notify(event)
        self.logger.debug('Event {} notified'.format(event_name))
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
        logger.exception('{name} exiting due to an exception.'.format(name=Worker.name))
        raise
