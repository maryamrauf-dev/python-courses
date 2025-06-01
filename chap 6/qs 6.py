obtain_marks=int(input("Enter your fsc marks:"))
total_marks=int(input("enter total marks:"))

per=(obtain_marks/total_marks)*100

if(per>=90):
    print("EXCELLENT! you scored well.")
elif(per>=80 and per<90):
    print("CONGRAGULATION! Grade \"A\"")
elif(per>=70 and per<80):
    print("CONGRAGULATION! Grade \"B\"")
elif(per>=60 and per<70):
    print("CONGRAGULATION! Grade \"C\"")
elif(per>=50 and per<60):
    print("CONGRAGULATION! Grade \"D\"")

else:
    print("Grade \"F\"")
                       