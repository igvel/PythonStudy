# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

# Templating
from string import Template
t = Template('${village}folk send $$10 to $cause.')
s = t.substitute(village='Nottingham', cause='the ditch fund')
s2 = t.safe_substitute(village='Dussel')
print s, s2


# Logging
import logging

logging.debug("Debug info!")
logging.info("INFO!")
logging.error("Bad error %d", -66)
