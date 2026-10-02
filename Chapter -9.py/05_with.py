f = open("file.txt")
print(f.read())
f.close()

# The same can written using this statement like this :

with open("file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file 