
Tuples , sets, dictionaries 

- Tuples -
	- basically are immutable lists
	- ordered , allows duplicate
	- can take multiple data type objects - heterogeneous
	- nested tuples are also possible 

- creating tuples - 
	- tuple( ) , t1 = ( ) -> empty tuple
	- tuple with single item - > ( 2, ) -> we need to add a comma after the item 
	- if no comma , then the single item will be a integer 
	- type conversion -> tuple('Hello') -> ('H', 'e', 'l', 'l', 'o')

- accessing items in tuple - 
	- same as lists and strings 
	- positive and negative indexing both are possible
	- slicing is also the same

- Editing items -
	- not possible -> immutable like strings
	- gives error - Type Error 
- adding items - 
	- not possible 
	- again tuples cannot be changed , once made it stays the same

- deletion - 
	- cannot delete single item 
	- del tuple_name -> deletes complete tuple

- operations on tuples - 
	- + and *  -> same as list -> merge and multiplication
	- in and not in also works the same -> membership operators
	- len() , min() , max() , sum( ) , sorted( reverse=True)

- t.count(5) -> same gives the frequency of the value in the tuple
	- if something is not present gives 0
- t.index(6) -> gives the index of the first occuring value passed 

- difference btwn lists and tuples - 
	- syntax - [ ] and ( )
	- tuples are faster than lists due to mutability , immutable objects are faster than mutable 
	- tuples take less space in memory than lists
	- lists is more error prone than tuples 
	- both have there own use cases 


Sets 

- set is unordered collection of objects
- heterogeneous but not mutable objects
- no duplicates 
- mutable - can be changed - add , edit 
- sets can't have mutable items -> like lists , no nested sets 

- Creating a set - 
	- { } -> this will create a dictionary and not a set
	- set( ) -> for empty set
	- {1,2,3,4} 

- accessing and editing set is not allowed as set is unordered so cannot access the item - no indexing or slicing will work , and so editing will also not work 

- adding items in set -
	- s.add(value) ->adds single value to the set
	- s.update(objects) -> add multiple values to the list 
	- order doesn't matter as sets are unordered
	-  update divides multiple elements and then adds to the set ,
		- Hi -> divided into H and i and then added to the list as single characters
		- this tuple will be divided into single elements and then added to the list as single elements
		- in update -> integer objects cannot be added as single element , it ned to be inside of a tuple otherwise it raises an error - Type error
	- use s.add to add a complete string , or tuple or int

- deletion in set - 
	- del set -> deletes the complete set
	- s.discard(value) -> deletes the value from the list
	- if the value doesn't exist , then discard ignores -> doesn't give error 
	- s.remove(value) -> same as discard ,except if the value doesn't exist it gives error 
	- s.pop() -> randomly deletes any element from the set
	- s.clear( ) -> empties the complete set

- Set operations - 
	- s.union( ) or | -> every item of each set will be printed once
	- s.intersection or & -> every item of s1 in s2 
	- s.difference or - -> every item in s1 not in s2
	- symmetric_difference or ^ -> all the items of both the set which are not common
	- membership -> in and not in 
	- loops - for , while 
	- len , min , max , sum, sorted(reverse=True)
	- all the above opns with _ update -> eg. s1.intersection_update(s2) -> stores the result of intersection in s1 and s2 remains as it is . 
	- similarly works for all the other operations

- s1.isdisjoint(s2) -> disjoint sets -> no single item is common
- s1.issubset(s2) -> is s1 a subset of s2 
- s1.issuprerset(s2) -> is s1 superset of s2
- s1 = s2.copy( ) -> copies s2 in s1

- Frozen set -> Immutable version of python set 
	- fs = frozenset([1,2,3,4]) 
	- no addition , no deletion
	- all opns without the update will work .
	- since frozen set are immutable , hence nested frozen sets are possible 

- set comprehension - 
	- { i * 2 for i in range(10) } 
	- same as lists


Dictionaries - 

- mutable , change , edit ,  delete , add
- indexing has no meaning - there are keys instead 
- Keys cannot be repeated 
- Keys should be immutable , no restriction on values
- can be heterogeneous

- Creating a dictionary - 
	- d = { } , dict( )
	- can have nested dictionaries in the place of values 
	- type conversion - dict( pass a list of tuples of 2 elements )
	- keys - must be immutable values

- Accessing the dict - 
	- indexing ,slicing don't work
	- you can access the elements or values by calling their keys 
	- my_dict[key] -> this will print value of the key 
	- my_dict.get(Key) -> this will also access the value of the key 

- editing the dict - 
	- you can edit the values of the specific keys - 
		- eg. student[key] = new_value
	- if the key doesn't exist then the key-value pair is added to the end of the dict , as a new element 
	- dict1.update(dict_another) -> this will update dict1 with the key-value pairs of d2 , if the keys doesn't exist in dict1 , then they will be added. 

- len , sorted , min , max -> work on dict
- dic.items( ) -> this will give a list of tuples of key value pairs
- dic.keys( ) -> this will give a list of all the keys
- dic.values( ) -> this will give a list of all the values 

- Deletion in dictionary - 
	- dict.pop( Key ) -> this will delete the respective key-value pair from the dict
	- dic.popitem( ) -> this will delete the last key-value pair from the dict
	- del dic -> delete the dic
	- del dic[key] -> deleted the specific key-value pair 
	- dic.clear( ) -> this will empty the dictionary . 

- 

