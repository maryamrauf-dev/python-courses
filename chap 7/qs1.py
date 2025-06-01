n=int(input("enter the number:"))
#printing table using for loop
i=1
for i in range(11):
    print(f"{n}  into  {i}  is\t{i*n}")
    i+=1

    #printing table using while loop
i=1
while(i<11):
    print(f"{n}  into  {i}  is\t{i*n}")
    i+=1