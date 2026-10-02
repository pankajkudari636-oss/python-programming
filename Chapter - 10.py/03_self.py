class Employee:
    language = "Python" # This is a class attribute 
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")

Pankaj = Employee()
#Pankaj.language= "Javas script" # This is a instence attribute 
print( Pankaj.language, Pankaj.salary)
Pankaj.greet()
Pankaj.getInfo()

#Employee.getInfo(Pankaj)
#Employee.greet(Pankaj)