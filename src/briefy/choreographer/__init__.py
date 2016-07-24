"""Briefy Choreographer."""
from briefy import choreographer
from zope.configuration.xmlconfig import XMLConfig

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

cs = logging.StreamHandler()
cs.setLevel(logging.INFO)

logger.addHandler(cs)

XMLConfig('configure.zcml', choreographer)()
