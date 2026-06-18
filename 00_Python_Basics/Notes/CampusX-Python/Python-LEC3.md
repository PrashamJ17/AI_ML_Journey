[[LEC3-Python]]


1. **Nested Loops - Loops within a loop**
	 - eg - grid - rows and columns , unique pairs , etc 
	 - inner loop completes first , and runs everytime until outer loop completes

2. **Loops control statements - break , continue and pass** - 
	- break - exits the loop - eg. linear searching in a database - if the result is found then break . 
	- continue - skips the current iteration - eg. using filters , skip the products that are out of stock .
	- pass - does nothing , its just to loop to waste time , good way of not having error. 

3. **Strings** -  
	- In python specifically , sequence of *unicode characters* - 16-bit , 2^16 bit character representation , (ascii character - 8bits - 2^8 bit character representation)
4. Creating strings - using 'Strings' , " Strings" , '''Strings''' , str( )
	 - ' ' -> when in a sentence itself you are using double quotes 
	 - " " -> normal way of creating strings .
	 - ''' ''' -> multi-line strings 
	 - str(Strings) -> str() -> fn to create strings .
5. Indexing in strings - 
	- positive indexing- starts from 0 - from forward - from left to right
	- accessing string - String_name[index] ->get the character of the string at an index 
	- negative indexing - starts from -1 , goes from backwards till the end - from right ot left 

6. Slicing - 
	- in slicing we provide range of index - [ start : stop : step-size] , separated by : 
	- includes the start but not the end index
	- eg. - [2:]
	- we can also use negative indexing - works the same as positive indexing - it doesn't mean we are starting from the back its just indexing/repr is changed .
	- if we want to reverse - in the place of step size -> -1 . 
	- [ : : -1] -> this will reverse the string
	- if nothing in start -> then means -> start from 0 
	- if nothing in end -> this means -> go til the last character 
	- by default step-size = 1

7. **strings are immutable** -> they cannot be changed / edited 
	- we can either use new variable and assign it to the edited , sliced string 
	- to delete a string , variable -> **del var_name**
	- del [sliced_string] -> not possible as we are editing the string -> gives error 

8. Operations on strings - 
	 - Arithmetic - + and *
		 - eg. str1 + str2 -> concatenation
		 - eg. " * " * 50 -> prints asterisk 50 times
	- relational - all the relational ops 
		 - eg - 'delhi' != 'mumbai'
		 - we compare strings lexicographically - the words that come in the dictionary later , or ascii values are bigger 
		 - eg. - 'M' < 'm' -> TRUE as ascii value of capital letter is smaller than lower case letters .
	- logical - 
		- if characters are present in the string -> TRUE 
		- if empty string - False
		- eg. -> 'H' and 'W' -> True -> 'W' because it had to verify both the condn , hence the final condn that it checked was 'W' hence it prints that
		- in or opn , if one is true it doesn't check further , so the final condn that it checks gets printed 
		- not 'String' -> prints False
	- Loops , we can iterate on strings 
	- Membership - in , not in 
		- eg - 'D' in 'Delhi' -> True
		- python is case-sensitive

9. Common String Functions - can be applied to all data types
	 - len( ) -> gives the length of the variable arg
	 - max( ) -> gives the maximum character -> depending on ascii values
	 - min( ) -> gives minimum element -> depending on ascii values
	 - sorted( ) -> sorts the argument and returns a list -> by default it sorts inn ascending order based on ascii values , 
		 - to reverse sort -> sorted(obj,reverse=True)

10. string functions -> 
	 - .capitalize( ) -> first char to upper case
	 - .upper( ) -> all char to upper case
	 - .lower( ) -> al char to lower case
	 - .title( ) -> first char of each word to upper case
	 - swapcase( ) -> upper -> lower , lower -> upper

11. .count(arg) -> finds the no. / frequency of arg in a given string
12. .find(arg) -> returns the first occuring index of the arg in the given string
	 - in case of the arg not present it returns -1
13. .index(arg) -> same as .find(arg) -> except if the arg is not present then it returns error , instead of -1 
14. .endwith(arg) / .startswith(arg) -> returns true or false , if the string starts with or ends with the arg 
15. .format(arg) -> if we want to insert values of variables in a string then , use place holder{ } incase of the variables, and then use .format(var_name) -> to replace those place holders -> it works in order the variable written first , is placed incase of first place holder
16. String conditional fns - 
	 - .isalnum( ) - checks if the string has no.s and characters only and not anything else
	 - .isalpha( ) - checks if the string has characters only and nothing else
	 - .isdigit( ) - checks if strings has no. only and nothing else
	 - .isidentifier( ) - checks if the string is a valid identifier
17. .split( ) -> splits a string into a list
	 - splits the string - by default on ' ' (space) and the elements together form a list
	 - .split(arg) -> splits the string on the arg that is passed in 
18. " " .join(list) -> converts , joins the elements of a list passed as arg and joins them into a list on the basis of the sep , that is passed eg. "-".join(list) -> joins elements of the list and joins them using - (hyphen)
19. .strip( ) -> removes white/blankspaces present in front and back of the string
	 - .lstrip() -> removes front , left blank spaces only
	 - .rstrip() -> removes back , right blank spaces only
20. .replace('this_word','with_this') -> this replaces the specific word with the another word , as passed in the arg 
	 - if a word is not present then the string remains the same