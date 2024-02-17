s = {1, 2, 3, 4,5}
print(s)
print(type(s))


s = {10,'20','Rahul', 234.56, True}
print(s)
print(type(s))


s = set(range(1, 6))
print(s)

# Duplicates not allowed
s = {10, 20, 30, 40, 10, 10}
print(s)


# Sets in Python Example
r = range(1, 11)
s = set(r)
print(s)

d = {}
print(d)
print(type(d))

s = set()
print(s)
print(type(s))

# add() function in sets
s={10,20,30}
s.add(40)
print(s)

# update(x, y) method:
s = {10,20,30}
l = [40, 50, 60, 10]
s.update(l)
print(s)

#Update method
s = {10,20,30}
l = [40,50,60,10]
s.update(l, range(1, 6))
print(s)
s.update(range(1,10,2),range(0,10,2))
print(s)

#copy() method

s={10,20,30}
s1=s.copy()
print(s1)

# pop() method
s = {50,60,30,65,31,55}
print(s.pop())
print(s)


# Remove() method
s={40,10,30,20}
s.remove(30)
print(s)


# clear() method

s={10,20,30}
print(s)
s.clear()
print(s)


#MATHEMATICAL OPERATIONS ON SETS in PYTHON:


x={10,20,30,40, 60, 60, 80, 105}
y={30,40,50,60, 90, 95}
# union method
print(x|y)
print(x.union(y))

# intersection method
print(x&y)
print(x.intersection(y))

# Difference Method
print(x-y)
print(y-x)
print(x.difference(y))

#symmetric_difference():
print(x^y)
print(x.symmetric_difference(y))


#SET COMPREHENSION in PYTHON

s = {x*x for x in range(6)}
print(s)

# REMOVING DUPLICATE ELEMENTS FROM SETS IN PYTHON
l = [0,4,5,6,7,8,1,9,4,5,3,2,2,1,3,4,5]
s = set(l)
print(s)

# FROZEN SET in PYTHON

vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print(fSet)
print(type(fSet))


