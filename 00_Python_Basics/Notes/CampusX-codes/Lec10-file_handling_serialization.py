
f = open('sample-1.txt','w') # w -> write , file - doesn't exist , so created new
f.write('Hi. File Handling Sample-1')
f.close()

f = open('sample-2.txt','w') # w -> write , file - doesn't exist , so created new
f.write('Hi. File Handling Sample-2')
f.close()

f = open('Sample-1.txt','w') # opens existing file , over writes old content
f.write('Salman')
f.write('\nkhan')
f.close()

f = open('Sample-1.txt','a') # this will append new content , after the old content
f.write('Bad \nActor')
f.close()

L = ['HELLO','\ni AM GOOD','\nfINE','\nThank YOU ']
f = open('Sample-2.txt','w')
f.writelines(L)
f.close()

f = open('sample-1.txt','r') # r-> read mode
s = f.read(5)
s+= f.read(5) # this will read from the last place were cursor was in that file 
print(s)
f.close()

f = open('sample-2.txt','r')
print(f.readline(),end='') # end -> bcoz readline by def moves cursor to next line 
print(f.readline(),end='')
f.close()

f = open('sample-2.txt','r') 
# this is a way you can use to read a complete file line by line 
while True :
    data = f.readline()
    if data == '':
        print('')
        break
    else :
        print(data,end='')
f.close()

# using 'with' keyword - 

with open('sample-1.txt','w') as f :
    f.write('I am a very bad actor')

# f.write('hello') - gives error as file is closed

with open('sample-1.txt','r') as f :
    print(f.read())


with open('sample-2.txt','r') as f:
    print(f.read(10))
    print(f.read(10)) # this prints the next 10 chacters - basically from where the cursor is left off previously

# This saves memory - instead of loading complete file in memory , we load chunks if it and read it until it is completely read

with open('big.txt','w') as f:
    for i in range(100):
        f.write('hello ')
    f.write('\n')
    for i in range(100):
        f.write('world ')

# NOW we have to read this big.txt - in chunks 


with open('big.txt', 'r') as f:
    chunk_size = 10
    total = 0
    while True:
        chunk = f.read(chunk_size)   # single read, result reused
        if len(chunk) == 0:
            break
        print(chunk, end='**')
        total += len(chunk)
    print(total)


# seek / tell
with open('sample-2.txt','r') as f:
    f.read(7)
    print(f.tell()) # this will print 7 as 0-6 char are read ,and the next char is 7

    f.seek(1) # this will move cursor to 1-index character
    print(f.read(3))
    print(f.tell()) # this will print 4 -> seek - 1 then read 3 -> s 4 

    f.seek(0,2)
    print(f.tell())

# using seek when write
with open('sample-1.txt','w') as f:
    f.write('hi')  # this will over write the file old content
    f.seek(0,2) # move cursor to the end
    f.write(' hello') # write from where the curor currently is 

    f.seek(0)
    f.write('yo') # this will overwrite hi , as the curor was at the start 
    

# WORKING WITH BINARY FILES
# modes - rb and wb

with open('IMG_4608.JPG','rb')as rf :
    with open('COPY_IMG.JPG','wb') as wf :
        wf.write(rf.read()) # this will read old content and then copy the img into another file


with open('sample-1.txt','w') as f:
    # f.write(5) this will raise error - cannot write integer into the file
    f.write('5')
with open('sample-1.txt','r') as f :
    # print(f.read() + 5) raise error -> as cannot add int + str
    print(type(f.read()))

d = {
    'name' : 'Prasham',
    'age' : 21,
    'gender': 'male'
}

with open('sample-1.txt','w') as f:
    # f.write(d) gives error as dict is not a string
    f.write(str(d))
with open('sample-1.txt','r') as f:
    rd = f.read()
    print(rd)
    print(type(rd))
    # dict(rd) error cannot convert str to dict

import json

# SERIALIZATION
L = [1,2,3,4]
with open('demo_json.json','w') as f:
    json.dump(L,f) # this will write L in demo_json
    json.dump(d,f) # this will add dict d next to the above dump , 

with open('demo_json.json','w') as f: 
    json.dump(d,f,indent=4) # replaces old content 
    # indent add indentation to json - beautification


# DESERIALIZATION
with open('demo_json.json','r') as f:
    res = json.load(f)
    print(res)
    print(type(res))

tup = (1,2,3,4)

with open('demo_json.json','w') as f:
    json.dump(tup,f) # even when you dump tuple , you get a list 
    # javascript doesn't have a tuple class/type . it stores it as a list/array

with open('demo_json.json','w') as f:
    json.dump(L,f)
    json.dump('\n',f)
    json.dump(d,f)


class Person:
    def __init__(self):
        self.name = 'prasham'
        self.age = 21
        self.gender = 'male'
    def display_info(self):
        print(self.age,self.name,self.gender)

# cannot directly serialize class objects to json file , 
# objects are not a valid json format

# You have to represtn object in different way to add to a json file

def show_obj(person):
    if isinstance(person,Person):
        return f"name - {person.name}, age - {person.age}, gender - {person.gender}"

p1 = Person()

with open('demo_json.json','w') as f:
    json.dump(p1,f,default=show_obj) # this will dump obj p1 as per the show_obj format 

p2 = Person()

def show_obj_dict(person):
    if isinstance(person,Person):
        return {'name':f"{person.name}",'age':f'{person.age}','gender':f'{person.gender}'}

with open('demo_json.json','w') as f:
    json.dump(p2,f,default=show_obj_dict)
with open('demo_json.json','r') as f:
    d = json.load(f)
    print(d)
    print(type(d))

# PICKLE / UNPICKLE -> BINARY TO PY AND PY TO BINARY
# important

import pickle
p = Person()
with open('person.pkl','wb') as f:
    pickle.dump(p,f)

with open('person.pkl','rb') as f :
    pp = pickle.load(f)
    print(pp) # this will be the P object of class Person

    pp.display_info() # this will run , as pp = p -> person class object



