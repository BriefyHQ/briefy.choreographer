"""Briefy Professional Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class IProfessionalEvent(IInternalEvent):
    """An event of a Professional."""


class IProfessionalWfEvent(IProfessionalEvent):
    """A workflow event of a Professional."""


class IProfessionalCreated(IProfessionalEvent):
    """Interface for professional.created."""


class IProfessionalUpdated(IProfessionalEvent):
    """Interface for professional.updated."""


class IProfessionalWfActivate(IProfessionalWfEvent):
    """Interface for professional.workflow.activate."""


class IProfessionalWfApprove(IProfessionalWfEvent):
    """Interface for professional.workflow.approve."""


class IProfessionalWfDelete(IProfessionalWfEvent):
    """Interface for professional.workflow.delete."""


class IProfessionalWfInactivate(IProfessionalWfEvent):
    """Interface for professional.workflow.inactivate."""


class IProfessionalWfReject(IProfessionalWfEvent):
    """Interface for professional.workflow.reject."""


class IProfessionalWfSubmit(IProfessionalWfEvent):
    """Interface for professional.workflow.submit."""


class IProfessionalWfValidate(IProfessionalWfEvent):
    """Interface for professional.workflow.validate."""


class IProfessionalWfAssign(IProfessionalWfEvent):
    """Interface for professional.workflow.assign."""


class ProfessionalEvent(InternalEvent):
    """An event of a Professional."""

    entity = 'Professional'


class ProfessionalWfEvent(ProfessionalEvent):
    """A workflow event of a Professional."""


@implementer(IProfessionalCreated)
class ProfessionalCreated(ProfessionalEvent):
    """Implement ProfessionalCreated."""

    event_name = 'professional.created'


@implementer(IProfessionalUpdated)
class ProfessionalUpdated(ProfessionalEvent):
    """Implement ProfessionalUpdated."""

    event_name = 'professional.updated'


@implementer(IProfessionalWfActivate)
class ProfessionalWfActivate(ProfessionalWfEvent):
    """Implement ProfessionalWfActivate."""

    event_name = 'professional.workflow.activate'


@implementer(IProfessionalWfApprove)
class ProfessionalWfApprove(ProfessionalWfEvent):
    """Implement ProfessionalWfApprove."""

    event_name = 'professional.workflow.approve'


@implementer(IProfessionalWfDelete)
class ProfessionalWfDelete(ProfessionalWfEvent):
    """Implement ProfessionalWfDelete."""

    event_name = 'professional.workflow.delete'


@implementer(IProfessionalWfInactivate)
class ProfessionalWfInactivate(ProfessionalWfEvent):
    """Implement ProfessionalWfInactivate."""

    event_name = 'professional.workflow.inactivate'


@implementer(IProfessionalWfReject)
class ProfessionalWfReject(ProfessionalWfEvent):
    """Implement ProfessionalWfReject."""

    event_name = 'professional.workflow.reject'


@implementer(IProfessionalWfSubmit)
class ProfessionalWfSubmit(ProfessionalWfEvent):
    """Implement ProfessionalWfSubmit."""

    event_name = 'professional.workflow.submit'


@implementer(IProfessionalWfValidate)
class ProfessionalWfValidate(ProfessionalWfEvent):
    """Implement ProfessionalWfValidate."""

    event_name = 'professional.workflow.validate'


@implementer(IProfessionalWfAssign)
class ProfessionalWfAssign(ProfessionalWfEvent):
    """Implement ProfessionalWfAssign."""

    event_name = 'professional.workflow.assign'
