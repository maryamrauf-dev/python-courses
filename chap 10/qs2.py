class calculator:
    def square(n):
        return n*n
    def cube(n):
        return n*n*n
    def squareroot(n):
        return(n**(1/2))
    
number=calculator
x=int(input("enter the number:"))
print(f"The square of {x} is {number.square(x)}.")
print(f"The cube of {x} is {number.cube(x)}.")   
print(f"The square root of {x} is {number.squareroot(x)}.")   
