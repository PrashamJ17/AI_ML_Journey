# Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

def q1():
    n = int(input("Enter no of rows: "))
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

# Problem 2: Print the following pattern.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def q2():
    n = int(input("Enter no of rows: "))
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print()


# Problem 3:Write a program to pring the following pattern
#     *
#   * * *
# * * * * *

def q3():
    n = int(input("Enter no. of rows: "))
    sp = n - 1
    for i in range(n):
        for k in range(sp,0,-1):
            print(" ",end=" ")
        sp -= 1
        for j in range(2*i + 1):
            print("*",end=" ")
        print() 


# Problem 4:Write a program to print the following pattern
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

def q4():
    n = int(input("Enter no. of rows: "))
    for i in range(1,n+1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()


# Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

def q5():
    n = int(input("Enter value of n: "))
    x = int(input("Enter value of x: "))
    sum = 1
    s=""
    print("1 ",end="")
    for i in range(2,n+1):
        s += "+ x^{0}/{0} ".format(i)
        sum += (x**i)/i
    print(s)
    print(sum)


# Problem 6: The natural logarithm can be approximated by the following series.
# temp.jpg
# ln(x) = (x-1)/x + 1/2 * ((x-1)/x)**2 + 1/3 • ((x-1)/x)3 + 1/4 • ((x-1)/x)*+ ...

# If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.

def q6():
    n = int(input("Enter value of n: "))
    x = int(input("Enter value of x: "))
    a = (x-1) / x
    sum = 0
    print("ln(x) = ",end=" ")
    s = ""
    for i in range(1,n+1):
        s += "1/{0} * ((x-1)/x)**{0} + ".format(i)
        sum += 1/i * (a**i)
    print(s[:-2])
    print(sum)

# Problem 7 - Find the sum of the series upto n terms.
# Write a program to calculate the sum of series up to n term. For example, 
# if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. 
# Take the user input and then calculate. And the output style should match which is given in the example.

# Example 1:

# Input:
# 5
# Output:
# 2+22+222+2222+22222
# Sum of above series is: 24690

def q7():
    n = int(input("Enter value of n: "))
    sum = 0
    s = ''
    for i in range(1,n+1):
        sum += int("2"*i)
        a = "2" * i
        s += f"{a} + "
    print(s[:-2])
    print(sum)

# Problem 8: Write a program to print all the unique combinations of 1,2,3 and 4
# Output:

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# .
# .
# and so on

def q8():
    for i in range(1,5):
        for j in range(1,5):
            if j == i :
                continue
            for k in range(1,5):
                if k == j or k == i:
                    continue
                for l in range(1,5):
                    if l == k or l == j or l == i:
                        continue
                    print(i,j,k,l)

# Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the number
def q9():
    num = int(input("Enter the decimal no : "))
    bin = ''
    if num == 0 :
        bin += '0'
    else: 
        while num != 1:
            bin += str(num%2)
            num //= 2
        bin += '1'
    print(bin[::-1])


# Problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers

def q10():
    a = int(input("Enter first no. : "))
    b = int(input("Enter second no. : "))

    s = min(a,b)
    ma = 0
    for i in range(1,s+1):
        if a%i == b%i == 0 :
            if ma < i :
                ma = i
    print("HCF of {} and {} = {}".format(a,b,ma))

    m = max(a,b)
    i = 1
    lcm = 0
    while True:
        if (m*i)%s == 0:
            lcm = m*i
            break
        else:
            i += 1
    print("LCM of {} and {} = {}".format(a,b,lcm))


# Problem 11: Create Short Form from initial character
# Given a string create short form ofthe string from Initial character. Short form should be capitalised.

# Example:

# Input:

# Data science mentorship program
# Output:

# DSMP

def q11():
    string = input("Enter the string: ")
    li = string.split()
    short = ''
    for i in li:
        short += i[0].upper()
    print(short)


# Problem 12: Append second string in the middle of first string
# Input:
# campusx
# data
# Output:

# camdatapusx

def q12():
    st1 = input("Enter first string: ")
    st2 = input("Enter second string: ")
    s = st1[:len(st1)//2] + st2 + st1[len(st1)//2:]
    print(s)

# Problem 13:Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given:

# str1 = PyNaTive
# Expected Output:
# yaivePNT

def q13():
    string = input("Enter the string: ")
    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    high = ''
    low = ''
    for i in string:
        if i in cap:
            high += i
        else :
            low += i
    print(low+high)


# Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
# Input:

# hel123O4every093

# Output:

# Sum: 22
# Avg: 2.75

def q14():
    string = input("Enter the string: ")
    sum = 0
    n = 0
    for i in string:
        if i in '0123456789':
            sum += int(i)
            n+=1
    print("sum = {} and avg = {}".format(sum,sum/n))



# Problem 15: Removal of all characters from a string except integers
# Given:

# str1 = 'I am 25 years and 10 months old'
# Expected Output:

# 2510

def q15():
    string = input("Enter a string: ")
    num = '0123456789'
    s = ''
    for i in  string:
        if(i in num):
            s += i
    print(s)

# Problem 16: Check whether the string is Symmetrical.
# Statement: Given a string. the task is to check if the string is symmetrical or not. 
# A string is said to be symmetrical if both the halves of the string are the same.

# Example 1:

# Input

# khokho
# Output
# The entered string is symmetrical

def q16():
    string = input("Enter a string: ")
    if(len(string)%2 == 1):
        print("Not symmetrical- odd no. of string")
        return 1
    p1 = string[:len(string)//2]
    p2 = string[len(string)//2:]
    if(p1 == p2):
        print("Symmetrical")
    else :
        print("Not symetrical")


# Problem 17: Reverse words in a given String
# Statement: We are given a string and we need to reverse words of a given string.

# Example 1:

# Input:
# geeks quiz practice code
# Output:
# code practice quiz geeks
# Example 2:

# Input:
# my name is laxmi
# Output:
# laxmi is name my

def q17():
    string = input("Enter a string: ")
    l1 = string.split(" ")
    l1.reverse() # when writing l1 = l1.reverse -> it overwrites l1 by None . 
    rev_s = " ".join(l1)
    print(rev_s)


# Problem 18: Find uncommon words from two Strings.
# Statement: Given two sentences as strings A and B. The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.

# Example 1:

# Input:

# A = "apple banana mango" 
# B = "banana fruits mango"
# Output:

# ['apple', 'fruits']

def q18():
    A = input("Enter string A: ").split()
    B = input("Enter string B: ").split()
    uncommon = []
    for i in A:
        if i not in B :
            uncommon.append(i)
    for i in B:
        if i not in A:
            if i not in uncommon :
                uncommon.append(i)
    print(uncommon)

# Problem 19: Word location in String.
# Statement: Find a location of a word in a given sentence.
# Example 1:

# Input:
# Sentence: We can learn data science through campusx mentorship program.

# word: campusx
# Output:
# Location of the word is 7.
# Note- Don't use index/find functions
def q19():
    string = input("Enter a string: ").split()
    word = input("Enter word to find: ")

    for i in range(len(string)):
        if string[i] == word :
            break
    
    print("Location of",word,"is",i+1)


# [ ]
# Code here
# Problem 20: Write a program that can remove all the duplicate characters from a string. User will provide the input.

def q20():
    string = input("Enter a string: ").split()
    words = []
    for i in string :
        if i in words:
            continue 
        else:
            words.append(i)
    
    print(" ".join(words))

