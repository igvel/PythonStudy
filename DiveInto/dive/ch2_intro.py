import odbchelper

params = {"server":"ivel", "database":"master", "uid":"sa", "pwd":"secret"}

print odbchelper.buildConnectionString(params)
print odbchelper.buildConnectionString.__doc__


def fib(n):
    """ Prints Fibbonacci """
    print 'n =', n
    if n > 1:
        return n * fib(n - 1)
    else:
        print 'end of the line'
        return 1

# Testing code - runs only if module is called directly else __name__ will be equal to module name
if __name__ == "__main__":
    fib(10)