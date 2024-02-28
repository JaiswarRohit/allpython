class Employee:
   def __init__ (self):
       print("constructor is executed automatically at the time of object creation")

   def m1(self):
       print("m1 print")

E1 = Employee()
E1.m1()
print(dir(Employee))


Emp = Employee()
Emp.__init__()