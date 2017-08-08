"""Logger handler."""
from briefy.choreographer.events import InternalEvent
from briefy.common.utils.transformers import json_dumps

import logging


logger = logging.getLogger(__name__)


def handler(event: InternalEvent) -> None:
    """Catch all handler that logs the event.

    :param event: Event
    """
    message = f'Event: {event.event_name}, Entity: {event.entity}, GUID: {event.guid}'
    logger.info(
        message,
        extra={
            'choreographer': {
                'event_name': event.event_name,
                'guid': event.guid,
                'id': event.id,
                'entity': event.entity,
                'actor': event.actor,
                'request_id': event.request_id,
                'data_payload': json_dumps(event.data)
            }
        }
    )
