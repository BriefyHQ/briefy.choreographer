"""Briefy Choreographer data objects tests."""
from briefy.choreographer.data.lead import ILeadDTO
from briefy.choreographer.data.lead import LeadDTO
from conftest import BaseDataCase


class TestLeadDTO(BaseDataCase):
    """Test LeadDTO."""

    data_class = LeadDTO
    data_interface = ILeadDTO
    data_file = 'lead.json'
