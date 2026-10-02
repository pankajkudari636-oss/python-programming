friends = ["Apple","Radha","Krishna",588,5.535, False]

print(friends[0])
friends[0] = "Grapes" # Unlike string lists are mutable

print(friends[0])
print(friends[1:4])
print(friends)

numbers = [1,12,45, 13,14,27]
numbers.sort()
# numbers.reverse()
numbers.insert(3,33333)  # insert 33333 such that its index in the list is 3
values =numbers
print(values)