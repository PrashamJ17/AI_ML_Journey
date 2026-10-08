RECURSION 

- calling a function itself within the same function
- using loops is much better than recursion 
- iteration vs recursive 
-  for writing recursive functions - 
	- first identify base case 
	- decompose the problem 
- recursion follows stack - FILO/LIFO 


- rabbit problem - 
	- there are 2 new born - male and female rabbits - in a pen (a stable)
	- they reproduce after they are a month old
	- everytime they reproduce , 2 rabbits - male and female again are born 
	- every pair reproduces each monthly 
	- so - in a pen - no. of pairs
		- 0, 1 , 1, 2 , 3 , 5 , 8 , 13 , 21 , ... 
		- so this is a fibonacci code

	- months - jan , feb , march , aprl , may , june , july , august ,
	- rabbits - 1 , 2 , 3 , 5 , 8 , 13 , ....

	- so lets say they are starting from 1 pair of rabbits already -> 1 , 1 , 2, 3, 5, 8, 13 , and so on thus add - previous 2 no.s to get third no.
	- base case - total months -> 0 or 1 -> rabbits -> 1
	- else -> after 1 months -> rabits -> sum of last 2

	- lets say total months = 5
	- month = 5 -> go to else -> return (4) + return(3)
	- month = 4 -> for to else -> return(3) + return (2)
	- month = 3 -> go to else -> return(2) + return(1)
	- month = 2 -> fo to else -> return(1) + return)(0)
	- month = 1 -> go to if -> return 1
	- month = 0 -> go to if -> return 1	
	- then back track .
	- so total rabbits -> 8

- this above algorithm is highly inefficient - bcoz , as input increases the time complexity increases exponentially ![[Screenshot 2026-07-01 at 3.44.23 PM.png]]

- so time complexity - 2^n -> ![[Screenshot 2026-07-01 at 3.46.40 PM.png]]


- This is because you repeatedly solving sub-trees with this methods

soln - 
- Storing values that are already calculated 
- memoization method -> that is storing of values that are calc previously , and using them when needed '
- even though you are using more space , but time complexity is decreases . 
- 