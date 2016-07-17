"""Module that implements `briefy.leads.models.lead.Lead` data model."""
from briefy.choreographer.data import DTO
from briefy.choreographer.data import IDataTransferObject
from zope.interface import implementer


class ILeadDTO(IDataTransferObject):
    """Lead transfer object."""


@implementer(ILeadDTO)
class LeadDTO(DTO):
    """Lead transfer object."""
