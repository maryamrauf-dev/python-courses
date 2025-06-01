#base class
class employee:
    company="ITC"
    def __init__(self):
        print("I am employee constructor:")
    def show(self,n,s):
        print(f"The name of employee is {n} and the salary is {s}.")
        print(F"The company is {self.company}.")

#inhereted class 
class programmer(employee):
    def __init__(self):
        print("I am programmer constructor.")
        super().__init__()

    company="DEVSINC"
    def showlang(self,l):
        print(f"The language of programmer is {l}.")
    

a=employee()
b=programmer()
a.show("Mryam",10000)
b.show("Ali",20000)
b.showlang("Python")

