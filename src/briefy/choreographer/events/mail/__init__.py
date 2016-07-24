"""Briefy Mail Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class IMailEvent(IInternalEvent):
    """An event related to a Mail."""


class IMailSent(IMailEvent):
    """An email was sent."""


class MailEvent(InternalEvent):
    """An event related to a Mail."""


@implementer(IMailSent)
class MailSent(MailEvent):
    """An email was sent."""

    event_name = 'mail.sent'
