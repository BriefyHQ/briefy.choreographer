"""Briefy base worker."""
from briefy.common.queue import IQueue
from briefy.common.worker import QueueWorker
from briefy.choreographer.events import IInternalEvent
from zope.component import getUtility
from zope.component import queryUtility
from zope.event import notify

import logging

logger = logging.getLogger('briefy.choreographer')


class Worker(QueueWorker):
    """Choreographer queue worker."""

    name = 'choreographer.worker'
    input_queue = None
    run_interval = None

    def process_message(self, message):
        """Process a message retrieved from the input_queue.

        :param message: A message from the queue
        :type message: briefy.common.queue.message.SQSMessage
        :returns: Status from the process
        :rtype: bool
        """
        status = True
        body = message.body
        event_name = body['event_name']
        guid = body['guid']

        if not event_name or not guid:
            return True
        event_factory = queryUtility(IInternalEvent, event_name, None)
        if not event_factory:
            logger.info('Event {} has no handler'.format(event_name))
            return False

        event = event_factory(
            guid=guid,
            data=body['data'],
            actor=body['actor'],
            request_id=body['request_id'],
            created_at=body['created_at']
        )
        notify(event)

        return True


def main():
    """Initialize and execute the Worker."""
    queue = getUtility(IQueue, 'events.queue')
    worker = Worker(input_queue=queue, logger_=logger)
    try:
        worker()
    except Exception as exc:
        logger.exception('{} exiting due to an exception.'.format(Worker.name))
        raise
