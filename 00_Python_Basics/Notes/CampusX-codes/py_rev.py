# print("Prasham","jain",sep="-",end=" .")
# print("Hi")

# # end -> decides where does cursor move after the print st , by default cursor moves to the next line unless specified 
# # sep -> decided what comes between 2 strings in same print st , by default " " comes between different strings unless specified

# print(type(1))

# num = input("Enter a number : ")
# print(type(num))

# # input's from the user are always of string data type . 
# # string is a universal data type - can be used to store different data types 

# # we can also change types of different data types - type conversion 
# # but they need to be a valid data type - canot convert a name-prasham to integer data type 


# # to set multiple variable values at once 

# v1,v2,v3 = 1,"Pjain",[1,2,3,"hi"]

# print(v1,v2,v3)

# # raw string - it ignores the escape sequence and prints them as a string
# print(r"\nHI\n\\\'")

# # operators 

# # operators - 
# # Arithmetic - + , - , * , / , // , ** , %
# # logical - and , or , not
# # relationship - > , < , <= , >= , == , != 
# # bitwise - and , or , not , xor , left shift , right shift
# # membership - in , not in

# # conditionals - if elif else
# # you can also use else statement with loops 

# # Loops - for , while 

# for i in range(1,11,2):
#     print(i)
# else : # this executes , when loops condn becomes False , loops ends
#     print("HI")
 
# print(abs(-100)) # abs(value) -> this always gives absolute , positive values irresepective of the sign of the value . 

# # eg - current pop = 10000
# # population increases 10% every year
# # print pop of lat 10 years 

# # So if its 2026 now , then pop of last 10 years means - 2017 to 2026 
# # 2026 - pop = 10000 - if we go back then last year pop was 10%less 
# # if x ka 10% + x = 10000 -> 1.1x = 10000 -> x = 10000/1.1 
# # the above eqn works in loop until year = 2016 and as year decreases .

# x = 2026
# x_pop = 10000

# for i in range(10):
#     print("year:",x,"population:",x_pop)
#     x -=1
#     x_pop = int(x_pop/1.1)

# v4 = ""
# v5 = '10'
# if v4 : # if the string is empty , then it prints False
#     print('True') 
# else :
#     print('False') # this will print as v4 is empty string

# if v5 :
#     print('Not empty')

# if v4 and v5 :
#     print('Both not empty')
# else :
#     print('one is empty')

# v6 = 'h'
# print(True if v6 and v5 else False)

# if not v4 : # since if v4 -> empty -> False , not v4 -> True , thus statement is True -> print executes
#     print('V4 is EMPTY')


# v7 = v6.replace('h','a')
# print(v6,v7)


# v7 = 'Hi my Name is praSham'

# print(v7.capitalize()) # first letter capital 
# print(v7.title()) # first letter of each word capital 

# print(v7.swapcase()) # swaps upper to lower and lower to upper 


# print("a".isalpha())
# print('for'.isidentifier())
# print("1001".isdigit())

# print("   a b d   ".rstrip())
        

# OOPs Revision

class Atm :

    def __init__(self):
        self.pin = ''
        self.bal = 0
        self.menu()

    def menu(self):
        opn = input("Welcome. How can I help you ?\n1. Press 1 to set pin.\n2. Press 2 to change pin.\n3. Press 3 to check balance.\n4. Press 4 to withdraw.\n5. Press 5 to Deposit.\n6. Press 6 to exit.\n")

        if opn == '1' :
            return self.set_pin()
        elif opn == '2' :
            return self.change_pin()
        elif opn == '3' :
            return self.check_bal()
        elif opn == '4' :
            return self.withdraw()
        elif opn == '5' :
            return self.deposit()
        elif opn == '6' :
            print("Thank You .")
            exit()
        else :
            print('Wrong Input ! Try Again.')
            return self.menu()
        
    def set_pin(self):
        pin = input('Enter Pin : \n')
        self.pin = pin
        print('Pin set successfully !')

        bal = int(input('Enter your Balance :\n'))
        if bal < 0 :
            print('Invalid Balance Amount !')
            self.pin = ''
            return self.menu()
        self.bal = bal
        print('Current Balance = {}'.format(self.bal))
        return self.menu()

    def change_pin(self):
        old_pin = input('Enter old pin : \n')
        if old_pin != self.pin :
            print('Wrong Pin ! ')
            return self.menu()
        new_pin = input('Enter New Pin : \n')
        self.pin = new_pin
        print('New pin set successfully !')
        return self.menu()
    
    def withdraw(self):
        pin = input('Enter your pin : \n')
        if pin != self.pin :
            print('Wrong Pin !')
            return self.menu()
        print('Current Balance = {}'.format(self.bal))
        amt = int(input('Enter amount to withdraw : \n'))
        if amt > self.bal :
            print('Not Enough Balance !')
            return self.menu()
        if amt <=0 :
            print('Amount Entered is Invalid !')
            return self.menu()
        self.bal -= amt

        print('Current Balance = {}'.format(self.bal))
        print('{} withdrawn successfully !'.format(amt))
        return self.menu()
    
    def check_bal(self):
        pin = input('Enter your pin : \n')
        if pin != self.pin :
            print('Wrong Pin !')
            return self.menu()
        print('Current balance = {}'.format(self.bal))
        return self.menu()

    def deposit(self):
        pin = input('Enter your pin : \n')
        if pin != self.pin :
            print('Wrong Pin !')
            return self.menu()
        print('Current Balance = {}'.format(self.bal))
        amt = int(input('Ente amount to deposit : \n'))
        if amt <= 0 :
            print('Amount entered is INVALID !')
            return self.menu()

        self.bal += amt
        print('Current Balance = {}'.format(self.bal))
        print('{} deposited successfully.'.format(amt))
        return self.menu()

