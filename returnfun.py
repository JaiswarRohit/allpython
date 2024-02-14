def main(a, b):
    c = a + b
    d = a - b
    return c, d


x, y = main(5, 10)
print(f'Sum of a and b: , {x}')
print(f'subtraction of a and b: {y}')


def rohit(a, b):
    e = a + b
    f = a - b
    return e, f


p, q = rohit(54, 65)
print(f'Sum of a and b: , {p}')
print(f'subtraction of a and b: {q}')


def m3():
    print("Rohit")


def m4():
    print("Suman")
    m3()


m4()


def rohit():
    print("rohit")


def suman():
    print("Suman")
    rohit()


suman()


# Assign a function to a variable

def rohit1():
    print("we assign a function to a variable")


suman = rohit1
suman()


# Pass function as a parameter to another function

def display(x):
    print("This is display function")


def message():
    print("This is message function")


display(message())


def first():
    print("This is outer function")

    def second():
        print("this is inner function")

    second()



first()  # calling outer function

# function can return another function
def r1():
    def r2():
        print("function can return another function")
    return r2

x2 = first()

def r3(a, b):
    c = a+b    # a and b is formal argument
    print(c)

x5 = 10
y5 = 20
r3(x5,y5)   # x and y are actual arguments

