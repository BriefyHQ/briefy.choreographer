"""Briefy Choreographer."""
from briefy import choreographer
from zope.configuration.xmlconfig import XMLConfig

import logging

logger = logging.getLogger(__name__)

XMLConfig('configure.zcml', choreographer)()
