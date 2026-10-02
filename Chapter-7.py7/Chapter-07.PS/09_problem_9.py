'''

***
* *      for n = 3
***


'''
# this code is chatgpt this code pinterd correctly  

n = int(input("Enter the number: "))

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
        
# this code in harry's code not pinterd correcty

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*")
    