try:
    a = int(input("Enetr a :"))
    b = int(input("Enetr b :"))

    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")