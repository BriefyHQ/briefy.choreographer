"""Briefy Assignment Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class ILaureAssignmentEvent(IInternalEvent):
    """Interface for IDataEvent on an Assignment object."""


class ILaureAssignmentValidated(IAssignmentEvent):
    """An Assignment was validated."""


class ILaureAssignmentRejected(IAssignmentEvent):
    """An Assignment was rejected."""


class ILaureAssignmentCopied(IAssignmentEvent):
    """An Assignment's assets were copyed to other folder(s)."""


class ILaureAssignmentCopyFailure(IAssignmentEvent):
    """An Assignment's assets failed to be copyied to other folder(s)."""


class LaureAssignmentEvent(InternalEvent):
    """An event to an Assignment."""


@implementer(ILaureAssignmentValidated)
class LaureAssignmentValidated(AssignmentEvent):
    """An assignment was validated."""

    event_name = 'laure.assignment.validated'
    """Event name."""


@implementer(IAssignmentRejected)
class LaureAssignmentRejected(AssignmentEvent):
    """An assignment was rejected."""

    event_name = 'laure.assignment.rejected'
    """Event name."""


@implementer(IAssignmentCopied)
class LaureAssignmentCopied(AssignmentEvent):
    """An Assignment's assets were copyed to other folder(s)."""

    event_name = 'laure.assignment.copyied'
    """Event name."""


@implementer(IAssignmentRejected)
class LaureAssignmentCopyFailure(AssignmentEvent):
    """An Assignment's assets failed to be copyied to other folder(s)."""

    event_name = 'laure.assignment.copy_failure'
    """Event name."""
