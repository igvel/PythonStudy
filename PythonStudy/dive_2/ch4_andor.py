__author__ = 'ielkin'

# And-or trick - like bool ? a: b in C
a = "first"
b = "second"
print 1 and a or b      # prints first - not safe if 'a' is false value
print (1 and [a] or [b])[0]  # prints first - safe
print (0 and [a] or [b])[0]  # prints second - safe
