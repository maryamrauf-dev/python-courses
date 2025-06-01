#base class
class employee:
    company="ITC"
    def show(self,n,s):
        print(f"The name of employee is {n} and the salary is {s}.")
        print(F"The company is {self.company}.")

# class programmer:
#     company="DEVSINC"
#     def show(self):
#         print(f"The name of employee is {self.name} and the salary is {self.salary}.") 
#     def showLang(self):
#         print(f"The language of programer is {self.language}.")

#inhereted class 
class programmer(employee):
    company="DEVSINC"
    def showlang(self,l):
        print(f"The language of programmer is {l}.")
    

a=employee()
b=programmer()
a.show("Mryam",10000)
b.show("Ali",20000)
b.showlang("Python")
