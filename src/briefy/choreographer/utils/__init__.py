"""Utils used by other modules in briefy.choreographer."""
from briefy.choreographer.actions import IAction
from briefy.choreographer.events import IInternalEvent
from zope.component import getGlobalSiteManager


_DUMMY_EVENT_PAYLOAD = {
    'id': '9b76dfba-fdd7-4773-9f2b-645c2d1e2ca6',
    'guid': 'fe1341e2-e669-4a54-a1b2-c27a01d0a2ef',
    'actor': 'f042bf65-16aa-42d6-be31-ec39af539a22',
    'request_id': '5beef1a5-be04-4c95-81db-e79b10ef054d',
    'data': {},
    'created_at': '2017-03-29T14:30:30+00:00'
}


def get_events() -> dict:
    """Return a dict with event names and actions registered."""
    registry = getGlobalSiteManager()
    registered_events = registry.getUtilitiesFor(IInternalEvent)
    return dict(registered_events)


def get_event_actions(events: dict) -> dict:
    """Return a dict with event names and actions registered."""
    registry = getGlobalSiteManager()
    event_actions = {}

    for event_name, klass in events.items():
        event = klass(**_DUMMY_EVENT_PAYLOAD)
        adapters = registry.getAdapters((event, ), IAction)
        actions = dict([(name, action) for name, action in adapters])
        event_actions[event_name] = actions
    return event_actions
