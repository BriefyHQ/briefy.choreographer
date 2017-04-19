"""Slack actions for Tasks in Leica."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.events.leica import task as events
from zope.component import adapter
from zope.interface import implementer


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

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        payload['title'] = self.title
        payload['username'] = 'Briefy Bot'
        payload['text'] = (
            'The order for this assignment does not have availability dates. '
            'Assignment can be seen <{url}|here>'.format(
                url=self._action_url,
            )
        )
        return payload


@adapter(events.IAssignmentPoolHasPoolId)
@implementer(ISlack)
class AssignmentPoolHasPoolId(TaskSlack):
    """Slack notification on Assignment to be moved to a Pool but already has a Pool ID."""

    entity = 'Assignment'
    title = 'Assigment to Pool Failed'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        payload['title'] = self.title
        payload['username'] = 'Briefy Bot'
        payload['text'] = (
            'This assignment already is on a Pool. '
            'Assignment can be seen <{url}|here>'.format(
                url=self._action_url,
            )
        )
        return payload


@adapter(events.IAssignmentPoolNoPayout)
@implementer(ISlack)
class AssignmentPoolNoPayout(TaskSlack):
    """Slack notification on Assignment to be moved to a Pool but there is no payout defined."""

    entity = 'Assignment'
    title = 'Assigment to Pool Failed'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        payload['title'] = self.title
        payload['username'] = 'Briefy Bot'
        payload['text'] = (
            'This assignment does not have a Payout value. '
            'Assignment can be seen <{url}|here>'.format(
                url=self._action_url,
            )
        )
        return payload
