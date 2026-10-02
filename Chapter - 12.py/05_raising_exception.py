a = int(input("Enter the number :"))
b = int(input("Enter the number :"))

if(b==0):
    raise ZeroDivisionError("hey our program is not meant to divided number by zero")

else:
    print(f"The divided a/b is {a/b}")