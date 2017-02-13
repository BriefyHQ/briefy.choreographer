"""Briefy Asset Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class IAssetEvent(IInternalEvent):
    """An event of a Asset."""


class IAssetWfEvent(IAssetEvent):
    """A workflow event of a Asset."""


class IAssetCreated(IAssetEvent):
    """Interface for asset.created."""


class IAssetUpdated(IAssetEvent):
    """Interface for asset.updated."""


class IAssetWfApprove(IAssetWfEvent):
    """Interface for asset.workflow.approve."""


class IAssetWfDelete(IAssetWfEvent):
    """Interface for asset.workflow.delete."""


class IAssetWfDiscard(IAssetWfEvent):
    """Interface for asset.workflow.discard."""


class IAssetWfInvalidate(IAssetWfEvent):
    """Interface for asset.workflow.invalidate."""


class IAssetWfProcess(IAssetWfEvent):
    """Interface for asset.workflow.process."""


class IAssetWfRefuse(IAssetWfEvent):
    """Interface for asset.workflow.refuse."""


class IAssetWfRequestEdit(IAssetWfEvent):
    """Interface for asset.workflow.request_edit."""


class IAssetWfReserve(IAssetWfEvent):
    """Interface for asset.workflow.reserve."""


class IAssetWfRetract(IAssetWfEvent):
    """Interface for asset.workflow.retract."""


class IAssetWfSubmit(IAssetWfEvent):
    """Interface for asset.workflow.submit."""


class IAssetWfValidate(IAssetWfEvent):
    """Interface for asset.workflow.validate."""


class AssetEvent(InternalEvent):
    """An event of a Asset."""

    entity = 'Asset'


class AssetWfEvent(AssetEvent):
    """A workflow event of a Asset."""


@implementer(IAssetCreated)
class AssetCreated(AssetEvent):
    """Implement AssetCreated."""

    event_name = 'asset.created'


@implementer(IAssetUpdated)
class AssetUpdated(AssetEvent):
    """Implement AssetUpdated."""

    event_name = 'asset.updated'


@implementer(IAssetWfApprove)
class AssetWfApprove(AssetWfEvent):
    """Implement AssetWfApprove."""

    event_name = 'asset.workflow.approve'


@implementer(IAssetWfDelete)
class AssetWfDelete(AssetWfEvent):
    """Implement AssetWfDelete."""

    event_name = 'asset.workflow.delete'


@implementer(IAssetWfDiscard)
class AssetWfDiscard(AssetWfEvent):
    """Implement AssetWfDiscard."""

    event_name = 'asset.workflow.discard'


@implementer(IAssetWfInvalidate)
class AssetWfInvalidate(AssetWfEvent):
    """Implement AssetWfInvalidate."""

    event_name = 'asset.workflow.invalidate'


@implementer(IAssetWfProcess)
class AssetWfProcess(AssetWfEvent):
    """Implement AssetWfProcess."""

    event_name = 'asset.workflow.process'


@implementer(IAssetWfRefuse)
class AssetWfRefuse(AssetWfEvent):
    """Implement AssetWfRefuse."""

    event_name = 'asset.workflow.refuse'


@implementer(IAssetWfRequestEdit)
class AssetWfRequestEdit(AssetWfEvent):
    """Implement AssetWfRequestEdit."""

    event_name = 'asset.workflow.request_edit'


@implementer(IAssetWfReserve)
class AssetWfReserve(AssetWfEvent):
    """Implement AssetWfReserve."""

    event_name = 'asset.workflow.reserve'


@implementer(IAssetWfRetract)
class AssetWfRetract(AssetWfEvent):
    """Implement AssetWfRetract."""

    event_name = 'asset.workflow.retract'


@implementer(IAssetWfSubmit)
class AssetWfSubmit(AssetWfEvent):
    """Implement AssetWfSubmit."""

    event_name = 'asset.workflow.submit'


@implementer(IAssetWfValidate)
class AssetWfValidate(AssetWfEvent):
    """Implement AssetWfValidate."""

    event_name = 'asset.workflow.validate'
