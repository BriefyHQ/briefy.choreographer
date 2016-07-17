"""Briefy Choreographer Subscribers."""
from briefy.choreographer.actions import IAction
from zope.component import getGlobalSiteManager

import logging
import operator

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
        if self._info_class_:
            data = event.data
            data.update({'guid': self.guid})
            self.info = self._info_class_(**data)

    @property
    def actions(self):
        """Return all actions for this event."""
        registry = self.registry
        action_adapters = registry.getAdapters((self.info, self.event), IAction)
        actions = [action for name, action in action_adapters]
        actions.sort(key=operator.attrgetter('weight'))
        return actions

    def __call__(self):
        """Handle events."""
        actions = self.actions
        for action in actions:
            try:
                action()
            except Exception:
                _logger.exception(
                    'An error occurred executing {}'.format(
                        action.__class__.__name__
                    )
                )
