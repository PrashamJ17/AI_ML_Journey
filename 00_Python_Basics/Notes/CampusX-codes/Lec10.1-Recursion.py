# Recursion 

# This is iteration solution - 
def mul(a,b) :
    res = 0
    for i in range(0,b):
        res += a
    print(res)

mul(3,4)

# This is recursive function 

def mul_rec(a,b):
    if b == 1 :
        return a
    else:
        return a + mul_rec(a,b-1)

print(mul_rec(5,6))

def fact(a):
    if a == 0 or a == 1 :
        return 1
    else :
        return a * fact(a-1)
print(fact(5))

def palindrome(a):
    if len(a) <= 1 :
        return'palindrome'
    else :
        if a[0] == a[-1]:
            return palindrome(a[1:-1])
        else :
            return'no pal'
    
print(palindrome('abaa'))

# rabbit problem == fibonacci series
def rabbit_prb(month):
    if month == 0 or month == 1:
        return 1
    else :
        return rabbit_prb(month - 1) + rabbit_prb(month -2)
    
print(rabbit_prb(12))

# months - jan , feb , march , aprl , may , june , july , august , 
# rabbits - 1 , 2 , 3 , 5 , 8 , 13 , ....
# so lets say they are starting from 1 pair of rabbits ->  1 , 1 , 2, 3, 5, 8, 13 , and so on
# thus add - previous 2 no.s to get third no. 

# base case - total months -> 0 or 1 -> rabbits -> 1
# else -> after 1 months -> rabits -> sum of last 2 

# lets say total months = 5 
# month = 5 -> go to else -> return (4) + return(3)
# month = 4 -> for to else -> return(3) + return (2)
# month = 3 -> go to else -> return(2) + return(1)
# month = 2 -> fo to else -> return(1) + return)(0)
# month = 1 -> go to if -> return 1 
# month = 0 -> go to if -> return 1
# then back track .
# so total rabbits -> 8 


# solving rabbit problem using memoization -
def memo_rab(m,d):
    if m in d :
        return d[m]
    else :
        d[m] =  memo_rab(m-1,d) + memo_rab(m-2,d)
        return d[m]

d = {0:1,1:1}
print(memo_rab(56,d))