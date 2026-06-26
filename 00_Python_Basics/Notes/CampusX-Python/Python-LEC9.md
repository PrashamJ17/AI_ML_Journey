OOPs-Part3

inheritance , polymorphism

- class relationships - 
	- When creating an application , there can be many classes for different entities
	- These classed can be related to each other
	- 2 types of relationships - Aggregation , Inheritance

- Aggregation - 
	- has a relation 
	- One class owns the other class 
	- Owner -> owns , other class -> its property 
	- eg. customer class -> owner , address class -> its property 
		customer has an address
	- hotel has a menu , -> hotel -> owner , menu -> its property
	- the private variables shouldn't be accessed directly by the owner .
	- Instead create a getter method for private variables

- aggregation class diagram - 
	- ![[Screenshot 2026-06-25 at 9.49.09 AM.png]]


- Inheritance - 
	- Simple concept - A parent class and a child class .
	- child class an access all the data and method of the parent class
	- this is better for code reusability
	- ![[Screenshot 2026-06-25 at 10.12.26 AM.png]]

- Think in terms of inheritance -> common functionalities , create parent class then subclasses-> child classes


- What all gets inherited ? - 
	- constructor , non private attributes and methods
	- when both child and parent classes have their own constructor - then the child class will use its own constructor and cannot access the parent class attributes present in the constructor , so the child_obj.parent_att -> not created in the memory . 
	- The flow is when called , child_obj.attr -> it first goes into its own constructor , if constructor is not created then it accesses parent's constructor and its attributes . This is the flow . 
	- So keep in mind that while using child and Parent classes , child constructor should not be created , for it to not over ride paren't attribute access

- ![[Screenshot 2026-06-25 at 10.25.43 AM.png]]

- ![[Screenshot 2026-06-25 at 10.26.06 AM.png]]


- how is it inherited ->  class child_class_name(Parent_class_name) 

- Method Overriding - 
	- what if both parent and child have the same method name ? 
	- then always their own method will be called just like the constructor . 

- Super Keyword - 
	- super().parent_data/method( ) -> this is the syntax to call parent's methods and access its data from child class . 
	-  Solution to the above constructor and method overriding problem is using super() keyword / 
	- Suppose we want to access parent constructor from within child constructor - 
	 then use super().__ init__ (parent_attr_names) -> this will access the parent constructor , then go to the child's constructor
	- This is how we can access / solve the overriding constructor and  methods using super( )
	- Super( ) -> always works inside a class not and gives error outside 
	- Also note - super( ).attribute_name -> this will give error 
	- super cannot be used to access attributes 
	- only constructor , methods . That't it . 

- Types of Inheritance - 
	- Single Inheritance
	- Multilevel Inheritance
	- Hierarchical Inheritance
	- Multiple Inheritance - Diamond Problem
	- Hybrid Inheritance

- Single Inheritance - 
	- one child and one parent 

- Multi level inheritance - 
	- can be infinitely long 
	- ![[Screenshot 2026-06-25 at 12.14.48 PM.png]]
	- The child has access to all the above parent classes . 

- Hierarchical Inheritance - 
	- One Parent , multiple children
	- ![[Screenshot 2026-06-25 at 12.16.44 PM.png]]


- Multiple Inheritance - 
	- Multiple Parent - a child has access
	- child has access, inheriting from multiple classes
	- ![[Screenshot 2026-06-25 at 12.18.10 PM.png]]

- Hybrid Inheritance - 
	- Combination of different types of inheritance
	- ![[Screenshot 2026-06-25 at 12.19.25 PM.png]]


- Method Resolution Order - MRO -
	- In multiple inheritance - out of multiple parents that child class inherits , it can technically only inherit the parent class that is written first when inherited 
	- Only the first parent's data/constructor and methods can be accessed and ignored everything else .  

- Polymorphism - 
	- Having Multiple Phases -
	- Method Overriding - same as above - 2 classes having same name for a method 
		- child's will override parent's method
	
	- Method Overloading - when 2 methods of same name are present inside a class but they have different behaviour based on input . this will give error . 
		- The method that is written latest , runs , it overrides first one. 
	
	- Operator Overloading - same operator has different behaviour based on input -
		- eg. - 'Hello' + 'World' -> HelloWorld, 1 + 3 -> 4


- Abstraction - 
	- its basically a concept of security 
	- If you want someone to not use your class without some security then you make the class abstract class . 
	- For a class to be abstract class it need to have at least one abstract method - denoted as - @abstractmethod just before defining a method
	- for a child class of this parent-abstract class to use , it need to include those abstract method in its code , 
	- Also note - you cannot have an object of abstract class - raises error 
	- to use abstraction concept - 
		- from abc import ABC,abstractmethod
		- then when creating parent class - class Parent_class(ABC) -> this will make the class abstract bu creating atleast one abstract method . 