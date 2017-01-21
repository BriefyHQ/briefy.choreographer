"""Briefy WorkingLocation Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class IWorkingLocationEvent(IInternalEvent):
    """An event of a WorkingLocation."""


class IWorkingLocationWfEvent(IWorkingLocationEvent):
    """A workflow event of a WorkingLocation."""


class IWorkingLocationWfDelete(IWorkingLocationWfEvent):
    """Interface for workinglocation.workflow.delete."""


class IWorkingLocationWfInactivate(IWorkingLocationWfEvent):
    """Interface for workinglocation.workflow.inactivate."""


class IWorkingLocationWfSubmit(IWorkingLocationWfEvent):
    """Interface for workinglocation.workflow.submit."""


class WorkingLocationEvent(InternalEvent):
    """An event of a WorkingLocation."""

    entity = 'WorkingLocation'


class WorkingLocationWfEvent(WorkingLocationEvent):
    """A workflow event of a WorkingLocation."""


@implementer(IWorkingLocationWfDelete)
class WorkingLocationWfDelete(WorkingLocationWfEvent):
    """Implement WorkingLocationWfDelete."""

    event_name = 'workinglocation.workflow.delete'


@implementer(IWorkingLocationWfInactivate)
class WorkingLocationWfInactivate(WorkingLocationWfEvent):
    """Implement WorkingLocationWfInactivate."""

    event_name = 'workinglocation.workflow.inactivate'


@implementer(IWorkingLocationWfSubmit)
class WorkingLocationWfSubmit(WorkingLocationWfEvent):
    """Implement WorkingLocationWfSubmit."""

    event_name = 'workinglocation.workflow.submit'
