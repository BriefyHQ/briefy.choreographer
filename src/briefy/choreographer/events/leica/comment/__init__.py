"""Briefy Comment Events."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.interface import implementer


class ICommentEvent(IInternalEvent):
    """An event of a Comment."""


class ICommentWfEvent(ICommentEvent):
    """A workflow event of a Comment."""


class ICommentCreated(ICommentEvent):
    """Interface for comment.created."""


class ICommentUpdated(ICommentEvent):
    """Interface for comment.updated."""


class CommentEvent(InternalEvent):
    """An event of a Comment."""

    entity = 'Comment'


class CommentWfEvent(CommentEvent):
    """A workflow event of a Comment."""


@implementer(ICommentCreated)
class CommentCreated(CommentEvent):
    """Implement CommentCreated."""

    event_name = 'comment.created'


@implementer(ICommentUpdated)
class CommentUpdated(CommentEvent):
    """Implement CommentUpdated."""

    event_name = 'comment.updated'
