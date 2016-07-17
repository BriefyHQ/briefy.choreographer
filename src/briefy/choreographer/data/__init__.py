"""Module that implements data models."""
from zope.interface import Interface


class IDataTransferObject(Interface):
    """Data transfer object."""

    def update():
        """Update data from external source."""


class DTO:
    """Data transfer object."""

    def __init__(self, **kw):
        """Initialize the object."""
        self._update_from_dict(**kw)

    def _update_from_dict(self, **kw):
        """Update data from a dictionary."""
        for k, v in kw.items():
            setattr(self, k, v)
