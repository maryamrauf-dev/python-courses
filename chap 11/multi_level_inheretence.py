#base class
class employee:
    company="ITC"
    def show(self,n,s):
        print(f"The name of employee is {n} and the salary is {s}.")
        print(F"The company is {self.company}.")

class coder:
    def code(self):
        print("Python programming language is preffered.")
#inhereted class 
#multiple inheretence with employee and coder class
class programmer(employee,coder):
    company="DEVSINC"
    def showlang(self,l):
        print(f"The language of programmer is {l}.")

class mary(programmer):
    def cong(self):
        print("Congragulations! You are a selected.")

a=employee()
b=programmer()
c=mary()
c.show("Mryam",20000)
c.showlang("Python")
c.code()
c.code()
c.code()
c.code()
c.cong()




