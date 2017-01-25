"""Slack actions for Assignments."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events.leica import assignment as events
from zope.component import adapter
from zope.interface import implementer


class AssignmentSlack(Slack):
    """Base class for Slack message sent on Assignment events."""

    entity = 'Assignment'
    weight = 100
    _channel = '#tests'
    title = 'Assignment'
    text = 'New Assignment!!'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = self.title
        payload['text'] = self.text
        payload['username'] = 'Briefy Bot'
        payload['data'] = {
            'fields': [
                {'title': 'Customer',
                 'value': data.get('customer', {}).get('title'),
                 'short': True,
                 },
                {'title': 'Project',
                 'value': data.get('project', {}).get('title'),
                 'short': True,
                 },
                {'title': 'Creative',
                 'value': data.get('professional', {}).get('title'),
                 'short': True,
                 },
            ]
        }
        return payload


@adapter(events.IAssignmentWfAssign)
@implementer(ISlack)
class AssignmentWfAssign(AssignmentSlack):
    """After assigning, post on Slack."""

    title = 'Assignment assigned!'
    text = 'Assignment was assigned to a creative'


@adapter(events.IAssignmentWfSelfAssign)
@implementer(ISlack)
class AssignmentWfSelfAssign(AssignmentSlack):
    """Post on Slack on self assignments."""

    title = 'Creative just self-assigned'
    text = 'New self-assign'


@adapter(events.IAssignmentWfApprove)
@implementer(ISlack)
class AssignmentWfApprove(AssignmentSlack):
    """Post on Slack on set approves."""

    title = 'Set was approved'
    text = 'A set was approved by our QA team'


@adapter(events.IAssignmentWfSchedule)
@implementer(ISlack)
class AssignmentWfSchedule(AssignmentSlack):
    """Post on Slack on schedule of an assignment."""

    title = 'Assignment was scheduled'
    text = 'Assignment was scheduled.'


@adapter(events.IAssignmentWfReschedule)
@implementer(ISlack)
class AssignmentWfReschedule(AssignmentSlack):
    """Post on Slack on reschedule of an assignment."""

    title = 'Assignment was re-scheduled'
    text = 'Assignment was re-scheduled.'
