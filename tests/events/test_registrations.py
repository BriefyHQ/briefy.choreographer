"""Tests for `briefy.choreographer.worker` module."""
from briefy import choreographer
from briefy.choreographer.events import IInternalEvent
from zope.component import queryUtility
from zope.configuration.xmlconfig import XMLConfig

import pytest


XMLConfig('configure.zcml', choreographer)()


EVENTS = [
    'lead.created',
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
    'assignment.updated',
    'assignment.workflow.approve',
    'assignment.workflow.assign',
    'assignment.workflow.cancel',
    'assignment.workflow.complete',
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
    'comment.updated',
    'customer.updated',
    'customer.workflow.activate',
    'customer.workflow.inactivate',
    'customer.workflow.submit',
    'link.workflow.delete',
    'order.updated',
    'order.workflow.accept',
    'order.workflow.assign',
    'order.workflow.cancel',
    'order.workflow.deliver',
    'order.workflow.new_shoot',
    'order.workflow.perm_refuse',
    'order.workflow.reassign',
    'order.workflow.refuse',
    'order.workflow.remove_availability',
    'order.workflow.remove_schedule',
    'order.workflow.require_revision',
    'order.workflow.reshoot',
    'order.workflow.schedule',
    'order.workflow.start_qa',
    'order.workflow.submit',
    'order.workflow.unassign',
    'pool.updated',
    'pool.workflow.disable',
    'pool.workflow.reactivated',
    'pool.workflow.submit',
    'professional.updated',
    'professional.workflow.activate',
    'professional.workflow.approve',
    'professional.workflow.delete',
    'professional.workflow.inactivate',
    'professional.workflow.reject',
    'professional.workflow.submit',
    'professional.workflow.validate',
    'project.updated',
    'project.workflow.close',
    'project.workflow.pause',
    'project.workflow.start',
    'workinglocation.workflow.delete',
    'workinglocation.workflow.inactivate',
    'workinglocation.workflow.submit'
]


@pytest.mark.parametrize("event_name", EVENTS)
def test_events_with_factories(event_name):
    assert queryUtility(IInternalEvent, event_name, None) is not None
