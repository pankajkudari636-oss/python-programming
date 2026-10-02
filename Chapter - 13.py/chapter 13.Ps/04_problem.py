
def divisible5(n):
        if(n%5 == 0):
            return True
        return False
a = [1,23,34,544,343774,565677,678,454,789]
f = list(filter(divisible5,a))

print(f)

