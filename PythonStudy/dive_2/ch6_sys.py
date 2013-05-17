import glob
import os
from dive_2.samples.fileinfo import MP3FileInfo

__author__ = 'ielkin'

# Print all modules
import sys
print '\n'.join(sys.modules.keys())

# Module of the class
print MP3FileInfo.__module__
print sys.modules[MP3FileInfo.__module__]

print os.path.join(os.path.expanduser("~"), "Python")

