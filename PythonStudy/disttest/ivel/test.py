# -*- coding: UTF-8 -*-
"""Test module"""

# imports
import sys
# constants
__author__ = 'ielkin'
# exception classes
# interface functions
# classes
# internal functions & classes


def hello(name):
    print "Hello,", name

def main(argv):
    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)