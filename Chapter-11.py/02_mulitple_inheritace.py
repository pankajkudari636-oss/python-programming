class Employee:
    company = "Gooogle"
    name = "John"
    def show(self):
        print(f"The name of theEmployee is {self.company} and the company is {self.company}")
class Coder:
    language = "Python"
    def printLangauage(self):
        print(f"out all the languages here is your language:{self.language}")

class Progarmmer(Employee, Coder):
    company = "Apple"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Progarmmer()

b.show()
b.printLangauage()
b.showLanguage()