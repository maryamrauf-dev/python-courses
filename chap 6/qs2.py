m1=int(input("Enter first subject marks:"))
m2=int(input("Enter second subject marks:"))
m3=int(input("Enter third subject marks:"))
per1=(m1/100)*100
per2=(m2/100)*100
per3=(m3/100)*100
total=(m1+m2+m3)/3

if(per1>=33 and per2>=33 and per3>=33 and total>=40):
    print("PASS")
else:
    print("FAIL")