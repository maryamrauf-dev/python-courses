a=int(input("enter a:"))
b=int(input("enter b:"))
if (b==0):
    #give custom error
    #this will crash program by our choice
    raise ZeroDivisionError ("can't divide by zero.")
else:
    print(f"divison{a/b}")