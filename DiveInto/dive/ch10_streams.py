# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

# Standard
import sys

sys.stdout.write('Hello!')
sys.stderr.write('Hello!')
print('Hello!')

# Redirect
print 'Dive in'
saveout = sys.stdout
fsock = open('out.log', 'w')
sys.stdout = fsock
print 'This message will be logged instead of displayed'
sys.stdout = saveout
fsock.close()

# Shortcut redirect
print >> sys.stderr, "Error!"

for arg in sys.argv: print arg