
- Dunder methods - 
	1. __ init__(self, * parameters)- initializes the object by calling  this method 
	2. __ new__ (cls, * parameters) - it creates an instance/object if the class , runs before init method initializes it 
		- so when we create an object of the class , it calls the new method , creates the instance/object -> super( ).__ new__(cls) -> and then sends it to init method to initialize it with attributes and other methods or...