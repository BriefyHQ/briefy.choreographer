"""Tests for `briefy.choreographer.worker` module."""
from briefy import choreographer
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events.subscribers import BaseHandler
from zope.component import getUtility
from zope.component import queryUtility
from zope.configuration.xmlconfig import XMLConfig

import pytest


XMLConfig('configure.zcml', choreographer)()

LEICA_EVENTS = [
    ('asset.created', 0),
    ('asset.updated', 0),
    ('asset.workflow.approve', 0),
    ('asset.workflow.delete', 0),
    ('asset.workflow.discard', 0),
    ('asset.workflow.invalidate', 0),
    ('asset.workflow.process', 0),
    ('asset.workflow.refuse', 0),
    ('asset.workflow.request_edit', 0),
    ('asset.workflow.reserve', 0),
    ('asset.workflow.retract', 0),
    ('asset.workflow.submit', 0),
    ('asset.workflow.validate', 0),
    ('assignment.created', 1),
    ('assignment.updated', 1),
    ('assignment.workflow.approve', 3),
    ('assignment.workflow.assign', 2),
    ('assignment.workflow.assign_pool', 0),
    ('assignment.workflow.assign_qa_manager', 1),
    ('assignment.workflow.cancel', 2),
    ('assignment.workflow.complete', 1),
    ('assignment.workflow.edit_compensation', 0),
    ('assignment.workflow.edit_payout', 0),
    ('assignment.workflow.invalidate_assets', 0),
    ('assignment.workflow.perm_reject', 3),
    ('assignment.workflow.publish', 1),
    ('assignment.workflow.ready_for_upload', 1),
    ('assignment.workflow.refuse', 1),
    ('assignment.workflow.reject', 2),
    ('assignment.workflow.remove_schedule', 1),
    ('assignment.workflow.reschedule', 2),
    ('assignment.workflow.retract', 1),
    ('assignment.workflow.retract_approval', 1),
    ('assignment.workflow.retract_rejection', 1),
    ('assignment.workflow.return_to_qa', 1),
    ('assignment.workflow.schedule', 2),
    ('assignment.workflow.scheduling_issues', 2),
    ('assignment.workflow.self_assign', 2),
    ('assignment.workflow.start_post_process', 2),
    ('assignment.workflow.submit', 2),
    ('assignment.workflow.upload', 2),
    ('assignment.workflow.validate_assets', 1),
    ('briefyuserprofile.created', 1),
    ('briefyuserprofile.updated', 1),
    ('briefyuserprofile.workflow.activate', 1),
    ('briefyuserprofile.workflow.inactivate', 1),
    ('comment.created', 4),
    ('comment.updated', 0),
    ('customer.created', 0),
    ('customer.updated', 0),
    ('customer.workflow.activate', 0),
    ('customer.workflow.inactivate', 0),
    ('customer.workflow.submit', 0),
    ('customeruserprofile.created', 1),
    ('customeruserprofile.updated', 1),
    ('customeruserprofile.workflow.activate', 2),
    ('customeruserprofile.workflow.inactivate', 1),
    ('leadorder.created', 1),
    ('leadorder.updated', 0),
    ('leadorder.workflow.confirm', 2),
    ('leadorder.workflow.remove_confirmation', 0),
    ('leadorder.workflow.accept', 0),
    ('leadorder.workflow.assign', 2),
    ('leadorder.workflow.cancel', 3),
    ('leadorder.workflow.deliver', 2),
    ('leadorder.workflow.edit_location', 2),
    ('leadorder.workflow.edit_requirements', 2),
    ('leadorder.workflow.new_shoot', 0),
    ('leadorder.workflow.perm_refuse', 0),
    ('leadorder.workflow.reassign', 0),
    ('leadorder.workflow.refuse', 3),
    ('leadorder.workflow.remove_availability', 2),
    ('leadorder.workflow.remove_schedule', 0),
    ('leadorder.workflow.require_revision', 0),
    ('leadorder.workflow.reshoot', 0),
    ('leadorder.workflow.schedule', 2),
    ('leadorder.workflow.set_availability', 1),
    ('leadorder.workflow.start_qa', 0),
    ('leadorder.workflow.submit', 2),
    ('leadorder.workflow.unassign', 1),
    ('link.workflow.delete', 0),
    ('order.created', 1),
    ('order.updated', 0),
    ('order.workflow.accept', 0),
    ('order.workflow.assign', 2),
    ('order.workflow.cancel', 3),
    ('order.workflow.deliver', 2),
    ('order.workflow.edit_location', 2),
    ('order.workflow.edit_requirements', 2),
    ('order.workflow.new_shoot', 0),
    ('order.workflow.perm_refuse', 0),
    ('order.workflow.reassign', 0),
    ('order.workflow.refuse', 3),
    ('order.workflow.remove_availability', 2),
    ('order.workflow.remove_schedule', 0),
    ('order.workflow.require_revision', 0),
    ('order.workflow.reshoot', 0),
    ('order.workflow.schedule', 2),
    ('order.workflow.set_availability', 1),
    ('order.workflow.start_qa', 0),
    ('order.workflow.submit', 2),
    ('order.workflow.unassign', 1),
    ('pool.created', 0),
    ('pool.updated', 0),
    ('pool.workflow.disable', 0),
    ('pool.workflow.reactivated', 0),
    ('pool.workflow.submit', 0),
    ('professional.created', 1),
    ('professional.updated', 1),
    ('professional.workflow.activate', 1),
    ('professional.workflow.approve', 3),
    ('professional.workflow.assign', 1),
    ('professional.workflow.delete', 0),
    ('professional.workflow.inactivate', 1),
    ('professional.workflow.reject', 1),
    ('professional.workflow.submit', 1),
    ('professional.workflow.validate', 2),
    ('project.created', 0),
    ('project.updated', 0),
    ('project.workflow.close', 0),
    ('project.workflow.pause', 0),
    ('project.workflow.start', 0),
    ('workinglocation.workflow.delete', 0),
    ('workinglocation.workflow.inactivate', 0),
    ('workinglocation.workflow.submit', 0),
]

