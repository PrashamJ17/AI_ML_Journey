# my_list = [1,2,3,4,5]

# my_list.append('Delhi')
# print(my_list)
# my_list.extend('Delhi') # this will divide Delhi into characters and then add to the end of the list
# print(my_list)
# my_list.extend(['Delhi'])
# print(my_list)
# my_list.append([12,4,42])
# print(my_list)
# my_list.extend([64,52,21])
# print(my_list)
# my_list.extend([[12,4.423,42]])
# print(my_list)

# my_list.insert(10,'Hello')
# print(my_list)

# my_list[10] = 'No' 
# print(my_list[10][1])

# del my_list[6:11]
# print(my_list)

# my_list.remove(1)
# print(my_list)

# my_list.pop(10)
# print(my_list)

# list1 = [12,4,2,4213,14,124,1241]
# print(len(my_list))
# print(max(my_list,list1)) # this will compare the first elements of both the list 
# # print(max(my_list)) # this will only work if the list is homogeneous

# # print(sorted(my_list)) # again this will only work for homogeneous list

# print(my_list.index(5))

L = []
for i in range(11):
    L.append(i)
print(L)

L = [j for j in range(11)]
print(L)

basket = ['apple', 'guava', 'cherry', 'banana' ]
my_fruits = ['apple', 'kiwi', 'grapes', 'banana' ]

l1 = [fruits for fruits in my_fruits if fruits in basket if fruits.startswith('a')]
print(l1)

l2 = [[k*l for k in range(4)]for l in range(3)]
print(l2)

l3 = [m*n for m in range(3) for n in range(4)]
print(l3)


l4 = [1,2,3,4]
l5 = [5,6,7,8]
l6 = [i+j for i,j in zip(l4,l5)]
print(l6)

l7 = l6
l7.append(16)
print(l6)

