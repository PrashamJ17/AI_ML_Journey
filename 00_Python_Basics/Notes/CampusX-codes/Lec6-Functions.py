def is_even(num):
    '''
    This functions checks if the input no. is even or odd
    input - any valid integer
    output - even or odd 
    created on - 21st June 
    created by - Prasham Jain
    '''

    if type(num) != int :
        return 'Wrong Input'
    if num%2 == 0 :
        return 'even'
    else :
        return 'odd'

def sum(b=1,a=10):
    print(a+b)

def multiply(*args):
    product = 1
    for i in args :
        product *= i
    print(args)
    return product

def display(**kwargs):
    for(key,value) in kwargs.items():
        print(key,"->",value)

def main():
    # for i in range(1,11):
    #     x = is_even(i)
    #     print(x)
    # print(is_even('hi'))

    # sum(a=7,b=11)
    # print(multiply(1,2,4,5,3,42))
    display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad')


def g(y):
    print(x)
def h(y):
    global x
    print(x)
    x = x+1
    

# x = 5
# g(x)
# h(x)
# g(x)
# print(x)


def f():
    def s():
        print('Inside function - s')
    s()
    # f()
    print('Inside function - f')

def t(x):
    def h(x):
        print(x)
        x = x+1
        return x
    x=x+1
    print(h(x))
    return x
x=3
print(t(x))
print(x)

def square(num):
    return num**2
fn = square
print(type(square))
print(type(fn))
print(fn(4))

def f1():
    def f2(a,b):
        return a + b
    return f2
print(f1()(10,40))

def f4():
    print('this is f4')
def f3(z):
    print('this is f3')
    return z()



a = lambda a,b : a+b
print(a(3,5))





