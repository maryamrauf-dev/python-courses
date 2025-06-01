# class employee:
#     s=50000
#     n="Maryam Rauf"
#     def show(self):
#         self.salary=self.s
#         self.name=self.n
#         print(f"The salary of employee {self.name} is {self.salary}.")
#     # def increment(self):
#     #     self.salary=int(self.salary*1.5)
#     #     print(f"The incremented salaey of employee is {self.salary}.")

#     @property
#     def increment(self):
#         return self.salary * 1.5
#     # @increment.setter
#     # def increment(self,)

# mary=employee()
# mary.show()
# print(f"The incremented salary of employee is {mary.increment}.")
    

class employee:
    salary=550
    increment=50 #increment in percentage
    @property
    def salary_after_increment(self):
        return self.salary+(self.salary*self.increment/100)#increment salary by 50%
    @salary_after_increment.setter
    def salary_after_increment(self):
        self.increment = e.salary_after_increment - e.salary
e=employee()
print(e.salary_after_increment)
print(f"The sallary pecentage increment is {e.increment}.")
