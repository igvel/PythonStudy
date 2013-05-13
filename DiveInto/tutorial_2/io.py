# -*- coding: UTF-8 -*-
import sys

__author__ = 'ielkin'

# Auto-closing
with open('c:/temp/workfile', 'w+') as f:
    f.write('0123456789')
    # from the beginning
    f.seek(3)
    print f.read(1)
    # seek from the end
    f.seek(-2, 2)
    print f.read(1)

# Serialization in Python called pickling
import pickle

with open('c:/temp/pickler', 'w+b') as f:
    x = {"x": 1, "y": 2}
    pickle.dump(x, f)

with open('c:/temp/pickler', 'rb') as f:
    y = pickle.load(f)
    print y

# Exception with args
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print sys.exc_info() # last exception information tuple
    print type(inst)     # the exception instance
    print inst.args      # arguments stored in .args
    print inst           # __str__ allows args to printed directly
    x, y = inst          # __getitem__ allows args to be unpacked directly
    print 'x =', x
    print 'y =', y
    #raise               # Without params - rethrows exception