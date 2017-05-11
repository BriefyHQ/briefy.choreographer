"""Slack actions for Assignments."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack import Slack
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
                {'title': 'Project',
                 'value': data.get('project', {}).get('title'),
                 'short': True,
                 },
            ]
        }
        professional = data.get('professional')
        if professional:
            payload['data']['fields'].append(
                {'title': 'Creative',
                 'value': data.get('professional', {}).get('title'),
                 'short': True,
                 },
            )
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


@adapter(events.IAssignmentWfPublish)
@implementer(ISlack)
class AssignmentWfPublish(AssignmentSlack):
    """After publish, post on Slack."""

    title = 'Assignment published!'


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


@adapter(events.IAssignmentWfRetract)
@implementer(ISlack)
class AssignmentWfRetract(AssignmentSlack):
    """After retract from publish to pending, post on Slack."""

    title = 'Assignment retracted to pending!'


@adapter(events.IAssignmentWfReadyForUpload)
@implementer(ISlack)
class AssignmentWfReadyForUpload(AssignmentSlack):
    """After moving to awaiting assets, post on Slack."""

    title = 'Assignment moved to awaiting assets!'


@adapter(events.IAssignmentWfInvalidateAssets)
@implementer(ISlack)
class AssignmentWfInvalidateAssets(AssignmentSlack):
    """After invalidate assets, post on Slack."""

    title = 'Assignment moved back to awaiting assets, machine invalidate upload!'


@adapter(events.IAssignmentWfValidateAssets)
@implementer(ISlack)
class AssignmentWfValidateAssets(AssignmentSlack):
    """After validate assets, post on Slack."""

    title = 'Assignment moved to QA, machine validate upload!'


@adapter(events.IAssignmentWfRetractRejection)
@implementer(ISlack)
class AssignmentWfRetractRejection(AssignmentSlack):
    """After manual retract set from awaiting assets to QA, post on Slack."""

    title = 'Assignment moved from awaiting assets to QA using retract rejection transition!'


@adapter(events.IAssignmentWfRetractApproval)
@implementer(ISlack)
class AssignmentWfRetractApproval(AssignmentSlack):
    """After manual retract set from approved to QA, post on Slack."""

    title = 'Assignment moved from approved to QA using retract approval transition!'


@adapter(events.IAssignmentWfPermReject)
@implementer(ISlack)
class AssignmentWfPermReject(AssignmentSlack):
    """After permanently reject, post on Slack."""

    title = 'Assignment permanently reject from QA!'


@adapter(events.IAssignmentWfEditPayout)
@implementer(ISlack)
class AssignmentWfEditPayout(AssignmentSlack):
    """After edit payout, post on Slack."""

    title = 'Assignment payout edit!'


@adapter(events.IAssignmentWfEditCompensation)
@implementer(ISlack)
class AssignmentWfEditCompensation(AssignmentSlack):
    """After edit compensation, post on Slack."""

    title = 'Assignment compensation edit!'


@adapter(events.IAssignmentWfReturnToQa)
@implementer(ISlack)
class AssignmentWfReturnToQa(AssignmentSlack):
    """After move from refused to QA, post on Slack."""

    title = 'Assignment moved from refused back to QA!'


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


@adapter(events.IAssignmentWfRemoveSchedule)
@implementer(ISlack)
class AssignmentWfRemoveSchedule(AssignmentSlack):
    """Post on Slack on remove_schedule of an assignment."""

    title = 'Scheduled removed from Assignment, moving to assigned.'


@adapter(events.IAssignmentWfReschedule)
@implementer(ISlack)
class AssignmentWfReschedule(AssignmentSlack):
    """Post on Slack on reschedule of an assignment."""

    title = 'Assignment was re-scheduled'


@adapter(events.IAssignmentWfAssignQAManager)
@implementer(ISlack)
class AssignmentWfAssignQAManager(AssignmentSlack):
    """Post on Slack when a QA Manager begin the review process."""

    title = 'QA Manager started the review'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        qa_managers = data['qa_managers']
        if qa_managers:
            qa_manager = qa_managers[0]
            fields = payload['data']['fields']
            fields.append(
                {
                    'title': 'QA Manager',
                    'value': qa_manager.get('fullname', ''),
                    'short': True,
                },
            )
            payload['data']['fields'] = fields
        return payload


@adapter(events.IAssignmentWfSubmit)
@implementer(ISlack)
class AssignmentWfSubmit(AssignmentSlack):
    """Post on Slack when an assignment is pending."""

    title = 'New assignment is in pending state'


@adapter(events.IAssignmentWfSubmit)
@implementer(ISlack)
class AssignmentWfSubmitScout(AssignmentSlack):
    """Post on Slack when an assignment is pending."""

    _channel = '#scouting-team'
    title = 'New assignment is available'


@adapter(events.IAssignmentWfStartPostProcess)
@implementer(ISlack)
class AssignmentWfStartPostProcess(AssignmentSlack):
    """Post on Slack when an assignment is moved to post_processing state."""

    title = 'Assignment start to be post processed.'
