# NAMESPACES - DICTIONARY OF IDENTIFIERS AS KEYS AND THEIR VALUES AS KEY'S VALUES


# 4 scopes - LEGB 
# L - LOCAL
# E - enclosing
# G - global
# B - built-ins


# Local and Global Scope 
# Global Scope - all the variables of the main function - 

y=40
x = 30

def local(z) :
    global x
    print("x-",x)
    x = 19
    print("z",z)
    z = x + y
    print("x-",x)
    print("y-",y)
    print('z-',z)

print(y)
local(14)
print(y)


# Built-in Scope
import builtins
# print(dir(builtins))

L = [1,4,7,2,10]
print(max(L))

def max(L):
    print('Hello')

max(L)

# enclosing scope
# functions within functions 
# outer functions enclosing inner functions - are enclosing functions -
# when looing for a variable - LEGB rule - after local that is its own function , it looks for vairable in the outer function
# then the global and built in 

x = 100
def outer2():
    y = 11
    def outer() :
        nonlocal y 
        y += 2
        a = 50
        def inner():
            print(a)
            print(x)
            print(y)
        inner()
        print(x)
    outer()

outer2()
print(x)


# Decorators - 
# built in decorators - @classmethod , @staticmethod , etc 
# user defined - @dec_name -> applied on functions
# functions are first class citizens 

def my_deco(func) :
    def wrapper():
        print('* ' * 10)
        func()
        print('* '*10)
    return wrapper

def hello():
    print('hello')

a = my_deco(hello)
a()

# Better syntax - 

@my_deco
def display():
    print('What up!')

display()

import time 
def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print('Time taken by ',func.__name__,time.time() - start,'secs')

    return wrapper

@timer
def hello():
    for i in range(100):
        pass
    print('hello')

@timer
def square(num):
    time.sleep(4)
    print(num**2)

hello()
# square(3)


def check_type(typ):
    def outer_wrapper(func) :
        def wrapper(*args):
            for i in args :
                if type(i) == typ :
                    func(*args)
                else :
                    raise TypeError('Wrong Input Type !')
        return wrapper
    return outer_wrapper

@check_type(int)
def square(num):
    print(num**2)

@check_type(str)
def greet(name):
    print('hi',name)

square(5)
greet('prasham')

