OOPS - PART-1

- OOPs principles -
	1. Objects and Classes
	2. Abstraction
	3. Encapsulation
	4. Inheritance

- Classes and Objects - 
	- Class is a blueprint - where rules are defined for an object of the respective class
	- Object is an instance of the class
	- eg. -> list is an inbuilt class , whenever you create a list , then that is an object of the list class - which has functions , data ...
	- class syntax - 
	 class ClassName : 
			This is where you create constructors and functions and data for the object , basically the rules/blueprint of objects of the class	
	- object syntax - 
		 obj_name = class_name( ) , that's it the object is created and constructor function runs by default 
	- only objects can access the data and methods created by class

- methods vs functions - 
	- Methods are functions within a class
	- Functions are normal def functions outside of the class
	- Methods are for respective class and its objects
	- obj_name.method() -> this is how you call a method


- Class Diagram - 
	- ![[Screenshot 2026-06-22 at 7.46.28 PM.png]]


- Magic Methods or Dunder Methods - 
	- special methods - __ _fnname_ __  (self) : every magic method has its own super power .
	- Eg.- constructor - __ init __ (self) -> executes whenever an object is created
	- using magic method you can create your own data type .

- constructor -> it is a special method 
	- triggers automatically whenever an object is created 
	- def __ init __ (self) : 
	- What is the benefit of using constructor ? 
		- Things you don't want user to control - all that code goes under constructor
		- like backend code , configuration related code , etc all those codes goes under constructor , internet connection, some integration
		- basically all the code without user permission or knowledge 
		- if god is the programmer , earth is a class , human beings are objects then , for eg , death comes under constructor , age growth , etc .
		- You cannot rename constructor
		- system boot - things you want to initialize on startup - goes into constructor

- self -> the default parameter of the class -
	- self is basically general term for the object of the class 
	- Inside a class rules  , only objects can access the methods and data of the class . 
	- So to communicate with each other ,  for one function to call another function , it was not possible even within the class , without using an object . 
	- This is where self comes in as object , and lets us define the rules and call other methods from another methods by using self as an object
	- eg. constructor want to call menu() , it cannot call menu( ) directly, it need to use self.menu( ) -> as an object calling menu( )
		-> this is the rule in python
	- when in the main function , we create object , it goes as an argument in place of self . 
	- we can change, rename self 
	- self always points to the current object you are working with , in case of multiple objects of a class

- __ str __ (self) -
	- superpower -> It includes all the code that displays how the class objects look like when print(obj_name) -> is called . 
	- by default when print is called , it goes into __ str __ ( ) and accordingly displays the object

- __ add __ (self,other) -> 
	- this is a magic method to add to objects of the same class 
	- self -> first object , other -> 2nd object 
	- whenever obj1 + obj2 -> the operand + is used , then it accesses the 
	__ add __ ( ) method and performs the code written in it . 

- __ sub __ (self,other) -> same as above for subtraction of 2 objects - 
- __ mul __ (self,other) -> same as above for multiplication of 2 objects *
- __ truediv__ (self,other) -> same as above for division of 2 objects / 

- __ repr__ (self) -> to represent objects , not like <main memory_add > but a string representation of objects , when they are used within class , used by devlopers ,
- similar to __str__ but its a representation of objects and not print( obj ) , 