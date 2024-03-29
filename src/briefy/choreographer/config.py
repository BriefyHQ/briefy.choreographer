"""Briefy Choreographer config."""
from briefy.common.config import _queue_suffix
from prettyconf import config


ENV = config('ENV', default='staging')

# NewRelic
NEW_RELIC_LICENSE_KEY = config('NEW_RELIC_LICENSE_KEY', default='')

# Mail Action
MAIL_ACTION_SENDER_NAME = config('MAIL_ACTION_SENDER_NAME', default='Briefy Team')
MAIL_ACTION_SENDER_EMAIL = config('MAIL_ACTION_SENDER_EMAIL', default='site@briefy.co')

MAIL_ACTION_LEICA_SENDER_NAME = config('MAIL_ACTION_LEICA_SENDER_NAME', default='Briefy Team')
MAIL_ACTION_LEICA_SENDER_EMAIL = config('MAIL_ACTION_LEICA_SENDER_EMAIL', default='site@briefy.co')
# Leica configs are also used by Laure,
# since it is a sub-service that should be transparent to users.

MAIL_ACTION_LEAD_SENDER_NAME = config('MAIL_ACTION_LEAD_SENDER_NAME', default='Andre from Briefy')
MAIL_ACTION_LEAD_SENDER_EMAIL = config('MAIL_ACTION_LEAD_SENDER_EMAIL', default='hello@briefy.co')

MAIL_ACTION_QUOTE_SENDER_NAME = config('MAIL_ACTION_QUOTE_SENDER_NAME', default='Andre from Briefy')
MAIL_ACTION_QUOTE_SENDER_EMAIL = config('MAIL_ACTION_QUOTE_SENDER_EMAIL', default='hello@briefy.co')

# Queues
MAIL_QUEUE = config('MAIL_QUEUE', default='mail-{0}'.format(_queue_suffix))
NOTIFICATION_QUEUE = config('NOTIFICATION_QUEUE', default='notification-{0}'.format(_queue_suffix))

# Slack
SLACK_QUEUE = config('SLACK_QUEUE', default='slack-{0}'.format(_queue_suffix))

# Laure
LAURE_VALIDATION_QUEUE = config('LAURE_VALIDATION_QUEUE', default='laure-{0}'.format(_queue_suffix))
LAURE_DELIVERY_QUEUE = config('LAURE_DELIVERY_QUEUE', default='delivery-{0}'.format(_queue_suffix))

# Reflex
REFLEX_QUEUE = config('REFLEX_QUEUE', default='reflex-{0}'.format(_queue_suffix))

# Leica
LEICA_QUEUE = config('LEICA_QUEUE', default='leica-{0}'.format(_queue_suffix))

# Platform
PLATFORM_URL = config('PLATFORM_URL', default='https://app.stg.briefy.co/')
DELIVERY_URL = config('DELIVERY_URL', default='https://delivery.stg.briefy.co/')

# BigQuery
DATASET = config('DATASET', default='app_events_{0}'.format(_queue_suffix))
TABLE = config('TABLE', default='events')
GOOGLE_APPLICATION_CREDENTIALS = config('GOOGLE_APPLICATION_CREDENTIALS', default='')


def is_production() -> bool:
    """Return if we are running in a live environment."""
    return True if ENV == 'production' else False
