"""Briefy Choreographer data objects tests."""
from briefy.choreographer.data.mail import IMailDTO
from briefy.choreographer.data.mail import MailDTO
from conftest import BaseDataCase


class TestMailDTO(BaseDataCase):
    """Test MailDTO."""

    data_class = MailDTO
    data_interface = IMailDTO
    data_file = 'mail.json'
