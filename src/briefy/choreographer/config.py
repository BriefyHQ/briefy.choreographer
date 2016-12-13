"""Briefy Choreographer config."""
from briefy.common.config import _queue_suffix
from prettyconf import config


ENV = config('ENV', default='staging')

# NewRelic
NEW_RELIC_LICENSE_KEY = config('NEW_RELIC_LICENSE_KEY', default='')

# Mail Action
MAIL_ACTION_LEAD_SENDER_NAME = config('MAIL_ACTION_LEAD_SENDER_NAME', default='Andre from Briefy')
MAIL_ACTION_LEAD_SENDER_EMAIL = config('MAIL_ACTION_LEAD_SENDER_EMAIL', default='hello@briefy.co')

MAIL_ACTION_QUOTE_SENDER_NAME = config('MAIL_ACTION_QUOTE_SENDER_NAME', default='Andre from Briefy')
MAIL_ACTION_QUOTE_SENDER_EMAIL = config('MAIL_ACTION_QUOTE_SENDER_EMAIL', default='hello@briefy.co')

# Queues
MAIL_QUEUE = config('MAIL_QUEUE', default='mail-{0}'.format(_queue_suffix))
NOTIFICATION_QUEUE = config('NOTIFICATION_QUEUE', default='notification-{0}'.format(_queue_suffix))

# Slack
SLACK_QUEUE = config('SLACK_QUEUE', default='slack-{0}'.format(_queue_suffix))


def is_production() -> bool:
    """Return if we are running in a live environment."""
    return True if ENV == 'production' else False
