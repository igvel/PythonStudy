# -*- coding: UTF-8 -*-
import os
import sys
from ivel.test import hello

__author__ = 'ielkin'

c = 1
print c

a = [1]

print "Hello!" + str(a)

print os.path.splitext("aaa.111")[1]

print sys.argv

hello("Igor")