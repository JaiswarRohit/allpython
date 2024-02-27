from demo4 import *

def fun1():
    print("inside function 1")
    a()
    print("from fun1")


def fun2():
    s()
    print("from fun2")


def main():
    fun1()
    fun2()

main()