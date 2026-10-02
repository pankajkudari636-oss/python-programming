from functools import reduce

l = [111, 234, 23 ,45, 56, 954, 834]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))
