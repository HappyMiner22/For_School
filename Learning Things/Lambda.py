'''x = lambda a, b : a * b
print(x(5, 6))'''

'''x = lambda a, b, c : a ** b + c

print(x(3, 3, 10))

y = lambda a, b, c : '''

'''def myfunc(n):
  return lambda a : a * n

print(myfunc(3))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))'''

'''def myfunc(n
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)):
myquadrapler = myfunc(4)

print(mydoubler(11))
print(mytripler(11))
print(myquadrapler(11))'''
'''
a = 5

def myfunc():
    g = a + 10
    return print(g)
if True:
    myfunc()'''

def sum(n):
    if n == 1:
        return 1
    else:
        sum(n-1) + n

print(sum(10))