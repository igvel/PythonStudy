# -*- coding: UTF-8 -*-
from dive.soundex import soundex1a

__author__ = 'ielkin'


import timeit
t = timeit.Timer("soundex1a.soundex('Pilgrim')", "from dive.soundex import soundex1a")
print t.timeit()
print min(t.repeat(3, 1000000))