# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

import string, re

allChar = string.uppercase + string.lowercase
charToSoundex = string.maketrans(allChar, "91239129922455912623919292" * 2)

def soundex(source):
    if (not source) and (not source.isalpha()):
        return "0000"
    digits = source[0].upper() + source[1:].translate(charToSoundex)
    digits2 = digits[0]
    for d in digits[1:]:
        if digits2[-1] != d:
            digits2 += d
    # digits3 = re.sub('9', '', digits2)
    # while len(digits3) < 4:
    #     digits3 += "0"
    # return digits3[:4]
    return (digits2.replace('9', '') + '000')[:4]

if __name__ == '__main__':
    from timeit import Timer
    names = ('Woo', 'Pilgrim', 'Flingjingwaller')
    for name in names:
        statement = "soundex('%s')" % name
        t = Timer(statement, "from __main__ import soundex")
        print name.ljust(15), soundex(name), min(t.repeat())