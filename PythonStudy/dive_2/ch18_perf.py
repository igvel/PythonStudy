# -*- coding: UTF-8 -*-
from dive_2.soundex import soundex1a

__author__ = 'ielkin'

# Time it
# import timeit
# t = timeit.Timer("soundex1a.soundex('Pilgrim')", "from dive_2.soundex import soundex1a")
# print t.timeit()
# print min(t.repeat(3, 1000000))

# Profile
import cProfile
cProfile.run("from dive_2.soundex import soundex1a; soundex1a.soundex('Pilgrim')")


# Trace
import trace

tr = trace.Trace()
tr.runfunc(soundex1a.soundex, 'Pilgrim')