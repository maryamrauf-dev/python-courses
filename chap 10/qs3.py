from random import randint
class train:
    #constructor to initialize the train number called automatically when object is created
    def __init__(self,trainNo):
        t.trainNo=trainNo

    def book_ticket(self,fro,to):
        print(f"Ticket is book from {fro} to {to} for train {self.trainNo}")

    def get_status(self):
        print(f"Train no: {self.trainNo} is running on time....")

    def fare_information(self):
        print(f"Ticket fare of train {self.trainNo} is {randint(500,1000)}")

t=train
t=train(301)
t.book_ticket("baffa","mansehra")
t.get_status()
t.fare_information()