class Employee:
    a = 100

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname}{self.lname}"

    @name.setter
    def name (self , value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45

e.name = "Pankaj kudari"
print(e.fname , e.lname)
e.show()# prints the class attribute a of class Employee