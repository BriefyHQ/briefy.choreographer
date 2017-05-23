"""Slack Actions for Ms. Laure Assignment events."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack.laure import LaureSlack
from briefy.choreographer.events import laure as events
from textwrap import dedent
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
        delivery_link = data.get('delivery_url')
        archive_link = data.get('archive_url')
        payload['text'] = (
            'Assignment can be seen <{url}|here>, <{url_1}|delivery> and <{url_2}|archive>'.format(
                url=self._action_url,
                url_1=delivery_link,
                url_2=archive_link,
            )
        )
        payload['color'] = 'good'
        return payload


@adapter(events.ILaureAssignmentIgnoredCopy)
@implementer(ISlack)
class AssignmentIgnoredCopy(AssignmentCopied):
    """Send data on assignment not-copied to slack."""

    title = 'Assignment photos not touched by Ms. Laure'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        payload['text'] = dedent(
            """\
            This approval was a result of photo reviewing after an initial
            client refusal for the set. The system can't know in which folders the photos
            had been updated, and therefore won't copy any images.
            The Approver is **responsible** for manually copying the modified assets
            to the appropriate folder!
            """
        ).replace('\n', ' ') + '\n\n' + payload['text']
        payload['color'] = 'warning'
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

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        payload['color'] = 'danger'
        return payload


@adapter(events.ILaureAssignmentPostProcessingComplete)
@implementer(ISlack)
class AssignmentPostProcessingComplete(Assignment):
    """Send notification that post process complete with success  by ms.laure."""

    title = 'Post process complete with success.'
