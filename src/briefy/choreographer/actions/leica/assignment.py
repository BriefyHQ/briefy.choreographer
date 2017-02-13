"""Leica Actions for Assignment."""
from briefy.choreographer.actions.leica import ILeicaAction
from briefy.choreographer.actions.leica import LeicaAction
from briefy.choreographer.events import laure as events
from zope.component import adapter
from zope.interface import implementer


@adapter(events.ILaureAssignmentValidated)
@implementer(ILeicaAction)
class AssignmentValidated(LeicaAction):
    """Send validated assignment data to Leica."""

    entity = 'Assignment'


@adapter(events.ILaureAssignmentRejected)
@implementer(ILeicaAction)
class AssignmentInvalidated(LeicaAction):
    """Send invalidated assignment data to Leica."""

    entity = 'Assignment'


@adapter(events.ILaureAssignmentCopied)
@implementer(ILeicaAction)
class AssignmentCopied(LeicaAction):
    """Send data on assignment copied data to Leica."""

    entity = 'Assignment'


@adapter(events.ILaureAssignmentCopyFailure)
@implementer(ILeicaAction)
class AssignmentCopyFailure(LeicaAction):
    """Send notification that assets failed to be copied to Leica."""

    entity = 'Assignment'
