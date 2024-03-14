import random

while True:
    userschoice=input("Enter your choice: ").lower()

    a=0
    b=0

    choices=["rock","paper","scissors"]
    x=str(random.sample(choices,k=1))
    x=x[2:-2]
    print(x)

    if userschoice in x:
        print("It's a tie")
    elif "rock" in x and "paper" in userschoice or "paper" in x and "scissors" in userschoice or "scissors" in x and "rock" in userschoice:
        print("Congratulations, You won!")
        a=+1 
        print("Your score:",a,"My score:",b)
    elif "scissors" in x and "paper" in userschoice or "rock" in x and "scissors" in userschoice or "paper" in x and "rock" in userschoice:
        print("You lost! Better luck next time.")
        b=+1
        print("Your score:",a,"My score:",b)

    else:
        print("Wrong input")
    
    z=input("Another game? \n y/n:")
    if z == "n":
        exit()