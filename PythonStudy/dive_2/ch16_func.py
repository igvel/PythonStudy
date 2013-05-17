# -*- coding: UTF-8 -*-
import sys

__author__ = 'ielkin'

import os
# Full path of where script is located
print os.path.abspath(os.path.dirname(sys.argv[0]))

# Filter list
def odd(n):
    return n % 2

li = [1, 2, 3, 5, 9, 10, 256, -3]

# Option 1
print filter(odd, li)
#[1, 3, 5, 9, -3]

# Option 2
print [e for e in li if odd(e)]

# Option 3
filteredList = []
for n in li:
    if odd(n):
        filteredList.append(n)
print filteredList

# Map list
def double(n):
    return n*2

li = [1, 2, 3, 5, 9, 10, 256, -3]
# Option 1
print map(double, li)
#[2, 4, 6, 10, 18, 20, 512, -6]

# Option 2
print [double(n) for n in li]

# Option 3
newlist = []
for n in li:
    newlist.append(double(n))
print newlist

# Depends on type - different result
li = [5, 'a', (2, 'b')]
print map(double, li)
#[10, 'aa', (2, 'b', 2, 'b')]

moduleNames = ['sys', 'os', 're', 'unittest']
modules = map(__import__, moduleNames)
print modules