# Program - The current population of a town is 10000. 
# The population of the town is increasing at the rate of 
# 10% per year. You have to write a program to find out 
# the population at the end of each of the last 10 years.

# logic - 
# if 10000 - 10th year , x in 9th year , x + 0.1x = 100000

def q1():
    cur_pop = 10000
    for i in range(2026,2016,-1):
        print("population in the year",i,"- ",cur_pop)
        cur_pop = cur_pop/1.1

# Sequence sum
# 1/1! + 2/2! + 3/3! + ...

def fact(n):
    ans = 1
    if n == 0 or n == 1 :
        return ans
    else:    
        for i in range(1,n+1):
            ans *= i
    return ans

def q2():
    n = int(input("Enter the range: "))
    sum = 0
    for i in range(1,n+1):
        sum += i/fact(i)
    print(sum)


# Nested Loops
# Pattern Printing Problems 

# *
# **
# ***
def patt1():
    n = int(input("Enter no. of rows: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end = " ")
        print()

# 1
# 121
# 12321
# 1234321

def patt2():
    n = int(input("Enter no. of rows: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i,1,-1):
            print(j-1,end = " ")
        print()


# Break , continue , pass 
# printing prime no.s between a given range - using break . 
def prime():
    s = int(input("Enter starting no. : "))
    e = int(input("Enter ending no. : "))
    for i in range(s,e+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else :
            print(i,"is Prime")



# Strings 

# Creating strings 
s1 = ""
s2 = 'yes'
s3 = '''
HI yo what
up'''
s4 = str()

# Indexing in strings
print(s3[-1])
# Slicing 
print(s3[::-1]) # this reverses the string

# deletion
del s1 #t this deletes the variable 

# operators 
print(s3+s2)
print(s3*2)

if("orld"): # empty string - False if string is not empty then True
    print("Okay")
if not(""):
    print("yes")

if "m" > "M": # depends on ascii values
    print("HA")
if 'D' in 'Delhi':
    print('Okayy')

# String Functions 

print(len(s3))
print(max(s3)) # this is based on the ascii values 
print(min(s3))

print(sorted(s3)) # the sorted fn , returns a list of sorted elements , by default - ascending order
print(sorted(s3,reverse=True)) # reverse = True -> prints list in descending order

print(s3.split()) # by default " " -> seperator
print(s3.split("\n"))

l1 = sorted(s3)
print(" ".join(l1)) 

print(s2.replace('ye','a'))

