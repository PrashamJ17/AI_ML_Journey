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

# 1. Strip . 
name = name.strip() 









