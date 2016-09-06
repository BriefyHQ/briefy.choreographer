"""Mail action for Lead."""
from briefy.choreographer.actions.mail import Mail
from briefy.choreographer.actions.mail import IMail
from briefy.choreographer.config import MAIL_ACTION_LEAD_SENDER_EMAIL
from briefy.choreographer.config import MAIL_ACTION_LEAD_SENDER_NAME
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer


class LeadMail(Mail):
    """Mail sent on Lead events."""

    entity = 'Lead'
    weight = 100

    @property
    def sender(self):
        """Return sender information for this action.

        :returns: Dictionary with two keys - name, email
        :rtype: dict
        """
        return {
            'name': MAIL_ACTION_LEAD_SENDER_NAME,
            'email': MAIL_ACTION_LEAD_SENDER_EMAIL,
        }

    def transform(self):
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload['fullname'] = data.get('fullname')
        payload['email'] = data.get('email')
        payload['data'] = {
            'FULLNAME': data.get('fullname'),
            'EMAIL': data.get('email'),
            'CATEGORY': data.get('category'),
            'SUBJECT': self.subject,
        }
        return payload


@adapter(lead.ILeadCreated)
@implementer(IMail)
class LeadCreated(LeadMail):
    """After creating a new Lead, send an email."""

    template_name = 'briefy-new-lead-professional'
    subject = '''You're Officially a Briefy Insider!'''

    @property
    def available(self):
        """Should not fire an email """
        available = super().available
        data = self.data
        return available and data.get('internal')
