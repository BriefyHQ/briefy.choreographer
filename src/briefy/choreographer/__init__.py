"""Briefy Choreographer."""
from briefy import choreographer
from briefy.common.log import log_handler
from zope.configuration.xmlconfig import XMLConfig

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

cs = logging.StreamHandler()
cs.setLevel(logging.INFO)

logger.addHandler(cs)

if log_handler:
    logger.addHandler(log_handler)

XMLConfig('configure.zcml', choreographer)()
