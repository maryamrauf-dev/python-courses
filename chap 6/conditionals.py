a=int(input("Enter your age:"))

#if elif else ladder
if(a<18 and a>0):
    print("You are not eligible for ID card\n\tTHANK YOU! ")

elif(a<0):
    print("You are entering wrong age\nEnter valid age")

elif(a==0):
    print("Surprisingly..!\nYou are not born yet\nEnter valid age")

else:
    print("You can have your ID card\n  Wait for your turn to have it.\n\tTHANK YOU")

print("END OF PROGRAM")