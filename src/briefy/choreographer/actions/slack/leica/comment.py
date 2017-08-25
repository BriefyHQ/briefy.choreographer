"""Slack actions for Comments."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.events.leica import comment as events
from zope.component import adapter
from zope.interface import implementer

import typing as t


class CommentSlack(Slack):
    """Base class for Slack message sent on Comment events."""

    entity = 'Comment'
    weight = 100
    _channel = '#leica-comments'
    title = 'Comment'
    text = 'New Comment!!'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        data = self.data
        payload_item['title'] = self.title
        payload_item['text'] = self.text
        payload_item['username'] = 'Briefy Bot'
        author_name = data.get('author', {}).get('fullname')
        author_role = data.get('author_role')
        author_info = f'{author_name} ({author_role})'
        payload_item['data'] = {
            'fields': [
                {'title': 'Author',
                 'value': author_info,
                 'short': True,
                 },
                {'title': 'To',
                 'value': data.get('to_role'),
                 'short': True,
                 },
                {'title': 'Entity',
                 'value': data.get('entity_type', ''),
                 'short': True,
                 },
                {'title': 'Entity ID',
                 'value': data.get('entity', {}).get('slug', ''),
                 'short': True,
                 },
                {'title': 'Comment',
                 'value': data.get('content'),
                 'short': False,
                 },
            ]
        }
        return payload


@adapter(events.ICommentCreated)
@implementer(ISlack)
class CommentCreated(CommentSlack):
    """After creating a new comment, post on Slack."""

    title = 'New comment!'
    text = 'New comment was created, see the details:'
