# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

# Sets
# comprehensions
print {x for x in 'abracadabra' if x not in 'abc'}
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit
print 'orange' in fruit

a = set('abracadabra')
b = set('alacazam')

print a - b
print a | b
print a & b
print a ^ b

# Dictionaries
# construct from key-value pairs
print dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# from comprehensions
print {x: x**2 for x in (2, 4, 6)}
# like function params
d = dict(sape=4139, guido=4127, jack=4098)
print d
# Unpacking  dictionary
x, y, z = d
print x, y, z

# Looping with index are done with enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

# To change sequence while iterating first make a copy
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print words

t = ('cat', 'window', 'defenestrate')
t2 = t[:]
print t, t2
# Unpacking list
x, y, z = t
print x, y, z

# String conversion and evaluation
l = (1,2,3)
print l
s = `l`
s2 = repr(l)
print s, s2
l2 = eval(s)
print l2

def main():
    print 'Test!'

if __name__ == '__main__':
    main()
