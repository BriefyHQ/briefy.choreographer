"""Tests for `briefy.choreographer.utils` module."""
from briefy import choreographer
from briefy.choreographer.events import InternalEvent
from briefy.choreographer.events.leica.order import order as order_events
from briefy.choreographer.utils import get_actions_for_event
from briefy.choreographer.utils import get_event_actions
from briefy.choreographer.utils import get_events
from zope.configuration.xmlconfig import XMLConfig

import pytest


XMLConfig('configure.zcml', choreographer)()


def test_get_event_actions():
    events = get_events()
    actions = get_event_actions(events)
    assert isinstance(actions, dict)


def test_get_events():
    events = get_events()
    assert isinstance(events, dict)


test_data = [
    (InternalEvent, 0),
    (order_events.OrderCreated, 1),
    (order_events.OrderUpdated, 0),
    (order_events.OrderWfSubmit, 2),
]


@pytest.mark.parametrize('event_factory,total_actions', test_data)
def test_get_actions_for_event_with_generic_event(event_factory, total_actions):
    from briefy.common.db import datetime_utcnow
    event = event_factory(
        id='91125bb8-dde8-426a-91a6-70760b8fb6fc',
        guid='e5baeeda-8e99-4097-914d-f7be391c3904',
        data={},
        actor='c5237fbf-73b3-4363-9045-dabe418bc75e',
        request_id='',
        created_at=datetime_utcnow()
    )
    actions = get_actions_for_event(event)
    assert isinstance(actions, list)
    assert len(actions) == total_actions
