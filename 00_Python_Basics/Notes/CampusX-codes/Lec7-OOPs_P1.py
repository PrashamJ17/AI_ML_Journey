'''
- We are creating a class for an atm machine . 
- 2 things - data , functions
- data for atm -> pin , balance
- functions -> withdraw , change pin, set pin , check balance , exit
'''

#intra class communication done by using self(as an obj)
# Rule -> Only an ibject of the class can c=use class data and call its methods -> self.data or self.methods()
class Atm:
    # __init__(self) -> special function called -> 
    # Constructor -> it executes by default whenever 
    # an object is created
    def __init__(self): # self parameter replaced by the object created 
         # initially when obj is created , it will have 
         # following data with default values - 
        # print(id(self))
        self.pin = ''
        self.balance = 0
        self.menu() 
        # whenever an object is created , 
        # the menu function will be called as it is called 
        # from within the constructor
    
    def menu(self):
        menu = input('''
        Hi how can I help you ?
        1. Press 1 to set Pin
        2. Press 2 to change Pin
        3. Press 3 to check Balance
        4. Press 4 to withdraw money
        5. Press 5 to exit

        ''')
        if menu == '1':
            #create pin
            self.create_pin()
        elif menu == '2':
            #change pin
            self.change_pin()
        elif menu == '3':
            # check balance
            self.check_balance()
        elif menu == '4':
            #withdraw
            self.withdraw()
        else:
            #exit
            print("Thank you")
            exit()

    def create_pin(self):
        set_pin = input("Enter your pin: ")
        self.pin = set_pin

        bal = int(input("Enter your balance: "))
        self.balance = bal

        print("Pin Created Successfully")
        self.menu()
    
    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin :
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin Changed Successfully")
            self.menu()
        else :
            print("Wrong Pin")
            self.menu()

    def check_balance(self):
        pin = input("Enter your pin: ")
        if pin == self.pin :
            print("Current Balance :",self.balance)
        else:
            print('Wrong Pin')
        self.menu()
    
    def withdraw(self):
        pin = input("Enter your pin: ")
        if pin == self.pin :
            print("Current Balance :",self.balance)
            amount = int(input("Enter Amount you want to withdraw: "))
            if amount <= self.balance :
                self.balance -= amount
                print("Withdraw Successfull. Current Balance:",self.balance)
            else:
                print("Not Enough Balance")
        else:
            print('Wrong Pin')
        self.menu()


# P = Atm()
# print(id(P))


# Creating Own data type 

# creating a fraction data type 
# I want a fraction data type not decimal to do fraction operations

class Fraction:
    '''
    Numerator 
    Denominator
    '''
    # parameterized constructor -> it needs input when creating object
    def __init__(self,x,y):
        self.num = x
        self.den = y

# How do we display fraction object ->#eg - 3/4 ? -> 
# using magic method -> __str__() 
    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self,other):
        if self.den == other.den :
            new_num = self.num + other.num
            new_den = self.den
        else:
            new_num = self.num*other.den + other.num*self.den
            new_den = self.den*other.den
        return f"{new_num}/{new_den}"

    def __sub__(self,other):
        if self.den == other.den :
            new_num = self.num - other.num
            new_den = self.den
        else:
            new_num = self.num*other.den - other.num*self.den
            new_den = self.den*other.den
        return f"{new_num}/{new_den}"

    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return f"{new_num}/{new_den}"
    
    def __truediv__(self,other):
        newother_num = other.den
        newother_den = other.num
        new_num = self.num*newother_num
        new_den = self.den*newother_den
        return f"{new_num}/{new_den}"

    def con_to_dec(self):
        return self.num/self.den
        

f1 = Fraction(3,4)
f2 = Fraction(5,6)

print(f1) # this accesses the __str__() -> 
# then checks how to display the fraction objects
print(f2)

print(f1*f2)
print(f1/f2)
print(f1.con_to_dec())