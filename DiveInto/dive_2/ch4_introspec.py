import __builtin__
from apihelper import info
from dive_2 import statsout
import odbchelper


li = []
info(li)
#######################
# Built-in functions
#print 'Built-in functions'
#info(__builtin__)
# type
type(1)
# int

import types
type(1) == types.IntType
# True

# str - coerces to string
print str(1)
print str([1,2,3])
print str(odbchelper)
str(None)

# dir - returns a list of the attributes and methods of any object: modules, functions, strings, lists, dictionaries...
#dir(<var>)
#print dir(odbchelper)
# callable - takes any object and returns True if the object can be called, or False otherwise. Callable objects include functions, class methods, even classes themselves

# getattr - reference attribute by name at runtime
print li.pop
getattr(li, 'append')("Moe")
print li


def output(data, format="text"):
    output_function = getattr(statsout, "output_%s" % format, statsout.output_text)
    return output_function(data)

print output("Hello, World!")
print output("Hello, World!", "html")

# Filtering of lists
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print [elem for elem in li if len(elem) > 1]

methodList = [method for method in dir(object) if callable(getattr(object, method))]