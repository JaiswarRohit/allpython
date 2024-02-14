''''# Local Variable
def f1():
    a = 10
    print("call f1", a)


def f2():
    b = 20
    print("call f2", b)


f1()
f2()

# Global Variable

c = 20
d = 10
def a():
    print(c, d)
def b():
    print(c, d)

a()
b()

p=10
def s():
    global d
    d = 20
    print(p, d)
def q():
    print(p, d)

s()
q()

# recursive
#Factorial using the recursive function in python

def factorial(n):
    if n == 0:
        return 1
    result= n * factorial(n -1)
    return result

x = factorial(int(input("Enter Your no: ")))
print(f'your Factorial is {x}')

def rohit():
    n = int(input("Enter Your factorail Number: "))
    fact = 1
    while n>0:
        fact = fact*n
        n=n-1
    print(f'factorial of the number is: {fact}')

rohit()

# lambda function

s = lambda a: a*a
x =s(int(input(f'Enter your number: ')))
print(x)

v = lambda a,b,c,d,e: a/b*c-d+e
y=v(4,5,6,7,6)
print(y)

# Filter in lambda function
item_cost = [99, 88, 65, 47, 84, 56]
get_above60 = filter(lambda x: x>60, item_cost)
x = list(get_above60)
print(x)


item_car = (1000, 3000, 4000, 7000, 8000, 700)
get_above1000 = filter(lambda y: y>999, item_car)
y = tuple(get_above1000)
print(y)

car = (85, 92, 12, 21, 65, 43)
get_outeven = filter(lambda q: q % 2 == 0, car)
get_outodd = filter(lambda a: a % 2 != 0, car)
q = list(get_outeven)
a = list(get_outodd)
print(q)
print(a)
# Filter in lambda function

#Map Function in python

b=[1000, 500, 6000, 7000, 8000]
with_gst = map(lambda p: p+(p*0.18), b)
p = tuple(with_gst)
print(b)
print(p)



# Reduce Function in python
from functools import reduce
no = [15, 64, 95, 85, 52, 63]
reducefunction = reduce(lambda e, f: e+f, no)
print(reducefunction)


def add(a, b):
    res = a+b
    return res
print(add(85, 65))
print(add(84, 65))



# Decorators in python
def decor(func):#Here ‘func’ is the the argument/parameter which receives the function
    def inner_function(x,y):
        if x<0:
            x=0
        if y<0:
            y=0
        return func(x,y)
    return inner_function

def add(a,b):
    res = a+b
    return res

add = decor(add)
print(add(55,-2))
print(add(-10, 55))
print(add(82, 2))


def decor(func):
    def inner_fun(x, y):
        if x<0:
            x=0
        if y<0:
            y=0
        return func(x,y)
    return inner_fun

@decor
def sum(a,b):
    res = a+b
    return res

print(sum(-45,6))
print(sum(-3,55))'''

# Generators in python

def m():
    yield 'rohit'
    yield 'suman'
    yield 'nitesh'
    yield 'omkar'
    yield 'nitin'
    yield 'nitesh'

g = m()
print(g)
for y in g:
    print(y)

def n(x, y):
    while x<=y:
        yield x
        x+=2

g = n(2,15)
for y in g:
    print(y)