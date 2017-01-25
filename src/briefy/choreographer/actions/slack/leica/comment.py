"""Slack actions for Comments."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events.leica import comment as events
from zope.component import adapter
from zope.interface import implementer


class CommentSlack(Slack):
    """Base class for Slack message sent on Comment events."""

    entity = 'Comment'
    weight = 100
    _channel = '#tests'
    title = 'Comment'
    text = 'New Comment!!'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = self.title
        payload['text'] = self.text
        payload['username'] = 'Briefy Bot'
        author_info = '{0} ({1})'.format(
            data.get('author', {}).get('fullname'),
            data.get('author_role'),
        )
        payload['data'] = {
            'fields': [
                {'title': 'Author',
                 'value': author_info,
                 'short': True,
                 },
                {'title': 'To',
                 'value': data.get('to_role'),
                 'short': True,
                 },
                {'title': 'Entity ID',
                 'value': data.get('entity', {}).get('slug', ''),
                 'short': True,
                 },
                {'title': 'Comment',
                 'value': data.get('comment'),
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
