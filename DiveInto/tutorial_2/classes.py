# -*- coding: UTF-8 -*-
__author__ = 'ielkin'


#Old style class
class OldStyleClass:
    # class field
    a = 1

    # Constructor
    def __init__(self):
        pass

    def f(self):
        print NewStyleClass.a
        pass

x = OldStyleClass()


#New style class - derived from object
class NewStyleClass(object):
    # class field
    a = 1

    # Constructor
    def __init__(self):
        pass

    def f(self):
        print NewStyleClass.a
        pass

y = NewStyleClass()

# for old style class type() == 'instance'
print x.__class__
print type(x)
# for new style class __class__ == type()
print y.__class__
print type(y)

x.f()

# Dynamically creating instance var
x.counter = 1
print x.counter
# Removing instance var
del x.counter


print isinstance(x, OldStyleClass)
print issubclass(NewStyleClass, object)


# Class based iterator
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    # Special method to return iterator - object that implements next()
    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

for elem in Reverse("abc"): print elem


# Generator - tool for creating iterators  __iter__ and next() are created auto-magically
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

for elem in reverse("abc"): print elem

# Generator expression
print max(x*x for x in [2,4,6,1,2])