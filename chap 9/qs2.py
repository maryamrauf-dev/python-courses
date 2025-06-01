import random

def game():
    print("YOY ARE PLAYING A GAME.....")
    score=random.randint(1,50)
    print(f"COMPUTER CHOSE {score}")
    #find the hiscore
    try:
        with open("hiscore.txt","r") as f:
            hiscore=f.read()
            if(hiscore==""):
                hiscore=int(hiscore)
            else:
                hiscore=0
    except FileNotFoundError:
        hiscore=0
    print(f"YOUR SCORE IS {score}")

    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
game()
