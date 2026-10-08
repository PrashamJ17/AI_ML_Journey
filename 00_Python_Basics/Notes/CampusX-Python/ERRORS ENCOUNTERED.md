1. Syntax Error - 
	- A typo error 
	- When local var already defined and global var_name is called after - both of the same name
	- eg. -  forgotten a closing ' ( ' or a quote " , or something else . 
2. Name Error -
	- a variable , func name is not defined before its use .
	- eg. - NameError: name 'hello' is not defined
3. ModuleNotFoundError   -
	- wrong module imported , or no module exists 
4. Type Error -
	 - When wrong actions , like changing the string , tuples
	 - str,tuple objects are immutable , ... kind of things 
	 - When position error during functions calling
5. UnboundLocalError - 
	- when a variable doesn't exist , or deleted and then called 
	- a variable is not associated with a value , its just there in the memory 
6. key error -
	- when a key , or an element doesn't exist in the data type when its called 
7. AttributeError - When attribute of an object is not defined , doesn't exist in a class
   - wrong functions on wrong types of variables - eg. L = {1:2, 4:'5'} -> L.upper()
8. ValueError - When you do an operation on a non-open object / files
	- I/O opn on a closed file
	- int('a') -> value error
9. Index Error - Index out out range -  index thrown out of range while accessing the item 
10. Indentation Error - when wrongly indented block of code 
11. Filenotfounderror - when file is not found while opening , 
