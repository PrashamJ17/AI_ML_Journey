# REVISION - 

# classes and objects 
# objects are instances of classes 
# class -> blueprint/rules you define for the objects to follow
# objects are represented. as self in the class while defining the rules 
# some methods within the class -> dunder methods or magic methods 
# They are pre-built methods like __init__ , __repr__ , __str__ , and so on 
# __init__(self,*parameters) -> called constructor method , which runs when in the main function , obj is created
# obj_name = Class_name(*arguments) -> this is how we create an object , when this line runs , __init__ is called by default 
# and attributes are set to object and any method inside it is called ... 
# attributes can be either private or public 
# private attributes are represented as __attr_name or __method_name -> 
# normal attributes are public 
# these private attributes and methods cannot be used directly outside the class by the object . 
# to access them , there needs to be some getters and setters methods that needs to be defined within the class . 
# although there is a way -> obj_name._Class_name__attr_name -> you can call this functioin outside the class and it will 
# access the private attribute
# In python nothing is truly hidden 
# There are some attributes that are static , that is there value remains constant everytime an object is created
# The static attributes are generally class attributes 
# they are defined outside any method , within the class 
# to access them -> class_name.attr_name -> this is how we access them 
# these can again be private or public

# some magic methods -> __str__ -> they are called when print(obj) -> this is called in the main function

# __repr__ -> this is called within the class methods -> its returns how the objects are represented within a class 
# eg. -> instead of main.__class_name__03w ... something , you can represent object however you want in the __repr__ method . 

# __eq__(self, other)	==	Equality comparison
# __ne__(self, other)	!=	Inequality comparison
# __lt__(self, other)	<	Less than
# __le__(self, other)	<=	Less than or equal
# __gt__(self, other)	>	Greater than
# __ge__(self, other)	>=	Greater than or equa

# __add__(self, other)	+	
# __sub__(self, other)	-
# __mul__(self, other)	*	
# __truediv__(self, other)	/
# __floordiv__(self, other)	//	
# __mod__(self, other)	%
# __pow__(self, other)	**	
# __radd__(self, other)	other + self

# __len__(self)	Returns length (for len())
# __getitem__(self, key)	Gets item by index/key (for obj[key])
# __setitem__(self, key, value)	Sets item by index/key
# __delitem__(self, key)	Deletes item
# __contains__(self, item)	Membership test (for in operator)
# __iter__(self)	Returns iterator for for loops
# __next__(self)	Returns next value in iteration

# __call__(self, *args, **kwargs)	Makes object callable like a function
#     def __init__(self, factor):
#         self.factor = factor
#     def __call__(self, x):
#         return x * self.factor

# triple = Multiplier(3)
# print(triple(5)) 

# __getattr__(self, name)	Gets attribute (fallback if not found)
# __setattr__(self, name, value)	Sets attribute
# __delattr__(self, name)	Deletes attribute
# __getattribute__(self, name)	Gets attribute (always called)

# __int__(self)	Converts to integer (for int())
# __float__(self)	Converts to float
# __str__(self)	String representation
# __bool__(self)	Boolean evaluation (for if statements)
# __hash__(self)	Hash value (for sets/dicts)


# __new__(cls,*parameter) - this is a static method , that creates instances of the class 
# when you call obj_name = Class_name(*args) -> this calls new -> creates instance -> sends to init ->
# initalizes the instance with attributes and methods ...

# class User:
    # def __new__(cls,value):
#        return super().__new__(cls)   (or some other child class) 

# using this instance is created
# its not so much used unless there is some conditions on objects created . 
# if using Parent class you want to use some condition , to create instance of the child class
# class Payment:
#     """Create different payment processors"""
    
#     def __new__(cls, payment_type):
#         if payment_type == "credit_card":
#             return super().__new__(CreditCardPayment)
#         elif payment_type == "paypal":
#             return super().__new__(PayPalPayment)
#         elif payment_type == "bitcoin":
#             return super().__new__(BitcoinPayment)
#         return super().__new__(cls)

# we use cls that is class_name (it is substitue for class ) because ,instance(obj) has not yet been created
# in __init__ -> the ibject is already created and we were initializing it with attributes 

# __repr__ -> used to represent objects -> 
# in normal case objects are represented as - obj_name.__clas_name__0xs...
# but with repr , we can rename it as we want and store it for easy understanding and readability and debugging

# if __str__ is not present in the code , then python calls __repr__ for print(obj)

# __iter__ and __next__ - these are used in looping through objects 
# for i in obj : this calls iter and next
#    do this 
# we need to use both these methods -> 
# iter initializes the start value - as self.current = self.start (or something) then returns self
# so it creates an attribute of self as current and then returns self
# then next runs with self.current  as start and the applies some condition to raise StopIteration
# Stop iteration is important for loop to not run infinitely 


    # def __iter__(self):
    #     self.current = self.start   # reset each time loop starts
    #     return self                 # this object is its own iterator

    # def __next__(self):
    #     if self.current <= 0:
    #         raise StopIteration     # tells the for-loop to stop
    #     value = self.current
    #     self.current -= 1
    #     return value


