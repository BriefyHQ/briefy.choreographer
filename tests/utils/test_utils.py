"""Tests for `briefy.choreographer.utils` module."""
from briefy import choreographer
from briefy.choreographer.utils import get_event_actions
from briefy.choreographer.utils import get_events
from zope.configuration.xmlconfig import XMLConfig


XMLConfig('configure.zcml', choreographer)()


def test_get_event_actions():
    events = get_events()
    actions = get_event_actions(events)
    assert isinstance(actions, dict)


def test_get_events():
    events = get_events()
    assert isinstance(events, dict)
