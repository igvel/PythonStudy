__author__ = 'ielkin'

# String formatting in Python uses the same syntax as the sprintf function in C.
k = "uid"
v = "sa"
"%s=%s" % (k, v)
#'uid=sa'

userCount = 6
print "Users connected: %d" % (userCount, )
#Users connected: 6

print "Change since yesterday: %+.2f" % 1.5
#+1.50

# Join/Split
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
["%s=%s" % (k, v) for k, v in params.items()]
#['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(["%s=%s" % (k, v) for k, v in params.items()])
#'server=mpilgrim;uid=sa;database=master;pwd=secret'

s.split(";")
#['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s.split(";", 1)
#['server=mpilgrim', 'uid=sa;database=master;pwd=secret']