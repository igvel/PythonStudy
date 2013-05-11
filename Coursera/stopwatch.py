
#Next, write a helper function format(t) that returns a string of the form A:BC.D where A, B, C and D are digits in the range 0-9. Test this function independent of your project. Note that the string returned by your helper function format should always correctly include leading zeros. For example
#format(0) == 0:00.0
#format(11) = 0:01.1
#format(321) = 0:32.1
#format(613) = 1:01.3
#Hint: Use integer division and remainder (modular arithmetic) to extract various digits for the formatted time from the global integer timer.

def format(t):
    tenths = t % 10
    seconds = t // 10
    minutes = seconds // 60
    seconds = seconds % 60
    #return str(minutes) + ":" + str(seconds).rjust(2, "0") + "." + str(tenths)
    return "%d:%02d.%d" % (minutes, seconds, tenths)

print format(0)
print format(11)
print format(321)
print format(5013)
