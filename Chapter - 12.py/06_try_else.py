from cmath import e


try:
    a = int(input("Hey, Enter a number :"))
    print(a)
except Exception:
    print(e)

else:
    print("I am inside else")