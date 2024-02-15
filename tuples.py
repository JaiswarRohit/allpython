employee_ids = 1, 2, 3, 4, 5
print("same type of objects:",employee_ids)
print(type(employee_ids))


name =("Sushanth", )
print(name)
print(type(name))

name = "Sushanth",
print(name)
print(type(name))

t=tuple(range(1, 10, 2))
print(t)


t=(10,20,30,40,50,60)
print(t[0])           #   10 #Positive indexing
print(t[-1])          #   60 #Negative indexing
#print(t[100])        #   IndexError: tuple index out of range


#Accessing Tuples using Slicing operator in Python:

t=(10,20,30,40,50,60)
print(t[2:5])
print(t[2:100])
print(t[::2])


#Accessing Tuples using Looping in Python:


t=(10,20,30,40,50,60)
for i in t:
   print(i)


#len() function
t=(10,20,30,40)
print(len(t))

#count() method
t=(10,20,10,10,20)
print(t.count(10))

#index() method in Tuples:
t=(10,20,10,10,20)
print(t.index(10))
# print(t.index(30))#     #  ValueError


t=(10,20,10,10,20)
print(t.index(10))
# print(t.index(30))#     #  ValueError


# sorted() function in Tuples:

t= (40, 10, 30, 20)
t1 = sorted(t)
print(t)
print(t1)

# min() and max() functions in Tuples:
t=(40,10,30,20)
print(min(t))    # 10
print(max(t))    # 40


a=10
b=20
c=30
d=40
e=50
t= a, b, c, d
print(t)



t = (x **2 for x in range(1,6))
print(type(t))
for x in t:
   print(x)