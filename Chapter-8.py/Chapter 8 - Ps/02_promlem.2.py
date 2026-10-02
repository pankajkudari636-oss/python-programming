def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter the temperture in F : "))
print(f"{f_to_c(f)} °c")