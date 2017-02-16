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
    _channel = '#leica-assignments'
    title = 'Assignment'
    text = 'New Assignment!!'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = self.title
        payload['text'] = (
            'Assignment can be seen <{url}|here>'.format(
                url=self._action_url,
            )
        )
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


@adapter(events.IAssignmentCreated)
@implementer(ISlack)
class AssignmentCreated(AssignmentSlack):
    """Assignment created, post on Slack."""

    title = 'Assignment created!'


@adapter(events.IAssignmentUpdated)
@implementer(ISlack)
class AssignmentUpdated(AssignmentSlack):
    """Assignment created, post on Slack."""

    title = 'Assignment updated!'


@adapter(events.IAssignmentWfAssign)
@implementer(ISlack)
class AssignmentWfAssign(AssignmentSlack):
    """After assigning, post on Slack."""

    title = 'Assignment assigned!'


@adapter(events.IAssignmentWfCancel)
@implementer(ISlack)
class AssignmentWfCancel(AssignmentSlack):
    """After cancelling, post on Slack."""

    title = 'Assignment cancelled!'


@adapter(events.IAssignmentWfComplete)
@implementer(ISlack)
class AssignmentWfComplete(AssignmentSlack):
    """After completing, post on Slack."""

    title = 'Assignment completed!'


@adapter(events.IAssignmentWfRefuse)
@implementer(ISlack)
class AssignmentWfRefuse(AssignmentSlack):
    """After customer refusal, post on Slack."""

    title = 'Assignment refused!'


@adapter(events.IAssignmentWfSchedulingIssues)
@implementer(ISlack)
class AssignmentWfSchedulingIssues(AssignmentSlack):
    """After a report of scheduling issues, post on Slack."""

    title = 'Assignment with schedulling issues!'


@adapter(events.IAssignmentWfSelfAssign)
@implementer(ISlack)
class AssignmentWfSelfAssign(AssignmentSlack):
    """Post on Slack on self assignments."""

    title = 'Creative just self-assigned'


@adapter(events.IAssignmentWfUpload)
@implementer(ISlack)
class AssignmentWfUpload(AssignmentSlack):
    """Post on Slack on set uploads."""

    title = 'Set was uploaded'


@adapter(events.IAssignmentWfApprove)
@implementer(ISlack)
class AssignmentWfApprove(AssignmentSlack):
    """Post on Slack on set approves."""

    title = 'Set was approved'


@adapter(events.IAssignmentWfReject)
@implementer(ISlack)
class AssignmentWfReject(AssignmentSlack):
    """Post on Slack on set rejections."""

    title = 'Set was rejected'


@adapter(events.IAssignmentWfSchedule)
@implementer(ISlack)
class AssignmentWfSchedule(AssignmentSlack):
    """Post on Slack on schedule of an assignment."""

    title = 'Assignment was scheduled'


@adapter(events.IAssignmentWfReschedule)
@implementer(ISlack)
class AssignmentWfReschedule(AssignmentSlack):
    """Post on Slack on reschedule of an assignment."""

    title = 'Assignment was re-scheduled'
