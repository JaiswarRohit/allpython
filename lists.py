'''
l1 = []
print(l1)
print(type(l1))

l2 = ["Rohit", "Suman", 1, 3, True, None]
print(l2)

#  Creating a list using list() function

r = range(1, 6)
l = list(r)
print(l)

# Mutability

n = int(input(f'Enter your List Range: '))
p = list(range(1, n+1))
print(p)
print(f'Before modifying n[0] : {p[0]}')
p[0] = 20
print(f'After modifying n[0] : {p[0]}')
print(p)

# Accessing List in Python:

#By using indexing
#By using the slicing operator
#By using loops

names = ["Prabhas", "Prashanth", "Prakash"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(type(names))
print(type(names[0]))
print(type(names[1]))
print(type(names[2]))

#By using the slicing operator

n = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
print(n)
print(n[1:7:1])
print(n[4::2])

#Accessing List By using loops in Python:

a = [100, 200, 300, 400]
#for x in a:
#   print(x)

x=0
while x < len(a):
    print(a[x])
    x = x+1

#IMPORTANT FUNCTIONS OR METHODS OF LISTS IN PYTHON

n = ["rohit", "rohit", "suman", "suman"]
print(len(n))
print(n.count("rohit"))
print(n.append("Nitesh"))
print(n)
n.insert(2, "Jaiswar")
print(n)

a.extend(n)
print(a)
print(n)
n.remove("suman")
print(n)
n.remove("suman")
print(n)



n=[1, 2, 3, 4, 5]
print(n.pop(2))
print(n)

print(n.pop())
print(n)'''

#Ordering the elements in list:

n = [1, 2, 'rohit', 3, 4, 'two']
n.reverse()
print(n)

s=['Suresh', 'Ramesh', 'Arjun']
s.sort()
print(s)

y=s
print(y)
s[1] = "Rohit"
print(s)
print(y)
print(id(s))
print(id(y))


w = [10, 20, 40, 60, 70, 80]
print(20 in w)
print(70 not in w)


f= [3, 4, 6]
g= [10, 30, 7, 80, f]
print(g[4])

j = [4, 5, 7, 9, 10]
y = []
for i in j:
    y.append(i*2)
print(y)

k = [1,2,3,4,5]
o = [i*2 for i in k]
print(o)
