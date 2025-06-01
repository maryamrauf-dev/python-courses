def greatest(n1,n2,n3):
    if(n1>n2 and n2>n3):
        print(f"{n1} is the greatest number")
    elif(n2>n3 and n2>n1):
        print(f"{n2} is the greatest number")
    else:
        print(f"{n3} is the greatest number")

a=int(input("enter a number:"))    
b=int(input("enter a number:"))  
c=int(input("enter a number:"))    
greatest(a,b,c)