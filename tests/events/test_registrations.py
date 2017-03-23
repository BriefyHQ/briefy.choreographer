"""Tests for `briefy.choreographer.worker` module."""
from briefy import choreographer
from briefy.choreographer.events import IInternalEvent
from zope.component import queryUtility
from zope.configuration.xmlconfig import XMLConfig

import pytest


XMLConfig('configure.zcml', choreographer)()


LEICA_EVENTS = [
    'asset.created',
    'asset.updated',
    'asset.workflow.approve',
    'asset.workflow.delete',
    'asset.workflow.discard',
    'asset.workflow.invalidate',
    'asset.workflow.process',
    'asset.workflow.refuse',
    'asset.workflow.request_edit',
    'asset.workflow.reserve',
    'asset.workflow.retract',
    'asset.workflow.submit',
    'asset.workflow.validate',
    'assignment.created',
    'assignment.updated',
    'assignment.workflow.approve',
    'assignment.workflow.assign',
    'assignment.workflow.assign_pool',
    'assignment.workflow.assign_qa_manager',
    'assignment.workflow.cancel',
    'assignment.workflow.complete',
    'assignment.workflow.edit_compensation',
    'assignment.workflow.edit_payout',
    'assignment.workflow.invalidate_assets',
    'assignment.workflow.perm_reject',
    'assignment.workflow.publish',
    'assignment.workflow.ready_for_upload',
    'assignment.workflow.refuse',
    'assignment.workflow.reject',
    'assignment.workflow.remove_schedule',
    'assignment.workflow.reschedule',
    'assignment.workflow.retract',
    'assignment.workflow.retract_approval',
    'assignment.workflow.retract_rejection',
    'assignment.workflow.return_to_qa',
    'assignment.workflow.schedule',
    'assignment.workflow.scheduling_issues',
    'assignment.workflow.self_assign',
    'assignment.workflow.submit',
    'assignment.workflow.upload',
    'assignment.workflow.validate_assets',
    'briefyuserprofile.created',
    'briefyuserprofile.updated',
    'briefyuserprofile.workflow.activate',
    'briefyuserprofile.workflow.inactivate',
    'comment.created',
    'comment.updated',
    'customer.created',
    'customer.updated',
    'customer.workflow.activate',
    'customer.workflow.inactivate',
    'customer.workflow.submit',
    'customeruserprofile.created',
    'customeruserprofile.updated',
    'customeruserprofile.workflow.activate',
    'customeruserprofile.workflow.inactivate',
    'link.workflow.delete',
    'order.created',
    'order.updated',
    'order.workflow.accept',
    'order.workflow.assign',
    'order.workflow.cancel',
    'order.workflow.deliver',
    'order.workflow.edit_location',
    'order.workflow.edit_requirements',
    'order.workflow.new_shoot',
    'order.workflow.perm_refuse',
    'order.workflow.reassign',
    'order.workflow.refuse',
    'order.workflow.remove_availability',
    'order.workflow.remove_schedule',
    'order.workflow.require_revision',
    'order.workflow.reshoot',
    'order.workflow.schedule',
    'order.workflow.set_availability',
    'order.workflow.start_qa',
    'order.workflow.submit',
    'order.workflow.unassign',
    'pool.created',
    'pool.updated',
    'pool.workflow.disable',
    'pool.workflow.reactivated',
    'pool.workflow.submit',
    'professional.created',
    'professional.updated',
    'professional.workflow.activate',
    'professional.workflow.approve',
    'professional.workflow.assign',
    'professional.workflow.delete',
    'professional.workflow.inactivate',
    'professional.workflow.reject',
    'professional.workflow.submit',
    'professional.workflow.validate',
    'project.created',
    'project.updated',
    'project.workflow.close',
    'project.workflow.pause',
    'project.workflow.start',
    'workinglocation.workflow.delete',
    'workinglocation.workflow.inactivate',
    'workinglocation.workflow.submit'
]


ROLLEIFLEX_EVENTS = [
    'user.created',
    'user.password.changed',
    'user.password.reset',
    'user.login',
    'user.login.first',
]


LAURE_EVENTS = [
    'laure.assignment.copy_failure',
    'laure.assignment.copied',
    'laure.assignment.ignored_copy',
    'laure.assignment.ignored',
    'laure.assignment.rejected',
    'laure.assignment.validated',
]

EVENTS = LEICA_EVENTS + ROLLEIFLEX_EVENTS + LAURE_EVENTS


@pytest.mark.parametrize("event_name", EVENTS)
def test_events_with_factories(event_name):
    assert queryUtility(IInternalEvent, event_name, None) is not None
