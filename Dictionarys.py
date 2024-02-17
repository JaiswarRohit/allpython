'''d = {1:"rohit", 2:"nitesh", 3:"suman", 4: 500}
print(d)

d = {}
d[1] = "Nitesh"
d[2] = "Amiya"
d[3] = "Suman"
print(d)

# ACCESSING DICTIONARIES IN PYTHON:

d = {1: 'Ramesh', 2: 'Suman', 3: 'Mahesh'}
print(d[1], d[2], d[3])

# Handle KeyError in Python Dictionary
d = {1:"rohit", 2:"nitesh", 3:"suman", 4: 500}
if 400 in d:
    print(d[400])
else:
    print("Key not found")


#Employee info program by using a dictionary

d = {}
n = int(input(f'Enter Employees no: '))
i = 1
while i <= n:
    name = input(f'Enter your Emp name: ')
    salary = input(f'Enter your Emp salary: ')
    d[name] = salary
    i = i+1

for x in d:
    print(f'the name id: {x} , and his salary is {d[x]}')

#Updating a dictionary in Python:
d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Old dictionary:", d)
d[10] = "Jaiswar"
print(d)



# Removing or deleting elements from the dictionary in Python:

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before deleting key from dictionary",d)
del d[1]
print(d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before deleting key from dictionary",d)
d.clear()
print(d)
'''

# Functions and methods of dictionary in Python

# dict() function:
d=dict()
print(d)
print(type(d))

#dict({key1:value1, key2:value2}) function:
d = dict({1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'})
print(d)

# dict([tuple1,tuple2]):
d = dict([(1, "Ramesh"), (2, "Arjun")])
print(d)

# len() function:
d = dict([(1, "Ramesh"), (2, "Arjun")])
print("length of dictionary is: ",len(d))

# get() method:
d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d.get(1))

print(d.get(100))

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d.get(1))

print(d.get(100,'No key found'))


# pop() method:
d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before pop:", d)
d.pop(1)
print("After pop:", d)

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print("Before popitem:", d)
d.popitem()
print("After popitem:", d)

# keys() method:
d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d)
for k in d.keys():
   print(k)

# values() method:
d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
print(d)
for k in d.values():
   print(k)

# items() method:
d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
for k, v in d.items():
    print(f'{k} ---- {v}')

# copy() method:

d = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
d2 = d.copy()
print(d2)

squares = {a:a*a for a in range(1,6)}
print(squares)