LEICA_TASK_EVENTS = [
    ('leica.task.assignment_awaiting_assets.success', 0),
    ('leica.task.assignment_awaiting_assets.failure', 0),
    ('leica.task.notify_late_submission.success', 1),
    ('leica.task.notify_late_submission.failure', 1),
    ('leica.task.notify_before_shooting.success', 0),
    ('leica.task.notify_before_shooting.failure', 0),
    ('leica.task.order_accepted.success', 0),
    ('leica.task.order_accepted.failure', 0),
    ('leica.task.assignment_pool.success', 0),
    ('leica.task.assignment_pool.no_availability', 1),
    ('leica.task.assignment_pool.has_pool_id', 1),
    ('leica.task.assignment_pool.no_payout', 1),
]

LEADS_EVENTS = [
    ('lead.created', 2),
    ('quote.created', 2),
    ('package_order.created', 1),
]

ROLLEIFLEX_EVENTS = [
    ('user.created', 0),
    ('user.password.changed', 1),
    ('user.password.reset', 2),
    ('user.login', 1),
    ('user.login.first', 1),
]

LAURE_EVENTS = [
    ('laure.assignment.copy_failure', 4),
    ('laure.assignment.copied', 2),
    ('laure.assignment.ignored_copy', 2),
    ('laure.assignment.ignored', 2),
    ('laure.assignment.rejected', 4),
    ('laure.assignment.validated', 2),
]

EVENTS = LEICA_EVENTS + ROLLEIFLEX_EVENTS + LAURE_EVENTS + LEICA_TASK_EVENTS + LEADS_EVENTS


@pytest.mark.parametrize('event_name,actions', EVENTS)
def test_events_with_factories(event_name: str, actions: int):
    assert queryUtility(IInternalEvent, event_name, None) is not None


@pytest.mark.parametrize('event_name,actions', EVENTS)
def test_actions_for_factories(event_name: str, actions: int):
    payload = {
        'guid': '8e453e03-7465-4a60-840a-902a02702532',
        'actor': 'fe69e340-14c1-4843-9e15-8ef584de02e7',
        'id': '6f40c93b-145e-4bd8-a5c9-a426532ee47c',
        'created_at': '2016-07-13T10:50:13.856154',
        'request_id': '',
        'data': {}
    }
    event_factory = getUtility(IInternalEvent, event_name)
    event = event_factory(**payload)
    handler = BaseHandler(event)
    assert len(handler.actions) == actions
