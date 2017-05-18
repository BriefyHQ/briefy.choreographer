"""Briefy Assignment Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class ILaureEvent(IInternalEvent):
    """Interface for IDataEvent from Ms. Laure."""


class ILaureAssignmentEvent(ILaureEvent):
    """Interface for IDataEvent on an Assignment object."""


class ILaureAssignmentValidated(ILaureAssignmentEvent):
    """An Assignment was validated."""


class ILaureAssignmentRejected(ILaureAssignmentEvent):
    """An Assignment was rejected."""


class ILaureAssignmentIgnored(ILaureAssignmentEvent):
    """An Assignment was ignored."""


class ILaureAssignmentCopied(ILaureAssignmentEvent):
    """An Assignment's assets were copied to other folder(s)."""


class ILaureAssignmentIgnoredCopy(ILaureAssignmentEvent):
    """An Assignment's assets were not copied to other folders."""


class ILaureAssignmentCopyFailure(ILaureAssignmentEvent):
    """An Assignment's assets failed to be copied to other folder(s)."""


class ILaureAssignmentPostProcessingStarted(ILaureAssignmentEvent):
    """An Assignment's assets start the post process execution on ms.laure."""


class ILaureAssignmentPostProcessingFailed(ILaureAssignmentEvent):
    """An Assignment's assets failed the post process execution on ms.laure."""


class ILaureAssignmentPostProcessingComplete(ILaureAssignmentEvent):
    """An Assignment's assets complete the post process execution on ms.laure."""


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


@implementer(ILaureAssignmentIgnored)
class LaureAssignmentIgnored(LaureAssignmentEvent):
    """An assignment was ignored."""

    event_name = 'laure.assignment.ignored'
    """Event name."""


@implementer(ILaureAssignmentCopied)
class LaureAssignmentCopied(LaureAssignmentEvent):
    """An Assignment's assets were copyed to other folder(s)."""

    event_name = 'laure.assignment.copied'
    """Event name."""


@implementer(ILaureAssignmentIgnoredCopy)
class LaureAssignmentIgnoredCopy(LaureAssignmentEvent):
    """An Assignment's assets were not copied to other folders.

    when it happens due to desired settings, not due to failure.
    """

    event_name = 'laure.assignment.ignored_copy'
    """Event name."""


@implementer(ILaureAssignmentRejected)
class LaureAssignmentCopyFailure(LaureAssignmentEvent):
    """An Assignment's assets failed to be copied to other folder(s)."""

    event_name = 'laure.assignment.copy_failure'
    """Event name."""


@implementer(ILaureAssignmentPostProcessingStarted)
class LaureAssignmentPostProcessingStarted(LaureAssignmentEvent):
    """An Assignment's assets started post processing."""

    event_name = 'laure.assignment.post_processing_started'
    """Event name."""


@implementer(ILaureAssignmentPostProcessingFailed)
class LaureAssignmentPostProcessingFailed(LaureAssignmentEvent):
    """An Assignment's assets failed post processing."""

    event_name = 'laure.assignment.post_processing_failed'
    """Event name."""


@implementer(ILaureAssignmentPostProcessingComplete)
class LaureAssignmentPostProcessingComplete(LaureAssignmentEvent):
    """An Assignment's assets complete post processing."""

    event_name = 'laure.assignment.post_processing_complete'
    """Event name."""
