class programmer :
    company = "Microsoft"
    def __init__(self , name, salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("pankaj" , 2500000 , 5811101)
print(p.name , p.salary , p.pin , p.company)
r = programmer("Shubam", 1500000 , 5811101)
print(r.name , r.salary, r.pin , r.company)