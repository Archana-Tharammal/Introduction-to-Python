x = lambda a: a + 10
print(x(2))

y = lambda a, b: a * b
print(y(5, 2))


def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
print(mydoubler(10))


def myfunc(n):
    return lambda a: a + n
mydoubler = myfunc(5)
mytripler = myfunc(6)
print(mydoubler(10))
print(mytripler(10))
