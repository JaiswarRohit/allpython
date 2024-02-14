'''c = "Python programming language, Python is easy"
n = c.split()
print("Before splitting: ", c)
print("After split: ", n)
print(type(n))
for x in n:
    print(x)


print(c.count("Python"))
x = c.replace("is", "hi")
print(x)
print(id(2603625209936))

z = c.split(",")
print(z)

profile = ['Rohit', 'Suresh', 'Jaiswar']
testcase= "rohit suresh jasiwar"
candidate = "-".join(profile)
print(candidate)
print(testcase.title())'''

n = int(input("how many data to add no: "))
name, salary, age = [], [], []
for _ in range(n):
    name.append(input("Enter Your Name: "))
    salary.append(int(input("Enter your Salary: ")))
    age.append(int(input("Enter your age: ")))

for i in range(n):
    print(f'{name[i]} is salary is {salary[i]} and his age is {age[i]}')


'''n = int(input("how many data to add no: "))
name, salary, age = [], [], []
for _ in range(n):
    name.append(input("Enter Your Name: "))
    salary.append(int(input("Enter your Salary: ")))
    age.append(int(input("Enter your age: ")))

for i in range(n):
    print(f'{name[i]} is salary is {salary[i]} and his age is {age[i]}')
   '''


