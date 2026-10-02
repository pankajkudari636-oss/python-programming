l = [123 , 323 , 567 , 575 , 487]

index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

# This can be simplefied using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")