try:
    a = int(input("Hey , Enter the number :"))
    print(a)\

except ValueError as v:
    print("heyyy")
    print(v)


except Exception as e:
    print(e)

print("Thank you")