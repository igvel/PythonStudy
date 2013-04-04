from dive.samples import fileinfo

__author__ = 'ielkin'


# Simplest class possible
class Simple:
    pass

# Inheritance
from UserDict import UserDict


class FileInfo(UserDict):
    # Initialization - like constructor
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename

    def someMethod(self, name):
        print 'Hello, ', name, '!'


#Multiple inhertiance
class A:
    pass


class B:
    pass


class C(A, B):
    pass

if __name__ == "__main__":
    f = fileinfo.FileInfo("/IVEL/Music/Salsa/Grupo Latin Vibe - La llave.mp3")
    print f.__class__


