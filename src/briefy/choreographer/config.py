"""Briefy Choreographer config."""
from briefy.common.config import _queue_suffix
from prettyconf import config


# Queues
MAIL_QUEUE = config('MAIL_QUEUE', default='mail-{}'.format(_queue_suffix))
