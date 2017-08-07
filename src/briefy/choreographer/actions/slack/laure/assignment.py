"""Slack Actions for Ms. Laure Assignment events."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack.laure import LaureSlack
from briefy.choreographer.events import laure as events
from textwrap import dedent
from zope.component import adapter
from zope.interface import implementer

import typing as t


class Assignment(LaureSlack):
    """Handle assignment events to be sent to Slack."""

    entity = 'Assignment'
    title = 'Assignment'
    text = ''

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        data = self.data
        assignment = data['assignment'] or {}
        url = self._action_url
        link = assignment.get('submission_link', '')
        project_name = assignment.get('project_name', '')
        slug = assignment.get('slug')
        payload_item['title'] = self.title
        payload_item['text'] = (
            f'Assignment can be seen <{url}|here> and the submission <{link}|here>'
        )
        payload_item['username'] = 'Ms. Laure'
        payload_item['pretext'] = f'{project_name}: Assignment #{slug}'
        payload_item['data'] = {
            'fields': [
                {
                    'title': 'Internal Status',
                    'value': assignment['approval_status'],
                    'short': True
                },
                {
                    'title': 'Content Creator',
                    'value': assignment['professional_name'],
                    'short': True
                }
            ]
        }
        return payload


@adapter(events.ILaureAssignmentValidated)
@implementer(ISlack)
class AssignmentValidated(Assignment):
    """Send validated assignment data to Leica."""

    title = 'Assignment validated by Ms. Laure'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        data = self.data
        validation = data.get('validation', {})
        total_images = validation.get('total_images', 0)
        number_of_photos = validation.get('number_of_photos', 0)
        total_passed = validation.get('total_passed', 0)
        total_failed = validation.get('total_failed', 0)
        fields = payload_item['data']['fields']
        fields.append(
            {
                'title': '# submitted / required',
                'value': f'{total_images} / {number_of_photos}',
                'short': True
            },
        )
        fields.append(
            {
                'title': '# validated / failed',
                'value': f'{total_passed} / {total_failed}',
                'short': True
            }
        )
        payload_item['data']['fields'] = fields
        payload_item['color'] = 'good'
        return payload


@adapter(events.ILaureAssignmentRejected)
@implementer(ISlack)
class AssignmentInvalidated(Assignment):
    """Send invalidated assignment data to Leica."""

    title = 'Assignment rejected by Ms. Laure'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        data = self.data
        validation = data.get('validation', {})
        fields = payload_item['data']['fields']
        feedback = validation.get('complete_feedback', '')
        total_images = validation.get('total_images', 0)
        number_of_photos = validation.get('number_of_photos', 0)
        total_passed = validation.get('total_passed', 0)
        total_failed = validation.get('total_failed', 0)
        fields.append(
            {
                'title': '# submitted / required',
                'value': f'{total_images} / {number_of_photos}',
                'short': True
            },
        )
        fields.append(
            {
                'title': '# validated / failed',
                'value': f'{total_passed} / {total_failed}',
                'short': True
            }
        )
        if feedback:
            fields.append(
                {
                    'title': 'Rejection message',
                    'value': feedback,
                    'short': False
                }
            )
        payload_item['data']['fields'] = fields
        payload_item['color'] = 'danger'
        return payload


@adapter(events.ILaureAssignmentIgnored)
@implementer(ISlack)
class AssignmentIgnored(Assignment):
    """Send ignored assignment data to Leica."""

    title = 'Assignment ignored by Ms. Laure'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['color'] = 'warning'
        return payload


@adapter(events.ILaureAssignmentCopied)
@implementer(ISlack)
class AssignmentCopied(Assignment):
    """Send data on assignment copied data to Leica."""

    title = 'Assignment copied by Ms. Laure'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        data = self.data
        url = self._action_url
        delivery_link = data.get('delivery_url')
        archive_link = data.get('archive_url')
        payload_item['text'] = (
            f'Assignment can be seen <{url}|here>, <{delivery_link}|delivery>'
            f'and <{archive_link}|archive_link>'
        )
        payload_item['color'] = 'good'
        return payload


@adapter(events.ILaureAssignmentIgnoredCopy)
@implementer(ISlack)
class AssignmentIgnoredCopy(AssignmentCopied):
    """Send data on assignment not-copied to slack."""

    title = 'Assignment photos not touched by Ms. Laure'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['text'] = dedent(
            """\
            This approval was a result of photo reviewing after an initial
            client refusal for the set. The system can't know in which folders the photos
            had been updated, and therefore won't copy any images.
            The Approver is **responsible** for manually copying the modified assets
            to the appropriate folder!
            """
        ).replace('\n', ' ') + '\n\n' + payload_item['text']
        payload_item['color'] = 'warning'
        return payload


@adapter(events.ILaureAssignmentCopyFailure)
@implementer(ISlack)
class AssignmentCopyFailure(Assignment):
    """Send notification that assets failed to be copied to Leica."""

    title = 'There was an issue copying the files to delivery and archive'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['color'] = 'danger'
        return payload


@adapter(events.ILaureAssignmentPostProcessingStarted)
@implementer(ISlack)
class AssignmentPostProcessingStarted(Assignment):
    """Send notification that assets start to be post processed by ms.laure."""

    title = 'Started to post process the assets.'


@adapter(events.ILaureAssignmentPostProcessingFailed)
@implementer(ISlack)
class AssignmentPostProcessingFailed(Assignment):
    """Send notification that assets failed to be post processed."""

    title = 'There was an issue post processing the assets.'

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        payload_item = payload[0]
        payload_item['color'] = 'danger'
        return payload


@adapter(events.ILaureAssignmentPostProcessingComplete)
@implementer(ISlack)
class AssignmentPostProcessingComplete(Assignment):
    """Send notification that post process complete with success  by ms.laure."""

    title = 'Post process complete with success.'
