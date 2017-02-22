"""Slack actions for Professionals."""
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.events.leica import professional as events
from zope.component import adapter
from zope.interface import implementer


class ProfessionalSlack(Slack):
    """Base class for Slack message sent on Professional events."""

    entity = 'Professional'
    weight = 100
    _channel = '#leica-creative'
    title = 'Creative'
    text = 'New Professional Profile!!'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['title'] = self.title
        payload['text'] = self.text
        payload['username'] = 'Briefy Bot'
        payload['text'] = (
            'Creative can be seen <{url}|here>'.format(
                url=self._action_url,
            )
        )
        payload['data'] = {
            'fields': [
                {
                    'title': 'Full name',
                    'value': data['title'],
                    'short': True,
                },
                {
                    'title': 'Email',
                    'value': data['email'],
                    'short': True,
                 },
                {
                    'title': 'Phone',
                    'value': data['mobile'],
                    'short': True,
                 },
                {
                    'title': 'State',
                    'value': data['state'],
                    'short': True,
                },
            ]
        }
        return payload


@adapter(events.IProfessionalCreated)
@implementer(ISlack)
class ProfessionalCreated(ProfessionalSlack):
    """After creating a new Professional, post on Slack."""

    title = 'New Creative added to Leica'


@adapter(events.IProfessionalUpdated)
@implementer(ISlack)
class ProfessionalUpdated(ProfessionalSlack):
    """After updated a new Professional, post on Slack."""

    title = 'Creative info was updated'


@adapter(events.IProfessionalWfSubmit)
@implementer(ISlack)
class ProfessionalWfSubmit(ProfessionalSlack):
    """After moving a Creative to pending, post on Slack."""

    title = 'Creative waiting for quality approval'


@adapter(events.IProfessionalWfReject)
@implementer(ISlack)
class ProfessionalWfReject(ProfessionalSlack):
    """After rejecting a Creative, post on Slack."""

    title = 'Creative was rejected'


@adapter(events.IProfessionalWfApprove)
@implementer(ISlack)
class ProfessionalWfApprove(ProfessionalSlack):
    """After quality approving a Creative, post on Slack."""

    title = 'Creative approved, waiting for legal validation'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['data'] = {
            'fields': [
                {
                    'title': 'Full name',
                    'value': data['title'],
                    'short': True,
                },
                {
                    'title': 'Email',
                    'value': data['email'],
                    'short': True,
                },
                {
                    'title': 'Phone',
                    'value': data['mobile'],
                    'short': True,
                },
                {
                    'title': 'State',
                    'value': data['state'],
                    'short': True,
                },
                {
                    'title': 'Initial Password',
                    'value': data['initial_password'],
                    'short': True,
                },
            ]
        }
        return payload


@adapter(events.IProfessionalWfApprove)
@implementer(ISlack)
class ProfessionalWfApproveFinance(ProfessionalSlack):
    """After quality approving a Creative, post on Slack."""

    _channel = '#creatives-validation'
    title = 'A new creative was approved, please proceed with legal validation'

    def transform(self) -> dict:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['data'] = {
            'fields': [
                {
                    'title': 'Full name',
                    'value': data['title'],
                    'short': True,
                },
                {
                    'title': 'Email',
                    'value': data['email'],
                    'short': True,
                },
                {
                    'title': 'Phone',
                    'value': data['mobile'],
                    'short': True,
                }
            ]
        }
        return payload


@adapter(events.IProfessionalWfValidate)
@implementer(ISlack)
class ProfessionalWfValidate(ProfessionalSlack):
    """After validating a new Professional, post on Slack."""

    title = 'Creative was validated by legal'


@adapter(events.IProfessionalWfValidate)
@implementer(ISlack)
class ProfessionalWfValidate(ProfessionalSlack):
    """After validating a new Professional, post on Slack."""

    _channel = '#scouting-team'
    title = 'Creative was validated by legal'


@adapter(events.IProfessionalWfAssign)
@implementer(ISlack)
class ProfessionalWfAssign(ProfessionalSlack):
    """After managing pools of a Professional, post on Slack."""

    title = 'Creative pools assigments changed'


@adapter(events.IProfessionalWfActivate)
@implementer(ISlack)
class ProfessionalWfActivate(ProfessionalSlack):
    """After activating a new Professional, post on Slack."""

    title = 'Creative was activated'


@adapter(events.IProfessionalWfInactivate)
@implementer(ISlack)
class ProfessionalWfInactivate(ProfessionalSlack):
    """After activating a new Professional, post on Slack."""

    title = 'Creative was inactivated'
