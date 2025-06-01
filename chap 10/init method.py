class student:
    name="maryam"
    id=301
    subject="oop"

    def __init__(self):#adding double underscore in start and end is called dunder method
        print("i am automatically called")

    def getinfo(self):
        print(f"the student name is {self.name} wit id {self.id} and subject is {self.subject}")

mary=student()
mary.getinfo()
harry=student()
#by dunder method init is automatically called