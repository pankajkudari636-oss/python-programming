import os 

# Select the directory whose content you want to list
directory_path = '/'
path = "."

# Use the os module to list the directory content 
contents = os.listdir(path)

# Print the content of the directory 
print(contents)
