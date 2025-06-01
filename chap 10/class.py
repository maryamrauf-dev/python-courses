class student:
    name="maryam"
    id=301
    subject="oop"
    def getinfo(self):
        print(f"the student name is {self.name} wit id {self.id} and subject is {self.subject}")
    @staticmethod #you don't need to pass object argument
    def greet():
        print("GOOD MORNING")
        #it is not taking object so we dont need to pass argument we can use static method

mary=student()
# print(mary.name,mary.id,mary.subject)
# sana=student()
# print(mary.name,mary.id,mary.subject)
mary.getinfo()
# student.getinfo(mary)
#this is same for above we can say sytactic sugar
#it take 1 positional argument by default 