class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class manager(Programmer):
    c = 3
o = Employee()
print(o.a) # prints the attribute a of class Employee
#print(o.b) # there is an error because there no attribute b in class Employee 

o = Programmer()
print(o.a, o.b) # prints the attributes a and b of class Programmer

o = manager()
print(o.a, o.b, o.c)# prints the attributes a, b and c of class manager