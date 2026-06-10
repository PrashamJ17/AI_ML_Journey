#  Operators - 
# 	 - Arithmetic - + , - , * , / , // (int/floor division) (lower integer 5/2 = 2 (not 3))  , % (modulo (remainder)) , ** (exponential) 
# 	 - Relational - > , < , >= , <= , == , != 
# 	 - Logical - and , or , not 
# 	 - Bitwise - binary no.s -  bitwise and (&), bitwise or( | ) , bitwise xor(^) , bitwise not (~), left shift(>>) , right shift(<<)
# 	 - Assignment - = , used in conjunction with other operators
# 	 - Membership - in , not in 


# #bitwise - > works on binary no.s 
# # and
# print(2 & 3) 
# # or 
# print(2 | 3)
# #xor -> both same -> 0 , if different -> 1
# print(2^3)
# #bitwise not
# print(~3)
# #bitwise left
# print(2>>3)
# #bitwise right
# print(2<<3)

# print('D' in 'Delhi')

# to find the sum of 3 digit number by the user

def sum3():
    num = int(input("Enter a 3-digit number: "))
    sum = 0
    sum += num//100
    num = num%100
    sum += num//10
    num = num%10
    sum += num
    print(sum)
    
def min3():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if(a<b and a<c):
        print("Minimum =",a)
    elif(b<c):
        print("Minimum =",b)
    else:
        print("Minimum =",c)


# Menu-driven program
# for Atm

def menu_driven():
    menu = input('''
Welcome ! 
Enter 1 to view Balance
Enter 2 to change pin
Enter 3 to Withdraw
Enter 4 to deposit
Enter 5 to exit
''')
    if (menu == '1'):
        print("Balance")
    elif (menu == '2'):
        print("Change Pin")
    elif (menu == '3'):
        print("Withdraw")
    elif (menu == '4'):
        print("Deposit")
    elif (menu == '5'):
        print("Exit")
    else :
        print("Invalid !")

# Modules or libraries in python 
# header files 
# these are codes ,functions written by other programmers for us to use , help 

# import MODULE_NAME
# from MODULE import specific_fn / * --> * means everything

# modules like random , datetime , math , keywords are very important .
# help('modules') --> gives names of all the modules there are in python . 

# Loops
# while loop
# for loop . 

def while_loops():
    number = int(input("Enter the number: "))

    i = 1 
    while i<11 :
        print(number,"*",i,"=",number*i)
        i += 1

# Loops with else 
# We can also use else statements with loops 
# eg. - 

def while_else_loop():
    number = int(input("Enter the number: "))

    i = 1 
    while i<11 :
        print(number,"*",i,"=",number*i)
        i += 1
    else :
        print("i limit out of range = i>10")
# after the loop executes ,else statement executes . 

# Guessing game - 
def guess_game():
    import random as r # we don;t have to do random.fn_name 
    # we can use r instead of random

    num = r.randint(1,100) # this gives random integer values btwn a,b both included .
    chanes = 1
    guess = int(input("Guess the number between 1 to 100: "))
    while guess != num :
        if (guess < num):
            guess = int(input("Guess higher!\n"))
        else :
            guess = int(input("Guess lower!\n"))
        chanes += 1
    else:
        print("Yes! You got It RIGHT in",chanes,"guesses !")

# For loops
# eg - current pop = 10000
# population increases 10% every year
# print pop of lat 10 years 
def for_loop():
    cur_pop = 10000
    for i in range(2026,2016,-1):
        print(i,cur_pop)
        cur_pop = int(cur_pop - 0.1*cur_pop) 
        # since we have to print for the last 10 years , hence pop is decreasing when we go backwards .

for_loop()
