import os

__author__ = 'ielkin'

# Prints list elems
li = ['a', 'b', 'e']
for s in li:
    print s

# Does the same
print "\n".join(li)

# iteration over range - use rarely!
for i in range(5):
    print i

# Basic like list iteration - DON'T DO THIS!
li = ['a', 'b', 'c', 'd', 'e']
for i in range(len(li)):
    print li[i]

print "\n".join(["%s=%s" % (k, v) for k, v in os.environ.items()])

