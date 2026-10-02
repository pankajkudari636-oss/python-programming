class Employee:
    name = "Pankaj"
    language = "Py" # This is a class attribute 
    salary = 1200000

Pankaj = Employee()
Pankaj.name = "Pankaj" # This is a instence attribute 
print(Pankaj.name , Pankaj.language, Pankaj.salary)

# Here is name is the instence attribute and salary and language is the class
# attribute and they belongs to class  