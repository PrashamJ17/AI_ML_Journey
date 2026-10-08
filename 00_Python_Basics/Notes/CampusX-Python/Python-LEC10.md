
File Handling , Serialization/Deserialization

- Types of Files - 
	- Textual files - Program files
	- Binary Files - images, music ,video, exe files

- File I/O opn - 
	- Open
	- Read/Write
	- Close

- Text Files - 
	- How to write in a text file ? .txt
	- 1. Suppose you don't have a file - so you create one - using 
	  f = open('file_name',opn - (r, w)) , w -> write , r -> read
	- 2. then you write in the file - f.write('TEXT')
	- 3. then close - f.close()

	- what if the file is already there and I want to write/read it ? 
		- f = open('File_name','w')
		- In this if you write on an existing file , then old content erases out and new content , whatever we write replaces them 

- How does open() work ?
	- the files stay on ROM - on hard drive , 
	- so when open() runs , they are moved to RAM for access in the buffer memory
	- From the buffer memory , the file is read - single character from the start 
	- until the file is closed , all the opns performed on the file happens on the buffer
	- after close() , the file is moved out to hard drive .

- What if you don't want to overwrite the old content in the file , instead write new content after the old one ?
	- In such case , you use append mode - 'a'
	- f= open('file_name','a') -> this won't replace old content , add new content only 
	- f.write('TEXT') -> this will start writing , just after the old content stopped (or where the cursor was at the last moment in the file)

- what if I want to write multiple lines /content in the file ?
	- then you use , f.writelines(L) , where L is a list of multiple content that was to be write in the file

- How to read from a file ?
	- 2 methods - read(no.of characters) or readlines()
	- r -> read mode
	- readline -> moves cursor to the next line after reading a line

- when to use read or readline ? 
	- readline -> use when you are using a large file , so that in memory it won't take so much space 
	- read -> for small file 

- Using Context Manager (UCM) -  with 
	- if we don't close a file , it will take up memory and resources until garbage collector eventually closes it 
	- using with keyword, we can close the file as soon as the usage is over
	- with is kind of replacement of f.close()

- using with -
	- with open('file_name','mode') as var_name : 
	- it itself closes the file after all opns are performed

- we read big files in chunks -> to prevent over load 

- f.seek(character) , f.tell() - 
	- f.tell() -> it tells where is the cursor , what is the next character that will be read
	- f.seek(character) -> moves cursor to the character specified
	- f.seek(cookie,whence) -> cookie -> to what posn to move to , whence -> from where , whence = 0,1,2 -> 0 ->from beginning (default) , 1 ->from current position , 2 -> from end 
	- eg , f.seek(0,2) -> this will move cursor to the end of the file 
	- f.seek(10,2) -> this will move cursor at 10th character from the back -> -10 .

- while using seek with writing files : 
	- when you open a file and write it -> it will over write the old content 
	- when you write again , with lets say f.seek(0) -> this will move cursor to the start and over write the old content upto the no. of new charcaters , rest old content will remain the same 

- Problems with text files/modes- 
	- You cannot use for binary files 
	- You cannot read/write different data type content into text files 
	- eg. f.write(5) -> this will give type error , as 5 is an int and not a string
	- f.write('5') -> correct , then f.read() + 10 -> this will give error -> as 5 read is string and 10 is int , cannot be added .

- Working with binary files - 
	- you cannot use normal text mode of read/write - r/w -> this is bcoz - text -> unicode characters - UTF-8 , not binary characters , these modes work with unicode characters only , and so you use different modes 
	- rb and rw -> for read and write resp -> read binary and write binary 

- To solve the second problem -. concept of Serialization and Deserialization 

- Serialization - converting python data to json format 
	- JSON - Javascript object notation - universal data format 
	- Most shareable codes are in JSON format - APIs , Data , Config files , etc
	- similar to python dictionary
	- use json.dump(value,file) -> this writes to value to the file f

- Deserialization - converting json to python data type
	- json.load(file) -> this reads from the file f

- json file only has one element - at the top level - everything else - all the other elements are nested inside it.
	- this top level can either be a { } - dict/object or list/array[ ]
	- all other elements - be it a dictionary , str, int , bool , etc should be inside/nested this root 

-  cannot directly serialize class objects to json file ,
	- objects are not a valid json format
	- You have to represent object in different way to add to a json file
	- define a function - func - to represent obj as you want
	- json.dump(obj,file,default=funct)

- Pickle - 
	- pickling and unpickling - 
	- process where an class object is converted into a byte stream - pickling
	- process of converting a binary file into an object hierarchy- unpickling
	- Since files are in binary , they can be shareable
	- when we unpickle we get the object back , so all the opns can be performed 

- pickle lets the user store infon in binary format , json lets the user store infon in human-readable format - objets cannot be stored in json format
- for machine learning algos , we use pickle a lot as they need to be run on different device and is easy to send in binary and for machine to understand

- 