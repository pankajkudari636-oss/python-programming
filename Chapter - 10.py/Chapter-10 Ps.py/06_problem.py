from random import  randint 
class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(Pankaj, fro, to):
        print(f"Ticket is booked in train no : {Pankaj.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no : {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo}, from {fro}, to {to} is {randint(222, 5555)}")

t = Train(1234)
t.book("Haveri", "Bangalore")
t.getstatus()
t.getfare("Haveri", "Bangalore")