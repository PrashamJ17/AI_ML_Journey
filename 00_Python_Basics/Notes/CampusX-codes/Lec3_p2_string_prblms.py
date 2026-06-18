# length of the given string without using length function

def q1():
    string = input("ENTER A STRING: ")
    count = 0
    for i in string:
        count += 1
    print(count)

# Extract username from a given email.
# Eg if the email is nitish24singh@gmail.com
# then the username should be nitish24singh
def q2():
    email = input("Enter email: ")

    pos = email.index('@')
    print("username: ",email[:pos])


# Count the frequency of a particular character in a provided string.
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

def q3():
    string = input("Enter the string: ")
    character = input("Enter character: ")

    print("frequency:",string.count(character))

# program to remove a particular character from a string 
def q4():
    string = input("Enter the string: ")
    character = input("Enter character: ")
    l1 = string.split(character)
    print("".join(l1))    

# string is palindrome or not
def q5():
    string = input("Enter the string: ")
    if string == string[::-1]:
        print("Palindrome")
    else :
        print("Not palindrome")

# Write a program to count the no. of words in a string without split 
def q6():
    string = input("Enter the string: ")
    count = 0
    for i in string:
        if i == " ":
            count += 1
    count +=1
    print(count)

# convert string to title case without using title()
def q7():
    string = input("Enter the string: ")
    l1 = string.split()
    l2 = []
    for i in l1:
        l2.append(i.capitalize())
    print(" ".join(l2))

# program to convert an integer to a string
def q8():
    integer = int(input("Enter integer: "))
    num = '0123456789'
    result = ""
    while integer != 0:
        result += num[integer%10]
        integer = integer // 10
    result = result[::-1]
    print(result)
    print(type(result))

