

- Lists - Lists are a data type - to store multiple objects and values and items of different data types -
	 - lists are a dynamic array , we can add values to it .
	 - Mutable - can be changed 
	 - my_list = [ ]
	 - in general you use lists to store large no. of values of similar data type

- Arrays vs Lists - 
	- arrays are fixed sized , in list items can be added ( dynamic array)
	- arrays are homogeneous - only a single data type items can be stored but in list different data type objects can be stored
	- speed of execution is faster in arrays , lists are slower 
	- arrays occupy lower space , while lists occupy larger space in th memory

- How is lists stored in memory ? 
	- referential array - address/ pointer of the items are stored in list 
	- using id( ) - we can get the address of lists , each item of the list  
	- using address we can store different data type items 
	- if you see in the list we are still storing integer data type values only so same data type , those addresses are pointing to different objects 
	- Everytime the list is full , a new array of larger size is created and the new address is stored in it 

- Characteristic of Lists - 
	- Lists are ordered 
	- Mutable , changeable
	- Heterogeneous
	- can have duplicates
	- are dynamic
	- can be nested
	- items can be accessed
	- can contain any kind of objects

- Creating a list
	- list( ) , [ ]
	- [1,2,4,5,6]
	- [ [ ] , [ ] , [ ] ]  -> list within a list 
	- type conversion for list - list( Some value) -> coverts each character into a list elements

- Accessing a list - same as string
	- Indexing  - forward / positive indexing - from 0 till n-1 - left to right
		- negative indexing / backward - from -1 till -n - from right ot left
	- if a list within a list - 
		- can be accessed by first accessing the inner list , then accessing the elements of the inner list .

- Adding a list - 
	- append( ) , extend( ), insert( )
	- append( Value ) -> adds a single value to the end of the list
	- extend(Value) -> adds multiple values to the list 
	- insert(posn,Value ) -> adds single val`ue to the index posn specified

- Editing a list -
	- we can access and change the values in the list
	- using indexing and slicing both , we can change the values of the index posns 

- del List_name -> this will deleted the complete list 
- list.remove(value ) -> this will delete the first occuring value from a list
- list.pop( index) -> pops out , the last elements by default if index is not provided
	- or pops out the value of the specified index
- arithmetic opns - + and * 
	- + -> adds and merges 2 lists 
	- * -> duplicates the lists and merges them L* 3 -> copy L 3 times and merge all 3
- membership ops -> in and not in
	- if i in list or if i not in list
- for i in list -> do this , this will access the elements of the list till the last element 

- List Functions -
	- len , max , min , sorted( reverse = True)
	- count( value ) -> gives the frequency of the value occuring in the list
	- index(value) -> gives the first occuring index of the value in the list
	- L.reverse(  ) -> this will permanently reverse the list , no need to assign it to something . it reverses the original list 
	- L.sort( ) -> sort again is a permanent function -> sorts the original list .
	- copy( ) -> it copies the list as a new list with same elements 

- List Comprehension - 
	- provides a short cut way of writing code
	- new_list = [ expression for item in iterable if condn == True ]
	- efficient , fast
	- nested list comprehension is also valid

- zip( ) - 
	- zip function creates a zip object -
	- it basically matches index of different list and creates a tuple of those index values 
	- it will take 0th index value of different lists and create a tuple with those values
	- It will only go till index of smaller list
	- convert the zip obj into list - list(zip( ))

- lis1 = lis2 -> when we do this then any change in any of those list will change in both the list . instead of doing this , use copy( ) to copy elements then do the changes

