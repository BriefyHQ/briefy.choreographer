"""Module that implements Briefy subscribers for Mail events."""
from briefy.choreographer.data.mail import MailDTO
from briefy.choreographer.subscribers import BaseHandler


class Handler(BaseHandler):
    """Handler for Mail events."""

    _info_class_ = MailDTO


def handler(event):
    """Handle Mail events.

    :param event: Event
    :type event: briefy.choreographer.events.mail.IMailEvent
    """
    handler = Handler(event)
    handler()
