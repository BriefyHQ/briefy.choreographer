"""Briefy Choreographer Subscribers."""
from briefy.choreographer.actions import Action
from briefy.choreographer.utils import get_actions_for_event
from zope.component import getGlobalSiteManager

import logging
import typing as t


_logger = logging.getLogger('briefy.choreographer')


class BaseHandler:
    """Base handler for Internal Events."""

    _info_class_ = None
    registry = None
    event = None
    info = None
    guid = None

    def __init__(self, event):
        """Initialize the Handler."""
        self.registry = getGlobalSiteManager()
        self.event = event
        self.guid = event.guid
        data = event.data
        data.update({'guid': self.guid})

    @property
    def actions(self) -> t.Sequence[Action]:
        """Return all actions for this event.

        :returns: Sequence of actions registered for this event.
        """
        return get_actions_for_event(self.event, self.registry)

    def __call__(self) -> None:
        """Execute all actions registered to this event."""
        actions = self.actions
        for action in actions:
            try:
                action()
            except Exception:
                info = action.action_info()
                _logger.exception(f'An error occurred executing {info}')
