
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
	1.  .strip() - remove white spaces in the string - 
		- lstrip() - removes left white spaces
		- rstrip() - removes right white spaces
	2. .upper() --> all letters of the string to upper case
	3. .lower() --> all letters of the string to lower case
	4. .title() --> first letter of the each word in the string is capital
	5. .capitalize() --> first letter of the complete string is capital .
	6. .split() --> divides the string based on the separator provided as arg in the func and converts the string into a list .
		- we can also assign the splitted halves of the string to different variables .
	
	 - we can also use multiple of these functions together . 
		 - eg. name.strip().title() 

- **Type conversion** - 
	- int("String") --> converts string no.s to integers . 
	- str(num or bool) --> converts a no. or bool(true/false) to a string
	- float(integer or string) --> converts to a decimal floating pt no. 
- **round(float_no, no_of_digit)** --> rounds a floating no. to the decimal digits as no. specified .
- **How do we print no.s with a , --> eg. 1,000,000**
	- use f-strings 
	- print(f"{100000:,}")    --> we use colon : and then a comma , .
	- by default it uses American system -> millions , thousands .. 
- **during division**   
	- by default its float .
	- if we convert into integer --> prints the lower int value , 
	- eg -> 3/2 = 1 (int)
- **We can also round no.s using f-strings** -- 
	- print(f"{100.99999:.2f}") --> 101.00   -> this will round the no. to 2 decimal places 
- **functions -> def**
	- Functions needs to be defined before their use , just like variables
	- we can either define the main function --> def main():
		and then we can define the other functions . 
		at the end just call main function -> this way it is much easier to write snd  read code
	- non-parameter -> def fn_name( ) : 
	- parameter function -> def fn_name(parameter) :
	- parameter with default value -> def fn_name(parameter = 'Default_value') : 
		- if nothing is passed when the fn is called , then it uses the default value of the parameter
	- return fn --> def fn_name( ... ) : return some_value/variable .. 
- **Scope** --> 
	- local scope --> defined inside a function -> can be passed to other functions but it cannot be used in other functions -> will give us name error , as the variable is not defined in that function . 
	- Although we can use the same name for variables , as the functions are different .
	- global scope --> defined globally --> can be used in any function -> a change in the value of the variable , can be seen globally outside the function as well .
	 