
Functions 

- 2 principles of functions - 
	1. Abstraction - We know there is a function - we just care about the input to give and get the expected output
	2. Decomposition - There are small different functions - They combine together to make a complete Product/ Output

- def fn_name( parameter ) :
		Doc String - that tells what the function does - for other people to understand - ''' ''' - similar to multi-line comment
		Statements , function body - that executes
		return Value  - the main output of the function
- Parameter vs Argument - 
	- Parameter is for developer who is creating a function 
	- Argument is for user - basically an input to a function in place of parameters

- Doc-string - 
	- ''' ''' 
	- Description of what the function does
	- state the input 
	- state the output
	- created on - 
	- created by - 
	- Things like that 

- A function should be complete - That is it should also include invalid inputs , errors, and so on  - Should take 2 POVs into account - User and Developer

- Types of Argument - 
	1. Default - You have given a parameter a default value while creating a function
		- When no argument is passed while calling the function then it uses the default argument
	2. Position - When calling the function the argument passed must be in order of the parameter 
		- def fn(a,b)  - when called fn(1,2) -> 1 goes into a and 2 goes into b 
	3. Keyword - When passing argument - you mention what parameter has what value , irrespective of the position
		- fn(a=2,b=1) -> this 2 goes into a and 1 goes into b
- When defining functions - default arg come after positional arg(parameter)

- * args , ** kwargs - 
	- These are special keywords used to pass variable length of argument to a function
	- any no. of inputs can be passed when calling a function 
	- internally it creates a tuple of input arguments - * args
	- ** kwargs are -> variable length of keyword args 
	- whenever you put * or ** , this means variable length of input args and keywords args resp 
	- for kwargs - same as args except , they are dictionaries - key-value pairs instead of tuples
	- Incase of parameters - first write normal param, then * args and then ** kwargs - This order is a rule 

- To access a functions doc_string , or doc about a function - 
	- fn_name.__ doc __
	- for any fn for which doc is written , it will show us

- How are functions executed in memory ? 
	- functions are treated as variables - a separate block is created for a function - a separate independent program having all its variables... .
	- interpreter first reads the function line by line as written from up to down 
	- then when the function is called it goes to the function block , executes the code 
	- After the execution of the function , the function block destroys after the output . 
	- When there is no return statement in the function , it still returns a default value - None

- When no return - then it still returns None

- Variable Scope - 
	- global vs local variable - 
	- All the variables defined outside the functions - in the main program -> global variables
	- All the variables defined within a function - when defining - local variable 
	- Local variables cannot be accessed from the main program 
	- global variables can be accessed from with a function
	- Local variables gets destroyed after the execution of the functions
	- even if names of local and global var are same , both are different scope . 
	- To access global variable from within the function - 
		- global var_name 
	- You can access the global variable from within the function by simple var_name but to edit it you have to write global var_name -> in the function have to define it first
	- It is not a good practice to change global var in the function , do not use global keyword too much 

- Nested function - 
	- The inner function are local function for the outside function 
	- Inner fns are hidden from the main program
	- What if you call the function from within the function ? - It forms loop 
	- Whatever var defined in the outer fn act like global var to inner fn 

- Functions in python are first class citizen - 
	- First class citizen are the entity which supports all the operations generally available to other entities
	- Generally data types are considered first class citizen but in python functions are as well 
	- functions act as a data type
	- You can assign a variable to a funtion- so instead of calling the function , you can call the var(arg) 
	- Functions are immutable 
	- you can return one function from anothter function as return fn2
	- You can also pass a function as an argument
	- del fn_name -> this will delete the function

- Benefits of using a function - 
	- Code modularity - divided codes , helps in debugging diffnt small fns
	- Code readability - easier to understand other people codes
	- Code reusability - fns once created can be used repeatedly

- Lambda Functions - 
	- small anonymous function - they are like function comprehension
	- anonymous -> no name 
	- can take any no. of args , 
	- lambda(keyword) a,b(parameters) : a+b(expression)
	- lambda parameter colon expression
	- this fn needs to be stored in a variable , and then to use it , the variable is called .  
	- written in one line , not reusable so much 
	- They are HOF - higher order functions