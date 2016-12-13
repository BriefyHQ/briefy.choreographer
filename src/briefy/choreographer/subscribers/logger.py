"""Logger handler."""
from briefy.choreographer.events import InternalEvent
import logging

logger = logging.getLogger(__name__)


def handler(event: InternalEvent):
    """Catch all handler that logs the event.

    :param event: Event
    """
    logger.info(
        'Event: {name}, Entity: {entity}, GUID: {guid}'.format(
            name=event.event_name,
            entity=event.entity,
            guid=event.guid
        ),
        extra={
            'choreographer': {
                'event_name': event.event_name,
                'guid': event.guid,
                'entity': event.entity,
                'actor': event.actor,
                'request_id': event.request_id,
                'data': event.data
            }
        }
    )
