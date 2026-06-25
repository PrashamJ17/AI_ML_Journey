OOPs - Part 2 - 
revision , Encapsulation , static , ...

- You can access public attributes and methods of an object - obj.att or obj.method()
- If an attribute doesn't exist and you want to create one from outside the class , then 
	- obj_name.new_attr = 'some value' -> this will create another attribute in the class for that object only , its like object variable . It won't exist for other objects .

- Reference Variable - 
	-  Objects are similar to lists 
	- When an object is passed as an argument in a function ,then the changes made to its attr are reflected outside the functions as well . 
	- One object can be identified by any no. of variables
	- eg p = Person( ) , q = p -> one Person() obj has 2 identifications -> p,q
	- since they both represent the same object , then changes made to either one -> changes made to obj -> can be accessed by either p or q
	- Pass by reference - The variable inside and the function -> the argument passed to the function -> referencing the same object -> hence all the changes are made to the same object -> seen outside and inside the function

- Objects are mutable -> as we can change values of its attr even after being created and inside of any function as well . All the changes can be reflected outside the function . 


- Encapsulation - 
	- What is instance variable in python ? 
		- same variable having different values for different objects 
		- eg. -> self.name -> created in a class -> has different values for different objects 
		- variables value depends on object
	- basically encapsulation is creating private variables and methods 
	- these private methods and variables , can be accessed but cannot be edited by users , or objects. 
	- covering methods and variables -> even though they can be accessed 
	- prefix -> __ method_name / attr_name -> all become private when __ is a prefix to them when defining class
	- You can still access the private variables outside the class as well and even if you change it , the main part is it won't give error .
	- Also the most important thing is , its value once set , it cannot be changed , even if accessed outside , and value assigned different and no errors 
	- This is main concept of encapsulation
	- Private methods and variables -> accessed outside the function , some programmer can even try to change its value -> no errors -> but initial value once set cannot be changed .
	- How ? ->  What happens is the obj.__ arr_name -> this in memory becomes -> _ Class_name__att_name -> this is why even when you access the 
	 obj.__ att_name -> you are technically creating a new attr as __ balance for that object and not changing the actual value . 
	- this thing is hidden from the users

- In python nothing is truly private . Programmers can still access and change values by accessing private attr as _ classname__ attname -> and change its value . 
- That is why Python is not for KIDS !! DO NOT CHANGE MY PRIVATE ATTRBUTES VALUE . 
- If you want to access and change then simply create another functions -> which are generally called as setter and getter methods , which will give you the value of the private attr , and secondly let you change the value of those variables . 
	- Write condns which will not let the code crash

- for every attribute create getter and setter methods .  

- Collection of objects - 
	- multiple objects can be stored in lists , sets , dict , etc 
	- same like any other variable 
	- Objects are mutable but they can be stored in sets !! HOW ??

- Static variables - 
	- Unlike instance variables -> whose value is different for different different objs static variables -> is a class variable , for every obj its same value 
	- for values yu want all objects have the same value -> implement them as static variable
	- defined outside any method , within a class . 
	- if methods are using static variable then they use them as -> class_name.vari_name ->
	- good practice to define the variable at the top of all the methods before constructor , just below class ClassName : 
	- you can also set these variables as private and use getter methods to access them 
	- But this methods is of class -> object is not -> its returning value of static variables -> such functions -> identified using - @staticemethod decorator
	- These function don't have self as a parameter unless required
	- called as utility function
	- called using class name -> class_name.fn_name( ) 

- @classmethods -> when we want to pass the attr values of an object during initialization but we don't want to use __ init __ (self,len,height) -> this to pass the values and we don't want setters methods as well . 
- SO we use @classmethod , which will take input of 1)by default class_name while creating object , 2)attribute values passed during object creation . -> this will take the input values and pass them to __ init__() as the argument . 
- def __i nit__(self,len,hei):

self.length = len
self.height = hei

@classmethod
def get_len_hei(cls,len,hei):
return cls(len,hei)

it first goes into classmethods , take the values and then goes into constructor and sets those values of attributes