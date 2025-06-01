class mary:
    @property #this is getter
    def name(self):
        return f"{self.sname} {self.lname}"
    @name.setter
    def name(self,value):
        self.sname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
    
#this is abstraction means k user sy process hide krna
#this is encapsulation means k bht sary kam karny valy methods ko aik particular unit e.g(class) mai dal diya
m=mary()
m.name="Mryam Rauf" #calls the setter method and split the string and assign the values to sname and lname
s=mary()
s.name="Ali Rauf"
print(m.sname,m.lname)
print(s.sname,s.lname)