# cust1 = Atm()
    

class Fraction :

    def __init__(self,num,den) :
        self.num = num
        self.den = den
    
    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self,other) :
        if self.den == other.den :
            return f'{self.num + other.num}/{self.den}'
        else :
            new_num = self.num*other.den + other.num*self.den
            new_den = self.den * other.den
            return f"{new_num}/{new_den}"
    
    def __sub__(self,other) :
        if self.den == other.den :
            return f'{self.num - other.num}/{self.den}'
        else :
            new_num = self.num*other.den - other.num*self.den
            new_den = self.den * other.den
            return f"{new_num}/{new_den}"

    def __mul__(self,other) :
        return f"{self.num*other.num}/{self.den*other.den}"
    
    def __truediv__(self,other) :
        return f"{self.num*other.den}/{self.den*other.num}"
    
    def conv_to_dec(self):
        return f"{self.num/self.den}"

# f1 = Fraction(1,2)
# f2 = Fraction(3,4)

# print(f1,f2)
# print(f1+f2)
# print(f1-f2)
# print(f1*f2)
# print(f1/f2)
# print(f1.conv_to_dec())


class Coordinates :
    def __init__(point,x,y) :
        point.x_co = x
        point.y_co = y
        
    def __str__(point):
        return f'({point.x_co},{point.y_co})'
    
    def dist_origin(point):
        orig_point = Coordinates(0,0)
        return point.dist_2pts(orig_point)

    def dist_2pts(point,other):
        return f'{((point.x_co - other.x_co)**2 + (point.y_co - other.y_co)**2)**0.5}'
    
    def pt_on_line(point,line) :
        if line.a*point.x_co + line.b*point.y_co + line.c == 0 :
            return True
        else :
            return False

    def dist_line_pt(point,line) :
        return abs(line.a*point.x_co + line.b*point.y_co + line.c) / (line.a**2 + line.b**2)**0.5

class Line :
    def __init__(line,a,b,c) :
        line.a = a
        line.b = b
        line.c = c 
    
    def __str__(line) :
        return f'{line.a}x + {line.b}y + {line.c}'
    
    def pt_on_line(point,line) :
        if line.a*point.x_co + line.b*point.y_co + line.c == 0 :
            return True
        else :
            return False

    def dist_line_pt(point,line) :
        return abs(line.a*point.x_co + line.b*point.y_co + line.c) / (line.a**2 + line.b**2)**0.5



# p1 = Coordinates(5,10)
# print(p1.dist_origin())


class Person :
    def __init__(self,name,country):
        self.name = name 
        self.country = country

    def obj(self) :
        self.name = 'Pjain'
    

def change_name(person) :
    person.name = 'pj'
    return person

# p1 = Person('prasham','usa')
# p1.obj()


# p2 = p1
# p4 = Person('jp','in')
# p3 = change_name(p2)
# p3.gender='male'
# print(p1.name,p2.name,p3.name)

# print(p1.gender,p2.gender,p3.gender)



