"""Leica Actions for Assignment."""
from briefy.choreographer.actions.leica import ILeicaAction
from briefy.choreographer.actions.leica import LeicaAction
from briefy.choreographer.events import laure as events
from zope.component import adapter
from zope.interface import implementer


class LeicaAssignment(LeicaAction):
    """Handle assignment events to be sent to Leica."""

    entity = 'Assignment'


@adapter(events.ILaureAssignmentValidated)
@implementer(ILeicaAction)
class AssignmentValidated(LeicaAssignment):
    """Send validated assignment data to Leica."""


@adapter(events.ILaureAssignmentRejected)
@implementer(ILeicaAction)
class AssignmentInvalidated(LeicaAssignment):
    """Send invalidated assignment data to Leica."""


@adapter(events.ILaureAssignmentIgnored)
@implementer(ILeicaAction)
class AssignmentIgnored(LeicaAssignment):
    """Send ignored assignment data to Leica."""


@adapter(events.ILaureAssignmentCopied)
@implementer(ILeicaAction)
class AssignmentCopied(LeicaAssignment):
    """Send data on assignment copied data to Leica."""


@adapter(events.ILaureAssignmentCopyFailure)
@implementer(ILeicaAction)
class AssignmentCopyFailure(LeicaAssignment):
    """Send notification that assets failed to be copied to Leica."""
