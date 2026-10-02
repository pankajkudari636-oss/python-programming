class Employee:
    company = "Gooogle"
    def show(self):
        print(f"The name of theEmployee is {self.name} and the salary is {self.salary}")

class programmer:
    company = "microsoft"
    def show(self):
        print(f"The name is{self.name} and he is good with {self.language}")

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

class Progarmmer(Employee):
    company = "Apple"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = programmer()

print(a.company , b.company)