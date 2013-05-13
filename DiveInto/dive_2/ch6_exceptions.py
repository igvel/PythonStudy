__author__ = 'ielkin'

try:
    fsock = open("/none", "r")
except IOError:
    print "No such file!"


# Bind the name getpass to the appropriate function
def win_getpass():
    print "In Windows!"
    return "Windows password"

def default_getpass():
    print "Default!"
    return "password"

try:
    import termios, TERMIOS
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            getpass = default_getpass
        else:
            getpass = AskPassword
    else:
        getpass = win_getpass
else:
    getpass = unix_getpass

getpass()

# File operation safe
try:
    fsock = open(filename, "rb", 0)
    try:
        fsock.seek(-128, 2)
        tagdata = fsock.read(128)
    finally:
        fsock.close()
except NameError:
    pass
except IOError:
    pass

logfile = open('test.log', 'w')
logfile.write('test succeeded')
logfile.close()
print file('test.log').read()

logfile = open('test.log', 'a')
logfile.write('\nline 2')
logfile.close()
print file('test.log').read()
