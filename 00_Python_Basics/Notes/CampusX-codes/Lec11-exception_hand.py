# EXCEPTION HANDLING

# if things go wrong during the execution of the program(during runtime)
# It generally happens when something unforseen has happened 

# Exception handling - try , exept block

# what if file doesn't exist ?
try :
    with open('sample.txt','r') as f :
        print(f.read())
except :
    print('File not found !')

# there can be any other error 

try :
    m=10
    f = open('sample-1.txt','r')
    print(f.read())
    print(m)
except :
    print('Some error occured') # this will print any time error occurs , any error

# Its good practice to show what error has occured, rather than some general line 
# Tell user , what's wrong and why ?
# How to catch specific error and exceptions ? -  write multiple except blocks 

try :
    # write you code here -
    f = open('sample-1.txt','r')
    print(f.read())
    print(m)
except Exception as e:
    print(e) # this will print the error . 
    print(e.with_traceback) # this will give the error name/class
# this is how you can catch the error

# But this is a general way of showing error 
# you should write except block for specific errors that may occur in the code
# and a general exept block at the end , for any other error that you may not think of ,

try :
    m = 10
    f = open('sample-1.txt','r')
    print(f.read())
    print(m)
    print(5/0)
    L = [1,2]
    print(L[100])
except FileNotFoundError :
    print('File Not Found')
except NameError :
    print('Variable Name not defined')
except ZeroDivisionError:
    print('Cannot Divdie by 0')
except Exception as e : # this h=should always be at the end or else this will run first instead of specific except blocks
    print(e)

# The code will stop at which ever error occurs first
# If no error - then all good 


# you can use else as well - try-except-else 
# in try you write unsure code - where you think error will occur 
# in except you handle those errors
# in else - ypu write code that runs after try - this code is a sure, perfect code that will not give any error
# else runs when try runs successfully with no errors 

# so basically , try runs -> if no error -> else runs , or if error -> except runs

# this is same as try-except , but for more readabilityand structure , use else 

try :
    f = open('sample-1.txt','r')
except FileNotFoundError :
    print('File not found')
except Exception as e :
    print(e)
else : # perfect , sure code with no error is written here , that runs after try 
    print(f.read())


# finally block - this will always run irrespective of except , else , whatever .
# what comes here - if ther is anything - like any connection - database , bluetooth , authentication , etc - you will close them here
# finally block will always run after everything, so all the things that should happen at the end, if someone closing an app , or anything , and you want to end things ,then end here


try :
    f = open('sample.txt','r')
except FileNotFoundError :
    print('File not found')
except Exception as e :
    print(e)
else : # perfect , sure code with no error is written here , that runs after try 
    print(f.read())

finally : # always run irrespective of error or success
    print('Always Runs')


# Raise Exception - you can yourself raise any error 

print('hi')
# raise NameError('Trying raise error ')

class Bank :
    def __init__(self,balance):
        self.balance = balance
    
    def withdraw(self,amount):
        if amount < 0 :
            raise Exception('Amount cannot be negative')
        if self.balance < amount :
            raise Exception('Balance Not enough')
        
        self.balance -= amount

b1 = Bank(10000)

try :
    b1.withdraw(15000)
except Exception as e :
    print(e)
else :
    print(b1.balance)


# Creating Custom Error - 
class SecurityError(Exception) :
    def __init__(self,mssg) :
        print(mssg)
    
    def logout(self):
        print('Logout')
        

class Google :
    def __init__(self,name,email,pswd,device) :
        self.name = name
        self.email = email
        self.pswd = pswd
        self.device = device
    
    def login(self,email,pswd,device):
        if device != self.device :
            raise SecurityError('New Device Login')
        if email == self.email and pswd == self.pswd :
            print('Welcome')
        else:
            print('Login Error')


obj = Google('prasham','prasham@gmail.com',123,'IOS')
try :
    obj.login('prasham@gmail.com',123,'Android')
except SecurityError as e :
    e.logout()
else :
    print(obj.name)
finally :
    print('Database Connection Closed')
