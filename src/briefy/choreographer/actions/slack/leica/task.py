"""Slack actions for Tasks in Leica."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.events.leica import task as events
from zope.component import adapter
from zope.interface import implementer

import typing as t


class TaskSlack(Slack):
    """Base class for Slack message sent on Task events."""

    weight = 100
    _channel = '#leica-internal'


@adapter(events.IAssignmentPoolNoAvailability)
@implementer(ISlack)
class AssignmentPoolNoAvailability(TaskSlack):
    """Slack notification on Assignment to be moved to a Pool without availability dates."""

    entity = 'Assignment'
    title = 'Assigment to Pool Failed'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['title'] = self.title
        payload_item['username'] = 'Briefy Bot'
        payload_item['text'] = (
            f'The order for this assignment does not have availability dates. '
            f'Assignment can be seen <{self._action_url}|here>'
        )
        return payload


@adapter(events.IAssignmentPoolHasPoolId)
@implementer(ISlack)
class AssignmentPoolHasPoolId(TaskSlack):
    """Slack notification on Assignment to be moved to a Pool but already has a Pool ID."""

    entity = 'Assignment'
    title = 'Assigment to Pool Failed'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['title'] = self.title
        payload_item['username'] = 'Briefy Bot'
        payload_item['text'] = (
            f'This assignment already is on a Pool. '
            f'Assignment can be seen <{self._action_url}|here>'
        )
        return payload


@adapter(events.IAssignmentPoolNoPayout)
@implementer(ISlack)
class AssignmentPoolNoPayout(TaskSlack):
    """Slack notification on Assignment to be moved to a Pool but there is no payout defined."""

    entity = 'Assignment'
    title = 'Assigment to Pool Failed'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['title'] = self.title
        payload_item['username'] = 'Briefy Bot'
        payload_item['text'] = (
            f'This assignment does not have a Payout value. '
            f'Assignment can be seen <{self._action_url}|here>'
        )
        return payload


@adapter(events.IAssignmentNotifyLateSubmissionFailure)
@implementer(ISlack)
class AssignmentNotifyLateSubmissionFailure(TaskSlack):
    """Slack notification for a failure when tried to notify about late submission."""

    entity = 'Assignment'
    title = 'Late Submission Notification Failure'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['title'] = self.title
        payload_item['username'] = 'Briefy Bot'
        payload_item['text'] = (
            f'Failure when tried to notify professional about late submission. '
            f'Assignment can be seen <{self._action_url}|here>'
        )
        return payload


@adapter(events.IAssignmentNotifyBeforeShootingFailure)
@implementer(ISlack)
class AssignmentNotifyBeforeShootingFailure(TaskSlack):
    """Slack notification for a failure when tried to notify about late submission."""

    entity = 'Assignment'
    title = 'Before Shooting Notification Failure'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['title'] = self.title
        payload_item['username'] = 'Briefy Bot'
        payload_item['text'] = (
            f'Failure when tried to notify professional before shooting. '
            f'Assignment can be seen <{self._action_url}|here>'
        )
        return payload
