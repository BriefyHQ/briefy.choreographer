"""Logger handler."""
from briefy.choreographer.events import InternalEvent
from briefy.choreographer.utils import get_actions_for_event
from briefy.common.utils.transformers import json_dumps

import logging


logger = logging.getLogger(__name__)


def handler(event: InternalEvent) -> None:
    """Catch all handler that logs the event.

    :param event: InternalEvent instance
    """
    actions = get_actions_for_event(event)
    actions_info = [cls.action_info() for cls in actions]
    total_actions = len(actions)
    logger.info(
        f'Event {event.event_name} ({event.guid}) with {total_actions:02d} actions',
        extra={
            'choreographer': {
                'event_name': event.event_name,
                'guid': event.guid,
                'id': event.id,
                'entity': event.entity,
                'actor': event.actor,
                'request_id': event.request_id,
                'data_payload': json_dumps(event.data),
                'total_actions': total_actions,
                'registered_actions': actions_info
            }
        }
    )
