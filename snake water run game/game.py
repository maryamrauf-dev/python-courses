import random

# Generate a random integer between 0,1,-1
computer = random.choice([0,1,-1])

# 0 for snake
#1 for water
#-1 for gun
yourchoice=input("Enter your choice:(s for snake, w for water, g for gun) ")
gamedict={"s":0,"w":1,"g":-1}
reversedict={0:"Snake",1:"Water",-1:"Gun"}
if yourchoice in gamedict:
    you=gamedict[yourchoice]
    print(f"COMPUTER CHOOSE {reversedict[computer]} \nand YOU CHOOSE {reversedict[you]}")

    if(computer==you):
        print("It is a DRAW!")

    else:
        if(computer==1 and you==0):
            print("YOU WIN!")
        elif(computer==1 and you==-1):
            print("YOU LOOSE!")
        elif(computer==0 and you==-1):
            print("YOU WIN!")
        elif(computer==0 and you==1):
            print("YOU LOOSE!")
        elif(computer==-1 and you==1):
            print("YOU WIN!")
        elif(computer==-1 and you==0):
            print("YOU LOOSE!")
else:
    print("INVALID CHOICE ENTERED\n PLEASE enter right choice")      



