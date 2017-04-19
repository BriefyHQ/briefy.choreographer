"""Briefy Choreographer."""
from briefy import choreographer
from briefy.common.log import LOG_SERVER
from briefy.common.log import logstash
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
    from briefy.common.utils.transformers import json_dumps
    from logstash import formatter

    # custom json wrapper do serialize complex objects and monkey patch logstash.formater.json
    class CustomJSON:
        """Custom json wrapper."""

        @staticmethod
        def dumps(message):
            """Dump a message to json."""
            return json_dumps(message)

    formatter.json = CustomJSON


XMLConfig('configure.zcml', choreographer)()