# __getattr__ -> its a getter method for non-existing attributes -> obj.attr -> calls this function
# if the object doesn't have the attribute called it calls this function - 

# __getattribute__ -> this is used to access the existing attributes and print thier value
# inisde the super().__getattribute__(attr) must be called to get the actual value

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __getattribute__(self, attr):
#         print(f"[LOG] Accessing: {attr}")
#         return super().__getattribute__(attr)   # must call super() to get actual value

# Use __getattr__ most of the times and not __getattribute__
# class Config:
    # def __init__(self):
    #     self._data = {"db_host": "localhost", "db_port": 5432}

    # def __getattr__(self, key):
    #     if key in self._data:
    #         return self._data[key]
    #     raise AttributeError(f"Config has no setting: '{key}'")

# in this as well , there when caller calls obj.db_host ->
#  python cannot find it , as its within a dictionary and not as self.db_host so it goes 
# to __getattr__ -> and then runs that method 


# That's it about dunder methods

# Then there is concept of inheritance and aggregation ->
# inheritance is parent child , child has access to parent's attrbutes and methods 
# if the same name attributes or methods exist then child's will override parent , and call its own attr and methods
# to use parents we need to use super() in methods of childs 
# super().__init__ , super().anymehtod , or somehing like that . 


# you can have multiple inheritance as well -> one child multiple parents -
# in such case , it inherits from both 
# but if there are same_name methods and sttributes - then it simply follows - MRO
# MRO- Method Resolution Order - whichever class is written first while inheriting - Class C(A,B) - so A
# that class's attrbutes andmethods are accesed 
# MRO — Method Resolution Order
# Python uses the C3 Linearization algorithm to decide the order in which classes are searched for a method.

# print(D.__mro__)
# # (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

# # Or more readable:
# print([cls.__name__ for cls in D.__mro__])
# # ['D', 'B', 'C', 'A', 'object']
# Python searches left to right, depth considerations applied:

# D → B → C → A → object
# First match wins — so B.greet() is called.

# class A:
#     def greet(self):
#         print("Hello from A")

# class B(A):
#     def greet(self):
#         print("Hello from B")
#         super().greet()     # next in MRO after B → goes to C, not A

# class C(A):
#     def greet(self):
#         print("Hello from C")
#         super().greet()     # next in MRO after C → goes to A

# class D(B, C):
#     def greet(self):
#         print("Hello from D")
#         super().greet()     # next in MRO after D → goes to B


# d = D()
# d.greet()
# Hello from D
# Hello from B
# Hello from C
# Hello from A



# ABSTRACTION - 
# simple concept of security/rule - hiding internal implementation details
# "What it does" is visible. "How it does it" is hidden.

# using abc module - abstract base class 
# from abc import ABC,abstarctmethod -> this need to be used in order to introduce abstraction concept
# to define an abstract class - class class_name(ABC) : 
# no instance of abstract class can be created
# in this class you define the functions that needs no exception to be present in the child classes in order to be used 
# you use abstraction to use DRY from you code -
# instead of similar idea code/method are included in multiple classes and they needs to be called everytime for an object of any class , 
# then use abstarction class and define all those methods , then use same name methods in each class
# when you want to call , just write a function obj.function -> this will call that class's object and its function
# 
# from abc import ABC, abstractmethod

# class PaymentGateway(ABC):

#     @abstractmethod
#     def authenticate(self):
#         pass

#     @abstractmethod
#     def pay(self, amount):
#         pass

#     @abstractmethod
#     def get_receipt(self):
#         pass

# class UPI(PaymentGateway):
#     def authenticate(self):
#         print("UPI PIN verified")

#     def pay(self, amount):
#         print(f"Paid ₹{amount} via UPI")

#     def get_receipt(self):
#         print("UPI receipt sent to phone")

# class CreditCard(PaymentGateway):
#     def authenticate(self):
#         print("Card CVV verified")

#     def pay(self, amount):
#         print(f"Paid ₹{amount} via Credit Card")

#     def get_receipt(self):
#         print("Receipt sent to email")

# # Caller doesn't care HOW payment is done internally
# def process_payment(gateway: PaymentGateway, amount):
#     gateway.authenticate()
#     gateway.pay(amount)
#     gateway.get_receipt()

# process_payment(UPI(), 500)
# # UPI PIN verified
# # Paid ₹500 via UPI
# # UPI receipt sent to phone

# process_payment(CreditCard(), 1200)
# # Card CVV verified
# # Paid ₹1200 via Credit Card
# # Receipt sent to email
