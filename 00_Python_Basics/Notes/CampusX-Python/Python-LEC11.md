Exception Handling 

- 2 stages where error may happen in a program - 
	- during compilation - syntax error
	- during execution - Exceptions

- Syntax Error - Wrong Grammar - some error in typing the code 
	- raised by interpreter/compiler
	- Solved -> debugging 
	- eg. - leaving colons , misspells , indentation error , etc , 

- There is some logical error - during the execution of the program . 
	- eg. - Memory Overflow
	- divide by 0 - logical error 
	- Database error 

- Stack Trace - the error that comes when you run a program 
	- it includes type of error - info abt the error - at what line of your code 
	- but if the user sees this error - they die

- Thus , for security and user exp , you need exception handling 
- how ? - 
	- TRY EXCEPT block - try - code that may have error - except handles those error 
	- else block - no error code block that runs after try successfully runs
	- finally block - always runs irrespective of error or success

- Raise exception - 
	- raise this_error('You own message if any')
	- raise Exception('This has occured ')

- Creating Custom Exceptions - 
	- you can create class with Exception class as parent class 
	- then you can raise this class object as exceptions