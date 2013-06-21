# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

# Root class
class A(object):
    def method(self):
        print "A"

# Cooperative classes B and C
class B(A):
    def method(self):
        super(B, self).method()
        print "B"

class C(A):
    def method(self):
        super(C, self).method()
        print "C"

# Uncooperative class
class E(object):
    def method(self):
        print "E"


# Here when calling D.method the call chain will be D->B->C->A
class D(B, C, E):
    def method(self):
        super(D, self).method()
        print "D"

D().method()
print D.__mro__


# Example of cooperative classes from Standard lib
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first seen'
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__,
                           OrderedDict(self))
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

oc = OrderedCounter('abracadabra')
for key, value in oc.items():
    print key, value