
[[CS50P - Lecture 0 - Functions, Variables]]

- **input()** - takes input from the user 
	- can take in argument - as string that it prints before the user prompt . 
	- the user input is always considered as string , even if the user input is no.s or symbols . 
	- eg . - name = input("What's your name )
	- in the above eg . we have set the input from the user to a variable - name , to use the user input in further code / fn .  
- **print()** - prints out anything that is given as input in the function. 
	- takes string as an input in double quotes - "STRING" 
	- can also take variable_names , numbers as input . 
	- the cursor moves to the next line after printing . 
	- eg . - print("Hello ",name) , print(123) 
- **return values** - after a function executes it may have a return value . 
	- eg - input() - function returns the user's input . 
	- these return values can be stored as variable names or can be used in further code / functions . 
	- using '='  sign - assignment operator - we can assign the return values to variables , these variables will be used in further code .
- **comments** - ignored notes , text for the programmer , reader  .
	- ' # ' - using # comments are created. 
	- for multi - line comments - ''' jbfbvibfvbfibvjhvuifb ''' -- anything that is writen in in btwn ''' ''' - is considered as comment . 
	- keyboard shortcut - cmd + / 
- **parameters and arguments** - 
	- parameters - what can be passed into a function 
	- arguments - what is actually passed into a function
- **print(*objects, sep=' ', end='\n')** - 
	- *objects - this is the input .
	- sep - separator - by default , a sep = ' ' - how arguments are seperated
	- end - end of print() fn - be default, end = '\n' - \n means new line. 
	- we can overwrite and change sep , end as we need . 
- **escape character - /**     - 
	- used - \n , then when you have to use double quotes inside of double quotes .
	- eg.  print("P said , \"Do you know?\" ")
- **f-string** - if we want to use variables , just put an f before of first double quote
	- eg. print(f"Hey, {name}")
- **string methods** - 
	1.  .strip() - remove white spaces in the string - lstrip() , rstrip()
		- eg . 
	2. .upper()
	3. .lower()
	4. .title()
	5. . capitalize()
	6. .split()
	 - we can also use multiple of these functions together . 
		 - eg. name.strip().title() 
		 - 
