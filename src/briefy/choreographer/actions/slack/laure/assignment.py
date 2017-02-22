"""Slack Actions for Ms. Laure Assignment events."""
from briefy.choreographer.actions.slack.laure import LaureSlack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events import laure as events
from zope.component import adapter
from zope.interface import implementer


class Assignment(LaureSlack):
    """Handle assignment events to be sent to Slack."""

    entity = 'Assignment'
    title = 'Assignment'
    text = ''

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        assignment = data['assignment'] or {}
        payload['title'] = self.title
        payload['text'] = (
            'Assignment can be seen <{url}|here> and the submission <{link}|here>'.format(
                url=self._action_url,
                link=assignment['submission_link']
            )
        )
        payload['username'] = 'Ms. Laure'
        payload['pretext'] = '{project}: Assignment #{code}'.format(
            project=assignment['project_name'],
            code=assignment['code']
        ),
        payload['data'] = {
            'fields': [
                {
                    'title': 'Internal Status',
                    'value': assignment['approval_status'],
                    'short': True
                },
                {
                    'title': 'Responsible Photographer',
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

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        validation = data.get('validation', {})
        fields = payload['data']['fields']
        fields.append(
            {
                'title': '# submitted / required',
                'value': '{0} / {1}'.format(
                    validation['total_images'],
                    validation['number_of_photos']
                ),
                'short': True
            },
        )
        fields.append(
            {
                'title': '# validated / failed',
                'value': '{0} / {1}'.format(
                    validation['total_passed'],
                    validation['total_failed']
                ),
                'short': True
            }
        )
        payload['data']['fields'] = fields
        payload['color'] = 'good'
        return payload


@adapter(events.ILaureAssignmentRejected)
@implementer(ISlack)
class AssignmentInvalidated(Assignment):
    """Send invalidated assignment data to Leica."""

    title = 'Assignment rejected by Ms. Laure'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        validation = data.get('validation', {})
        fields = payload['data']['fields']
        feedback = validation.get('complete_feedback', '')
        fields.append(
            {
                'title': '# submitted / required',
                'value': '{0} / {1}'.format(
                    validation['total_images'],
                    validation['number_of_photos']
                ),
                'short': True
            },
        )
        fields.append(
            {
                'title': '# validated / failed',
                'value': '{0} / {1}'.format(
                    validation['total_passed'],
                    validation['total_failed']
                ),
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
        payload['data']['fields'] = fields
        payload['color'] = 'danger'
        return payload


@adapter(events.ILaureAssignmentIgnored)
@implementer(ISlack)
class AssignmentIgnored(Assignment):
    """Send ignored assignment data to Leica."""

    title = 'Assignment ignored by Ms. Laure'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        payload['color'] = 'warning'
        return payload


@adapter(events.ILaureAssignmentCopied)
@implementer(ISlack)
class AssignmentCopied(Assignment):
    """Send data on assignment copied data to Leica."""

    title = 'Assignment copied by Ms. Laure'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        delivery_link = data['delivery_url']
        archive_link = data['archive_url']
        payload['text'] = (
            'Assignment can be seen <{url}|here>, <{url_1}|delivery> and <{url_2}|archive>'.format(
                url=self._action_url,
                url_1=delivery_link,
                url_2=archive_link,
            )
        )
        payload['color'] = 'good'
        return payload


@adapter(events.ILaureAssignmentCopyFailure)
@implementer(ISlack)
class AssignmentCopyFailure(Assignment):
    """Send notification that assets failed to be copied to Leica."""

    title = 'There was an issue copying the files to delivery and archive'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        payload['color'] = 'danger'
        return payload
