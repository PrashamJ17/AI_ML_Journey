
[[LEC1-Python]]

- **Python is a case sensitive language** 
	- eg . Print and print are both different

- **print( )**  -> gives output on the screen 
	- eg. print("Hello World") --> Hello World
	- print( Prasham ) --> this will give error , because there is no quotes to specify the input is string or a variable or int , or whatever . 
	- print("Hello",1,4.5,True) --> we can all print multiple values separated using a , 
	- print( values , sep= ' ' , end= '\n' ) --> this is the print function , sep --> separator to separate multiple values --> by default sep = ' ' 
		 end --> after print fn executes it end with cursor moving to the next line (by default) --> \n 
		 we can specify the end or sep values , to whatever we want 
	- eg. print("Hello",1,4.5,True, sep="-",end=" .") --> this will sep multiple values by -  and ed with . and not go to the next line .

- **Data Types** - 
	- integer -> int
	- decimal -> float
	- boolean -> True or False -> bool
	- Text -> strings -> str
	- complex no. 

- **Data structures** - 
	- Lists  - [ some data sep by ,  ]
	- Tuples - ( some data sep by ,)
	- Sets - { some data (sorted ) sep by ,  }
	- Dictionary - { key: value pairs}

- **type( arg )** --> gives the data type of the input argument

- **Variables** - containers used to store info 
	- when you don't have definite idea of the input , you use variables to store those inputs and use the variable names instead of those inputs everywhere else inside your code 
	- var_name = value 
	- eg. name = 'Prasham'-
	- Dynamic typing -> In python , variables are not defined with a specific data type like in cpp , c , etc --> ( known as static typing)
	- Dynamic binding -> In python , variable's value can be changed 
		- eg - name = 3 .... name = 'Prasham'  -> we change the values of the variables unlike static binding in c, cpp , etc
	 - To create multiple variables at once we can use , 
		 - eg - a,b,c = 1,2,3 
		 - a,b,b = 1,3,4  # this will give b = 4 not 3 .
		 - if all the variables have the same values -> a=b=c=5

- **Comments** ->
	- non-interpreted text --> these are not read , or not the part of the code 
	- used for explanations to understand the code , to help others . 
	- defined using a # before the comment 
	- eg - # this is a comment

- **Keywords and Identifiers** - 
	- keywords or reserved words -> pre-defined words that cannot be used to name the variables . 
	- 33-keywords in python![[Screenshot 2026-06-06 at 6.18.05 PM.png]]
	- Identifiers -> names that you make , create that is used for variables , functions , class ...
		- Cannot start with a digit . 
		- you can only use _ as a special character .
		- cannot be keywords 

- **User Input** - input( ) fn
	- input(argument) -> takes input from the user
	- we can pass in argument -> which can be message like "What's your name" 
		 this will also be printed before asking the input from the user 
	- eg. input("Type your email: ") 
	- Input from the user is always of string data type .
	- string is a universal data format , because different data types can be stored as string

- To change a data type -> type conversion ->
	- built-in fn like int( ) , str( ) , float( ) ... converts to the desired data type 
	- this is explicit type conversion -> we have given fn to change the data type
	- implicit type conversion -> 5 + 5.6 = 10.6 --> interpreter itself converts the data type .

- Literals - Values given to a variable
	- binary literals - 0b binary_no.
	- decimal literals - 100 , 1212
	- hexadecimal literals - 0x hd_no.
	- octal literals - 0o octal_no.
	- float literal - 10.994 , 1.4e2 -> 1.4x10^2 , 1.9e-2 -> 1.9x10^-2 ...
	- complex -> 3 + 4j -> x.real , x.imag 
	- string literal -> ' string ' , "String" , "S" , '''String''' , u"Unicode String" , r"raw \n string"
	- Boolean literal -> True , False
	- None literal -> None

- **sqrt( some value)** --> python math function to find square root
- **pow(value,power)** --> value ^ power 

