"""Briefy Assignment Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class ILaureAssignmentEvent(IInternalEvent):
    """Interface for IDataEvent on an Assignment object."""


class ILaureAssignmentValidated(ILaureAssignmentEvent):
    """An Assignment was validated."""


class ILaureAssignmentRejected(ILaureAssignmentEvent):
    """An Assignment was rejected."""


class ILaureAssignmentCopied(ILaureAssignmentEvent):
    """An Assignment's assets were copyed to other folder(s)."""


class ILaureAssignmentCopyFailure(ILaureAssignmentEvent):
    """An Assignment's assets failed to be copyied to other folder(s)."""


class LaureAssignmentEvent(InternalEvent):
    """An event to an Assignment."""


@implementer(ILaureAssignmentValidated)
class LaureAssignmentValidated(LaureAssignmentEvent):
    """An assignment was validated."""

    event_name = 'laure.assignment.validated'
    """Event name."""


@implementer(ILaureAssignmentRejected)
class LaureAssignmentRejected(LaureAssignmentEvent):
    """An assignment was rejected."""

    event_name = 'laure.assignment.rejected'
    """Event name."""


@implementer(ILaureAssignmentCopied)
class LaureAssignmentCopied(LaureAssignmentEvent):
    """An Assignment's assets were copyed to other folder(s)."""

    event_name = 'laure.assignment.copyied'
    """Event name."""


@implementer(ILaureAssignmentRejected)
class LaureAssignmentCopyFailure(LaureAssignmentEvent):
    """An Assignment's assets failed to be copyied to other folder(s)."""

    event_name = 'laure.assignment.copy_failure'
    """Event name."""