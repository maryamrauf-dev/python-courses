class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
    def __mul__(self,c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return complex(real_part, imag_part)


    
c1=complex(3,4)
c2=complex(5,6)
print(f"The sum of two complex numbers {c1} and {c2} is {c1+c2}.")
print(f"The product of two complex numbers {c1} and {c2} is {c1*c2}.")