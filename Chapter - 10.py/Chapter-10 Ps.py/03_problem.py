class Demo:
    a = 4

o = Demo()
print(o.a) # it prints the class attribute because instance attribute is not present      

o.a = 0
print(o.a) # it is instence attribute set 

print(Demo.a) # prints the class attribute 
