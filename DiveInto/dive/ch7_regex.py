__author__ = 'ielkin'

import re

s = '100 NORTH BROAD ROAD'
print re.sub('ROAD$', 'RD.', s)

s = '100 BROAD ROAD APT. 3'
print re.sub(r'\bROAD\b', 'RD.', s)

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'

match = re.search(pattern, 'MMMCC')
#print [el for el in dir(match) if not el.startswith('__')]

# Roman number up to thousands
pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print re.search(pattern, 'MCLXVII')

# Verbose variant
pattern = """
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """
print re.search(pattern, 'MCMLXXXIX', re.VERBOSE)

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print phonePattern.search('800-555-1212').groups()

phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)

print phonePattern.search('work 1-(800) 555.1212 #1234').groups()