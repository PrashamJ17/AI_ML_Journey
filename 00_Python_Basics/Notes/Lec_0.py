print("Hello, World")

name = input("What's your name ? ") # this takes input from the user . 
# The input function can take in argument as well that it prints before the user prompt . 

print("Hello,",name) # the variable isn't in double quotes " " . 
# when we add a ',' - a space is already added by default . 

print(123)
print("Hello, " + name + ". Nice to meet you") # the '+' , doesn't add space by default .

# print(*objects, sep=' ', end='\n')

# *objects - this is the input . 
# sep - separator - by default , a sep = ' ' 
# end - end of print() - be default, end = '\n'

print("Hello,",name,sep='-',end=' ')
print('Nice to meet you !')

# Escpae Sequence
# What if we want to print a quote 
# eg. print - He said "Hello"

print("P said , \"Do you know?\" ")

# f-string - if we want to use variables , just put an f before of first double quote of the string
print(f"Hey, {name}")

# string methods 

# 1.  .strip() --> removes white spaces (blank spaces), from the variable - from left or right 
name = name.strip() 
print(name)
# also sub methods -> .lstrip() , .rstrip() . 

# 2.  .upper() --> all letters of the string to upper case
# 3.  .lower() --> all letters of the string to lower case
# 4.  .title() --> first letter of the each word in the string is capital 
# 5.  .capitalize() --> first letter of the complete string is capital . 

print(name.capitalize()) 
print(name.title())

# 6.   .split() --> divides the string based on the seperator provided as arg in the func and converts the string into a list . 

print(name.split(" "))
# we can also assign the splitted halves of the string to different variables . 

first,last = name.split(" ")
print(first)
print(last)

x = input("What's x? ")
y = input("What's y? ")

# x , y are strings now as input default is string . 
# need to convert its type. 

z = x + y # this will concatenate strings . 
print(z)

print(int(x) + int(y))

print(round(19.5473,2))

# How to print no.s with a comma ? --> eg. 1,000,000 
# we have to use f-strings
print(f"{1000:,}")

# rounding a no. using f -strings , not using round fn .
print(f"{10.9999:.2f}")

# functions --> def 

def hello(): # doesn't take any input . 
    print("Hello")

hello()

def hello_name(to): # we have passed in a parameter 
    print(f"hello {to}")

hello_name(name)

def hello_default(to="World"): # we have passedin a default value to 'to' variable . 
    print(f"hello {to}") # if nothing is passed when a function is called then , it uses the default value of the variable

hello_default()
hello_default(name)

def main():
    x = int(input("Value of x : "))
    print(square(x))
def square(x):
    return x * x # we can also do x**2 or pow(x,2)


main()
