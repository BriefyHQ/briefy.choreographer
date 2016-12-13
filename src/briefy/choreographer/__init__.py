"""Briefy Choreographer."""
from briefy import choreographer
from briefy.common.log import logstash
from briefy.common.log import LOG_SERVER
from zope.configuration.xmlconfig import XMLConfig

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

cs = logging.StreamHandler()
cs.setLevel(logging.INFO)

logger.addHandler(cs)

if LOG_SERVER:
    log_handler = logstash.LogstashHandler(
        LOG_SERVER, 5543, version=1, tags=['Worker', 'briefy.choreographer']
    )
    logger.addHandler(log_handler)

XMLConfig('configure.zcml', choreographer)()
