"""Briefy email action for Lead events tests."""
from briefy.choreographer.actions import Action
from briefy.choreographer.actions import IAction
from briefy.choreographer.events import lead as events
from conftest import BaseActionCase

import pytest


class TestBaseAction(BaseActionCase):
    """Test for base action class."""

    action_class = Action
    action_interface = IAction
    event_class = events.LeadCreated
    data_file = 'lead.json'

    def test_interfaces(self):
        """Test that this action provides IAction interfaces."""
        pass

    def test_registration(self):
        """Test that this action is registered."""
        pass

    def test_call(self):
        """Test action execution."""
        pass

    def test_transform(self):
        """Test data transform."""
        obj = self.obj
        with pytest.raises(NotImplementedError):
            obj.transform()
