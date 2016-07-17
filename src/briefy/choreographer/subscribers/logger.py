"""Logger handler."""
import logging

logger = logging.getLogger(__name__)


def handler(event):
    """Catch all handler that logs the event.

    :param event: Event
    :type event: briefy.choreographer.events.IInternalEvent
    """
    logger.info(
        'Event: {}, Entity: {}, GUID: {}'.format(event.event_name, event.entity, event.guid),
        extra={
            'event_name': event.event_name,
            'guid': event.guid,
            'entity': event.entity,
            'actor': event.actor,
            'request_id': event.request_id,
            'data': event.data
        }
    )
