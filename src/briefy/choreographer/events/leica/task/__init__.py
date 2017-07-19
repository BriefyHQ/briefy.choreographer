"""Briefy Leica Task Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class ILeicaTaskEvent(IInternalEvent):
    """An event triggered by a task on Leica."""


class IAssignmentAwaitingAssetsSuccess(ILeicaTaskEvent):
    """Interface for leica.task.assignment_awaiting_assets.success."""


class IAssignmentAwaitingAssetsFailure(ILeicaTaskEvent):
    """Interface for leica.task.assignment_awaiting_assets.failure."""


class IAssignmentNotifyLateSubmissionSuccess(ILeicaTaskEvent):
    """Interface for leica.task.notify_late_submission.success."""


class IAssignmentNotifyLateSubmissionFailure(ILeicaTaskEvent):
    """Interface for leica.task.notify_late_submission.failure."""


class IAssignmentNotifyBeforeShootingSuccess(ILeicaTaskEvent):
    """Interface for leica.task.notify_before_shooting.success."""


class IAssignmentNotifyBeforeShootingFailure(ILeicaTaskEvent):
    """Interface for leica.task.notify_before_shooting.failure."""


class IOrderAcceptedSuccess(ILeicaTaskEvent):
    """Interface for leica.task.order_accepted.success."""


class IOrderAcceptedFailure(ILeicaTaskEvent):
    """Interface for leica.task.order_accepted.failure."""


class IAssignmentPoolSuccess(ILeicaTaskEvent):
    """Interface for leica.task.assignment_pool.success."""


class IAssignmentPoolNoAvailability(ILeicaTaskEvent):
    """Interface for leica.task.assignment_pool.no_availability."""


class IAssignmentPoolHasPoolId(ILeicaTaskEvent):
    """Interface for leica.task.assignment_pool.has_pool_id."""


class IAssignmentPoolNoPayout(ILeicaTaskEvent):
    """Interface for leica.task.assignment_pool.no_payout."""


class LeicaTaskEvent(InternalEvent):
    """An event triggered by a task on Leica."""

    entity = None


@implementer(IAssignmentAwaitingAssetsSuccess)
class AssignmentAwaitingAssetsSuccess(LeicaTaskEvent):
    """Event for Leica Task leica.task.assignment_awaiting_assets.success."""

    entity = 'Assignment'
    event_name = 'leica.task.assignment_awaiting_assets.success'


@implementer(IAssignmentAwaitingAssetsFailure)
class AssignmentAwaitingAssetsFailure(LeicaTaskEvent):
    """Event for Leica Task leica.task.assignment_awaiting_assets.failure."""

    entity = 'Assignment'
    event_name = 'leica.task.assignment_awaiting_assets.failure'


@implementer(IAssignmentNotifyLateSubmissionSuccess)
class AssignmentNotifyLateSubmissionSuccess(LeicaTaskEvent):
    """Event for Leica Task leica.task.notify_late_submission.success."""

    entity = 'Assignment'
    event_name = 'leica.task.notify_late_submission.success'


@implementer(IAssignmentNotifyLateSubmissionFailure)
class AssignmentNotifyLateSubmissionFailure(LeicaTaskEvent):
    """Event for Leica Task leica.task.notify_late_submission.failure."""

    entity = 'Assignment'
    event_name = 'leica.task.notify_late_submission.failure'


@implementer(IAssignmentNotifyBeforeShootingSuccess)
class AssignmentNotifyBeforeShootingSuccess(LeicaTaskEvent):
    """Event for Leica Task leica.task.notify_before_shooting.success."""

    entity = 'Assignment'
    event_name = 'leica.task.notify_before_shooting.success'


@implementer(IAssignmentNotifyBeforeShootingFailure)
class AssignmentNotifyBeforeShootingFailure(LeicaTaskEvent):
    """Event for Leica Task leica.task.notify_before_shooting.failure."""

    entity = 'Assignment'
    event_name = 'leica.task.notify_before_shooting.failure'


@implementer(IOrderAcceptedSuccess)
class OrderAcceptedSuccess(LeicaTaskEvent):
    """Event for Leica Task leica.task.order_accepted.success."""

    entity = 'Order'
    event_name = 'leica.task.order_accepted.success'


@implementer(IOrderAcceptedFailure)
class OrderAcceptedFailure(LeicaTaskEvent):
    """Event for Leica Task leica.task.order_accepted.failure."""

    entity = 'Order'
    event_name = 'leica.task.order_accepted.failure'


@implementer(IAssignmentPoolSuccess)
class AssignmentPoolSuccess(LeicaTaskEvent):
    """Event for Leica Task leica.task.assignment_pool.success."""

    entity = 'Assignment'
    event_name = 'leica.task.assignment_pool.success'


@implementer(IAssignmentPoolNoAvailability)
class AssignmentPoolNoAvailability(LeicaTaskEvent):
    """Event for Leica Task leica.task.assignment_pool.no_availability."""

    entity = 'Assignment'
    event_name = 'leica.task.assignment_pool.no_availability'


@implementer(IAssignmentPoolHasPoolId)
class AssignmentPoolHasPoolId(LeicaTaskEvent):
    """Event for Leica Task leica.task.assignment_pool.has_pool_id."""

    entity = 'Assignment'
    event_name = 'leica.task.assignment_pool.has_pool_id'


@implementer(IAssignmentPoolNoPayout)
class AssignmentPoolNoPayout(LeicaTaskEvent):
    """Event for Leica Task leica.task.assignment_pool.no_payout."""

    entity = 'Assignment'
    event_name = 'leica.task.assignment_pool.no_payout'
