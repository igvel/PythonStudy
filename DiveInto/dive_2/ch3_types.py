__author__ = 'ielkin'

######################
# Dictionaries
d = {"server": "localhost", "db": "master"}

d["uid"] = "uid"
d["id"] = 3
d[5] = "ivel"
del d["db"]

# List of keys
print d.keys()
# List of values
print d.values()
# List of tuples
print d.items()

if "id" in d: print "In Dictionary!"

d.clear()
print d

# list of tuples per list
zip([1,2,3],[2,5,3,5],[4,5])
#[(1, 2, 4), (2, 5, 5)]

# build dictionary from list
given = ['John', 'Eric', 'Terry', 'Michael']
family = ['Cleese', 'Idle', 'Gilliam', 'Palin']
pythons = dict(zip(given, family))

######################
# Lists
li = ["a", "b", "mpilgrim", "z", "example"]
li[0]
li[4]
# from the end li[-n] == li[len(li) - n]. So in this list, li[-3] == li[5 - 3] == li[2].
li[-1]

# Slicing
li[1:3]
li[1:-1]
li[3:]
li[:3]
# Complete copy of the list
li[:]

# Adding
li.append("new")
li.insert(2, "new")
li.extend(["two", "elements"])
print li

#Searching
li.index("new")
# Check if in list - returns True or False
"two" in li

#Deleting
li.remove("new")
# Removes last and returns value
li.pop()

# Operators
li = li + ["1", 2];
# Works like li.extend([])
li += ['two']
# Repeater -> [1, 2, 1, 2, 1, 2]
li = [1, 2] * 3

##################################
# Tuples
t = ("a", "b", "mpilgrim", "z", "example")
#('a', 'b', 'mpilgrim', 'z', 'example')
t[0]
#'a'
t[-1]
#'example'
t[1:3]
#('b', 'mpilgrim')
"z" in t

# Conversion between list and tuple
tuple(li)
list(t)

#######################################
# Variables
x = 1
# Multiple assignments
(x, y, z) = (1, 2, 3)
# Consequtive values assignment
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)

#######################################
# List comprehension
li = [1, 9, 8, 4]
li = [elem*2 for elem in li]
li
#[2, 18, 16, 8]

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
[k for k, v in params.items()]
#['server', 'uid', 'database', 'pwd']
[v for k, v in params.items()]
#['mpilgrim', 'sa', 'master', 'secret']
["%s=%s" % (k, v) for k, v in params.items()]
#['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']