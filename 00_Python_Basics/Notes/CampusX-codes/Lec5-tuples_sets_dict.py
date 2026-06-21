def tupl(): 
    tup1 = (1,2,3,4)
    tup2 = (5,6,7,8)
    tup3 = tup1
    tup3 = tup3 + (6,5,4)
    print(tup3)
    print(tup1)

    a,b,c = (1,2,3)
    c,d,*others = (9,10,11,23,2441)
    print(others)
    print(a,b,c)

    print(tuple(zip(tup1,tup2)))

def sett():
    s = set()
    print(s)
    s1 = {1,2,3}
    # s2 = {{124}} # -> gives error
    s1.add('Hello')
    s1.add((120,99))
    s1.add(129)
    print(s1)
    s1.update('Hi',(10,20,'h')) 
    # update divides multiple elements and then adds to the set , 
    # Hi -> divided into H and i and then added to the list as single characters
    s1.update((119,784))
    # this tuple will be divided into single elemnts and then added to the list as single elements
    # in update -> integer objects cannot be added as single element , it ned to be inside of a tuple 
    # otherwise it raises an error - Type error
    print(s1)

    del s
    # print(s)
    s1.discard('h')
    print(s1)
    # s1.remove('h')
    s1.remove('H')
    print(s1)

    print(s1.pop()) 
    print(s1.pop())
    print(s1)
    
def set_opns() : 
    s1 = {1,2,3,4,5,6,7,8}    
    s2 = {1,5,8,4,10,11,15}
    print(s1 | s2)
    print(s1-s2)
    print(s1&s2)
    print(s1^s2)
    
    s1.update(s2)
    print(s1)
    print(s2)

    print(s1.intersection(s2))
    s1.intersection_update(s2)
    print(s1)
    print(s2)
    
    fs1 = frozenset([12,3,'Hello'])
    print(fs1)
    fs2 = frozenset([1,2,frozenset([1,2,4])])
    print(fs2)
    

def dicti():
    d = {'name': 'Prasham', 'Age': 21}
    d1 = dict()

    d2 = {1 : "Hi" , (39,48,'Hello'):'prasham'}

    student = {
        'name':'Prasham',
        'college':'Manipal University Jaipur',
        'sem': 4,
        'subjects':{
            'Maths':78,
            'DSA':95,
            'Eco':99
        }
    }

    d3 = dict([('name','Pjain'),('age',21),(3,9)])
    
    my_name = d3['name']
    num = d3.get('age')

    for i in student :
        print(i)
        print(student[i])

    print(student['subjects']['Maths'])
    student['subjects']['Maths'] = 100
    print(student['subjects']['Maths'])

    student['gender'] = 'Male'
    print(student)

    student.update(d3) 
    print(student)

    for key,value in student.items():
        print(f"{key} : {value}")
    print(student.items())

    for i in student.keys():
        print(i)
    print(student.keys())

    for i in student.values():
        print(i)
    print(student.values())

    print('name' in student)
    print('Pjain' in student)

    # print(sorted(student)) # since keys - integer and string in student cannot be compared

    print(len(student))
    # min/max(student)

    print(student.pop('name'))

    print(student.popitem())
    print(student.popitem())
    
    del student['gender']
    del d1
    print(student)

    d2.clear()
    print(d2)


    num = {i:i**2 for i in range(1,11)}
    
    distnace = {'delhi':1000,'mumbai':2000,'banglore':3000}
    miles = {key:values*0.62 for key,values in distnace.items()}
    print(miles)

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    temp_C = [30.5,32.6,31.8,33.4,29.8, 30.2,29.9]

    temps = {i:j for i,j in zip(days,temp_C) if j > 31}
    print(temps)

    mul_table = {i:{j:i*j for j in range(1,6)}for i in range(2,5)}
    print(mul_table)
dicti()


