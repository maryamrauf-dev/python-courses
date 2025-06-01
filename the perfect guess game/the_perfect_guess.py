from random import randint;
def guess_game():
    number=randint(1,100)
    attempts=0
    while True:
        your_guess=int(input("Enter your guess: "))
        attempts+=1
        if(your_guess>number):
            print("Lower number please....")
        elif(your_guess<number):
            print("Higher number please....")
        else:
            print("You guessed it right....")
            break
    print(f"\t \t Finally! You guessed it in ",attempts,"tries")
guess_game()