class Atm : 
    __counter = 1

    def __init__(self) : 
        self.__pin = ''
        self.__bal = 0

        self.cid = Atm.__counter
        Atm.__counter += 1

        # self.menu()
    
    def menu(self) :
        opn = input("Welcome. How can I help you ?\n1. Press 1 to set pin.\n2. Press 2 to change pin.\n3. Press 3 to check balance.\n4. Press 4 to withdraw.\n5. Press 5 to exit.\n")

        if opn == '1' :
            return self.set_pin()
        elif opn == '2' :
            return self.change_pin()
        elif opn == '3' :
            return self.check_bal()
        elif opn == '4' :
            return self.withdraw()
        elif opn == '5' :
            print("Thank You .")
            exit()
        else :
            print('Wrong Input ! Try Again.')
            return self.menu()
        


    def set_pin(self) :
        pin = input('Enter Pin : \n')
        self.__pin = pin

        bal = int(input('Enter your balance : \n'))
        if bal < 0 :
            print('Invalid Balance !')
            self.__pin = ''
            # return self.menu()
        self.__bal = bal
        # return self.menu()

    def change_pin(self) :
        old_pin = input('Enter your old pin : \n')
        if old_pin != self.__pin :
            print('Wrong pin !')
            # self.menu()
    
    def withdraw(self) :
        pin = input('Enter your pin : \n')
        if pin != self.__pin :
            print('Wrong Pin !')
            # return self.menu()

        amt = int(input('Enter amount to withdraw : \n'))
        if amt > self.__bal :
            print('Not enough Balance !')
            # return self.menu()
        if amt <=0 :
            print('Invalid Amount !')
            # return self.menu()
        self.__bal -= amt
        # return self.menu()

    def check_bal(self) :
        pin = input('Enter Pin : \n')
        if pin != self.__pin :
            print('Wrong Pin !')
            # return self.menu()
        print('Current Balance : {}'.format(self.__bal))
        # self.menu()



# c1 = Atm()
# c1.set_pin()
# print(c1._Atm__pin)
# c1._Atm__pin = '1267'
# c1.check_bal()
# # print(c1.__bal)
# c1.__bal = 1000
# print(c1.__bal)


# c2 = Atm()

# print(c1.cid)
# print(c2.cid)

# print(Atm._Atm__counter)

# owner class , every custom has an address class -> its property ,
class Customer :
    def __init__(self,name,gender,address) :
        self.name = name
        self.gender = gender 
        self.address = address

    def print_add(self):
        self.address.print_add()

    def change_add(self,city,state,country) :
        self.address.edit_add(city,state,country)

    def __str__(self):
        return f"{self.name}\n{self.gender}\n{self.address}"

class Address :
    def __init__(self,city,state,country) :
        self.city = city
        self.state = state
        self.country = country 

    def print_add(self) :
        print(self.city,self.state,self.country)
    
    def edit_add(self,new_city,new_state,new_country) :
        self.city = new_city
        self.state = new_state
        self.country = new_country

    def __str__(self) :
        return f"{self.city}\n{self.state}\n{self.country}"

add1 = Address('Mumbai','MH','India')
cust1 = Customer('Prasham','Male',add1)

print(cust1)
cust1.change_add('Jaipur','Rajasthan','India')
cust1.print_add()


# INHERITANCE

# Parent class -> child class
# eg. Udemy platform 
# User -> Instructor and Student 
# Login and register features is for both 
# User -> Parent class -> having login and register
# Student , Instructor -> child class can inherit login and register from User class 

# using super().method() -> to call parents method , if both child and parent have same name classes
class Parent :
    def __init__(self,bg,surname):
        self.bg = bg
        self.surname = surname
    
    def get_bg(self) :
        print('This is parents')
        print(self.bg)


class Child(Parent) :
    def __init__(self,bg,surname,name,age) :
        super().__init__(bg,surname)
        self.name = name
        self.age = age

    def get_bg(self):
        super().get_bg()

# ch1 = Child('O+','Jain','prasham',19)
# ch1.get_bg()

class A :
    def m1(self) :
        return 20
class B(A):
    def m1(self):
        val = super().m1() + 30
        return val
class C(B) :
    def m1(self):
        val = super().m1() + 10
        return val

# obj = C()
# print(obj.m1())

class Mom :
    def __init__(self) :
        self.id = 'M'
    def parent(self) :
        print('Mom')

class Dad :
    def __init__(self) :
        self.id = 'D'
    def parent(self) :
        print('Dad')

class Kid(Mom,Dad) :
    def __init__(self) :
        super().__init__()
        self.child = 'C'
    def my_parent(self):
        self.parent()

# K1 = Kid()
# print(K1.id)
# K1.my_parent()


# abstraction - security method - 
# the methods of parent class with @abstractmethod must 
# be included in the child class 
from abc import ABC,abstractmethod # must be imported to use abstraction 

class BankApp(ABC) :
    def database(self):
        print('connection successful')
    
    @abstractmethod
    def security(self):
        self.pswd = 1230
        print('Hi , Secured')
    
class Mobile(BankApp) :
    def login(self) :
        self.usr = 'P'
        print('Login Success')

    def security(self): # this is included in the child class because it is an abstract method
        pass

    def display(self) :
        super().security()
        print('Using Now')

M1 = Mobile()
M1.login()
print(M1.usr)
M1.display()

M1.security()



