a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
d=int(input("Enter the number:"))

if(a>b and b>c and c>d):
    print(f"{a} is the greatest number")
elif(b>a and b>c and b>d):
    print(f"{b} is the greatest number")
elif(c>a and c>b and c>d):
    print(f"{c} is the greatest number")
elif(d>a and d>b and d>c):
    print(f"{d} is the greatest number")
