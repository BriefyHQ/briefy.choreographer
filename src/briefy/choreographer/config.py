"""Briefy Choreographer config."""
from briefy.common.config import _queue_suffix
from prettyconf import config


# NewRelic
NEW_RELIC_LICENSE_KEY = config('NEW_RELIC_LICENSE_KEY', default='')

# Mail Action
MAIL_ACTION_LEAD_SENDER_NAME = config('MAIL_ACTION_LEAD_SENDER_NAME', default='Andre from Briefy')
MAIL_ACTION_LEAD_SENDER_EMAIL = config('MAIL_ACTION_LEAD_SENDER_EMAIL', default='hello@briefy.co')

# Queues
MAIL_QUEUE = config('MAIL_QUEUE', default='mail-{}'.format(_queue_suffix))
NOTIFICATION_QUEUE = config('NOTIFICATION_QUEUE', default='notification-{}'.format(_queue_suffix))
