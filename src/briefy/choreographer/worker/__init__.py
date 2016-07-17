"""Briefy base worker."""
from briefy.common.queue import IQueue
from briefy.common.worker.queue import QueueWorker
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
    sleep = None

    def process_message(self, message):
        """Process a message retrieved from the input_queue.

        :param message: A message from the queue
        :type message: briefy.common.queue.message.SQSMessage
        :returns: Response from the handler
        :rtype: dict
        """
        body = message.body
        event_name = body['event_name']
        guid = body['guid']
        if event_name and guid:
            event_factory = queryUtility(IInternalEvent, event_name, None)
            if event_factory:
                event = event_factory(
                    guid=guid,
                    data=body['data'],
                    actor=body['actor'],
                    request_id=body['request_id']
                )
                notify(event)
            else:
                logger.info('Event {} has no handler'.format(event_name))
        # Removing message
        message.delete()


def main():
    """Initialize and execute the Worker."""
    queue = getUtility(IQueue, 'event.queue')
    worker = Worker(input_queue=queue, logger_=logger)
    try:
        worker()
    except:
        logger.exception(
            '{} exiting due to an exception.'.format(Worker.name)
        )
