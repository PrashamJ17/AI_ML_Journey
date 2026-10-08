Namespaces and Decorators - 

- Name spaces - dictionary of variables/identifiers and their values 
- 4 types of namespaces - LEGB 
	- Local , enclosing , global , built-ins

- scopes - region of program where a namespace is directly accessible 
	- basically , area where s variable is accessible from 
- the interpreter follows LEGB rule while searching for a variable -
	- goes from inside out - Local -> enclosing -> global -> built-in
	- if no variable is found -> raise NameError exception

- Local and Global - scope/namespaces - 
	- global scope includes all the variables/identifiers of the code in the main program , outside any function or class method
	- The variables can be  accessed from within a function 
	- Local scope includes all the variables defined within a function or a class method and are valid and accessed from within them only . 
	- local variables cannot be accessed outside the function globally 
	- Name of local and global scope can be same - but 2 local variables or 2 global variables cannot be same . 
	- We can access and read global variables within local functions but we cannot edit them , unless called .
	- to edit global variables - keyword global var_name  ->  need to be there in the local functions
	- If we call global x , but x is already defined locally , then it raises SyntaxError - y is assigned to before global declaration - both of the same name
	- Parameters of a function are also local variables
	- Follow LEGB rule 

- Built-in scope - 
	- Namespace - a list -  of all the keywords , like print , len , type , all the Exceptions , id , dunder methods , etc .
	- to see all the built-ins - use import builtins -> dir(builtins)
	- we can have our own functions names as keyword names -> then follow the LEGB rule - we will first access our own functions and not the keyword / builtin function - eg.  def max() and then max() -> this won't call max built in function but out own function 

- Enclosing Scope - 
	- this is for functions within functions - enclosing functions
	- innermost functions - local functions 
	- and as the hierarchy goes outer functions - enclosing functions
	- you can access, read these enclosing scope variables from any inner functions 
	- but to edit them you have to use nonlocal var_name -> defined first in order to edit them


- Decorators - 
	- A decorator in python is a function that receives another function as input and adds some functionality to it and returns it . 
	- python functions are first class citizens - all the operations can be applied on functions - that is why decorators can be used on functions
	- @dec_name -> this is a decorator
	- built-in decorator - @staticmethod , @classmethod , @ abstractmethod , etc 
	- user-defined decorator - programmers create these as per use

- decorator returns a function object -> note its not calling the wrapper functions , instead it is returning the function obj , which is stored in another variable 
- this variable is now pointing/referencing to that wrapper function object 
- so when this variable function is called -> this now calls the wrapper function and does the functionality .
- This is how the decorators work , just returning the inner wrapper function object , storing it in a variable , everytime we want to use it , just call the variable . 
- the variable stores the ref to inner function but when it is called , it can access to outer function variables as well !! this is known as closure in python
- When outer function returns inner function -> it also stores enclosing variables , that is outer function variables -> this is why the inner function - wrapper, is able to call another function that is passed to the deco and not the wrapper . 
- ![[Screenshot 2026-07-08 at 11.58.48 AM.png]]

- Child function can still access parent function's variables even when parent is not in memory 

- @my_deco -> above a function where you want to use dec -> then call the function
- the decorator function 