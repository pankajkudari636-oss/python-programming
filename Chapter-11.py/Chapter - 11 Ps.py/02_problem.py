class Animals:
    pass

class pets(Animals):
    pass

class Dogs(pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dogs()
d.bark()
