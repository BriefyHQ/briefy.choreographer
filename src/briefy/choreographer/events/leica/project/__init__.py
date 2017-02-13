"""Briefy Project Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class IProjectEvent(IInternalEvent):
    """An event of a Project."""


class IProjectWfEvent(IProjectEvent):
    """A workflow event of a Project."""


class IProjectCreated(IProjectEvent):
    """Interface for project.created."""


class IProjectUpdated(IProjectEvent):
    """Interface for project.updated."""


class IProjectWfClose(IProjectWfEvent):
    """Interface for project.workflow.close."""


class IProjectWfPause(IProjectWfEvent):
    """Interface for project.workflow.pause."""


class IProjectWfStart(IProjectWfEvent):
    """Interface for project.workflow.start."""


class ProjectEvent(InternalEvent):
    """An event of a Project."""

    entity = 'Project'


class ProjectWfEvent(ProjectEvent):
    """A workflow event of a Project."""


@implementer(IProjectCreated)
class ProjectCreated(ProjectEvent):
    """Implement ProjectCreated."""

    event_name = 'project.created'


@implementer(IProjectUpdated)
class ProjectUpdated(ProjectEvent):
    """Implement ProjectUpdated."""

    event_name = 'project.updated'


@implementer(IProjectWfClose)
class ProjectWfClose(ProjectWfEvent):
    """Implement ProjectWfClose."""

    event_name = 'project.workflow.close'


@implementer(IProjectWfPause)
class ProjectWfPause(ProjectWfEvent):
    """Implement ProjectWfPause."""

    event_name = 'project.workflow.pause'


@implementer(IProjectWfStart)
class ProjectWfStart(ProjectWfEvent):
    """Implement ProjectWfStart."""

    event_name = 'project.workflow.start'
