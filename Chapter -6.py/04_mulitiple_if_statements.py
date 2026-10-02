a = int(input("Enter your age: "))
# If statement no : 1 
if(a%2 == 0):
    print("a is even")
#End of statement no :1 

# If statement no : 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you ")

elif(a<0):
    print("You are Entering aninvalid negative  age")

elif(a==0):
    print("You are Entring 0 which is not a valid a age ")
#End of statement no : 2


else:
    print("You are below the age of consent")

print("End the program")
