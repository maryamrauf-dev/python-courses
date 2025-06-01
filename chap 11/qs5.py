class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,v2):
        result=vector(self.x+v2.x,self.y+v2.y,self.z+v2.z)
        return result
    def __mul__(self,v2):
        result=vector(self.x*v2.x,self.y*v2.y,self.z*v2.z)
        return result
    def __str__(self):
        return f"{self.x}i {self.y}j {self.z}k"
    
v1=vector(1,2,3)
v2=vector(4,5,6)
v3=vector(7,6,4)
print(f"The sum of vectors {v1} and {v2} is: \n{v1+v2}.")
print(f"The product of vectors {v1} and {v2} is: \n {v1*v2}.")      
print(f"The sum of vectors {v1} and {v3} is: \n{v1+v3}.")       
print(f"The product of vectors {v1} and {v3} is: \n {v1*v3}.")
print(f"The sum of vectors {v2} and {v3} is: \n{v2+v3}.")   
print(f"The product of vectors {v2} and {v3} is: \n {v2*v3}.")