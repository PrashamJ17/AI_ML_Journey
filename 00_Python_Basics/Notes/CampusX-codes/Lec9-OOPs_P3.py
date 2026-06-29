class Customer :
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_add(self):
        print(self.address.get_city(),self.address.state,self.address.pincode)

    def edit(self,new_name,new_city,new_state,new_pin):
        self.name = new_name
        self.address.edit_add(new_city,new_state,new_pin)

class Address :
    def __init__(self,city,state,pincode):
        self.__city = city
        self.state = state
        self.pincode = pincode

    def get_city(self):
        return self.__city
    
    def edit_add(self,new_city,new_state,new_pin):
        self.__city = new_city
        self.state = new_state
        self.pincode = new_pin


def aggre_eg():
    add1 = Address('Mumbai','Maharashtra',400033)
    cust1 = Customer('Pjain','Male',add1)
    cust1.print_add()

    cust1.edit('prasham','jaipur','rajasthan',303007)
    cust1.print_add()

# aggre_eg()

# INHERITANCE - 

# PARENT
class User :
    def __init__(self):
        self.name = 'Pjain'
    
    def login(self):
        print('login')

# CHILD 
class Student(User) :
    # def __init__(self):
    #     self.rollno = 123
    
    def enroll(self):
        print("Enrolled into course")


def inherit():
    u = User()
    s = Student()

    print(s.name)
    # print(s.rollno)
    s.login()
    s.enroll()

# inherit()

class Phone :
    def __init__(self,price,brand,camera):
        print("Inside parent constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")
    

class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        print("Inside child constr")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("child Constructor")
    
    def buy(self):
        print("Buying a smartphone") # first this will execute , then - 
        super().buy() # this will execute after  # syntax to call parent ka buy method

# s1 = SmartPhone(20000,'Apple',4)
# s1 = SmartPhone(20000,"Apple",4,"IOS",12)
# s1.buy()


class Parent :
    def __init__(self):
        self.num = 100
    
    def edit_child(self):
        self.val = 20

    def pr(self):
        print(self.val)
class child(Parent):
    def __init__(self):
        super().__init__()
        self.num = 310
        
    
    def edit_num(self):
        self.num = 30
    
    def add(self):
        self.edit_child()
        # self.edit_num()
        print(self.num)

# c = child()
# p = Parent()

# c.add()
# p.edit_child()
# print(p.val)

# Multi-Level Inheritance
class GrandFather :
    def __init__(self):
        self.gf = 'GF'
        print('gf')
    
class Father(GrandFather):
    def __init__(self):
        super().__init__()
        self.f = 'F'
        print('f')

class Child(Father):
    def __init__(self):
        super().__init__()
        self.ch = 'CH'
        print('ch')

c1 = Child()

# Multiple Inheritance - 

class Dad :
    def __init__(self):
        self.dad = 'D'
        print('DAD')
    
    def parent(self):
        print(self.dad)
        # print(self.mom)
        print('Dad Class')

class Mom :
    def __init__(self):
        self.mom = 'M'
        print('MOM')

    def parent(self):
        # print(self.dad)
        print(self.mom)
        print('Mom Class')

class Kid(Mom,Dad) :
    def __init__(self):
        super().__init__()
        self.kid = 'K'
        print('KID')

    def who_is_my_parent(self):
        self.parent()


k1 = Kid()
k1.who_is_my_parent()

class A:
    def m1 (self) :
        return 20
    
class B(A):
    def m1(self) :
        return 30

    def m2(self) :
        return 40
    
class C(B):
    def m2(self):
       return 20
    

obj1=A()
obj2=B()
obj3=C()

print (obj1.m1() + obj3.m1()+ obj3.m2())


class A:
    def m1(self) :
        return 20
class B(A):
    def m1(self) :
        val=super().m1()+30
        return val
class C(B):
    def m1(self) :
        val=self.m1()+20
        return val
obj=C()
# print(obj. m1())

from abc import ABC,abstractmethod

class BankApp(ABC) :

    def database(self):
        print('Coonected to database')
    
    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def display(self):
        pass
class MobileApp(BankApp):
    def mobile_login(self):
        print('LOGIN INTO MOBILE')
    
    def security(self):
        print('Mobile Security')
    
    def display(self):
        return super().display()

mob = MobileApp()

