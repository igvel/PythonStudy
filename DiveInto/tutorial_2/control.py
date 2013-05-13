# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

# Else in for
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'

# Function with variable params and keywords
def f(a, *args, **kwords):
    print a
    for i in args:
        print i,

f(1, 2, 3, 4, key1=1, key2=2)

# Unpacking lists or dicts
args = [3, 6]
print range(*args)            # call with arguments unpacked from a list
#[3, 4, 5]

def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print parrot(**d)

