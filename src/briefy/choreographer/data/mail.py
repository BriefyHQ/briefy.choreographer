"""Module that implements a mail dto."""
from briefy.choreographer.data import DTO
from briefy.choreographer.data import IDataTransferObject
from zope.interface import implementer


class IMailDTO(IDataTransferObject):
    """Mail transfer object."""


@implementer(IMailDTO)
class MailDTO(DTO):
    """Mail transfer object."""
