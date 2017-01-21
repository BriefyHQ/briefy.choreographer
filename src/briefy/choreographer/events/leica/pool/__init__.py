"""Briefy Pool Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class IPoolEvent(IInternalEvent):
    """An event of a Pool."""


class IPoolWfEvent(IPoolEvent):
    """A workflow event of a Pool."""


class IPoolCreated(IPoolEvent):
    """Interface for pool.created."""


class IPoolUpdated(IPoolEvent):
    """Interface for pool.updated."""


class IPoolWfDisable(IPoolWfEvent):
    """Interface for pool.workflow.disable."""


class IPoolWfReactivated(IPoolWfEvent):
    """Interface for pool.workflow.reactivated."""


class IPoolWfSubmit(IPoolWfEvent):
    """Interface for pool.workflow.submit."""


class PoolEvent(InternalEvent):
    """An event of a Pool."""

    entity = 'Pool'


class PoolWfEvent(PoolEvent):
    """A workflow event of a Pool."""


@implementer(IPoolCreated)
class PoolCreated(PoolEvent):
    """Implement PoolCreated."""

    event_name = 'pool.created'


@implementer(IPoolUpdated)
class PoolUpdated(PoolEvent):
    """Implement PoolUpdated."""

    event_name = 'pool.updated'


@implementer(IPoolWfDisable)
class PoolWfDisable(PoolWfEvent):
    """Implement PoolWfDisable."""

    event_name = 'pool.workflow.disable'


@implementer(IPoolWfReactivated)
class PoolWfReactivated(PoolWfEvent):
    """Implement PoolWfReactivated."""

    event_name = 'pool.workflow.reactivated'


@implementer(IPoolWfSubmit)
class PoolWfSubmit(PoolWfEvent):
    """Implement PoolWfSubmit."""

    event_name = 'pool.workflow.submit'
