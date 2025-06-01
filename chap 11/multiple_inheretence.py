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
    

a=employee()
b=programmer()
b.show("Ali",20000)
b.showlang("Python")
b.code()
