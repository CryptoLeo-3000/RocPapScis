import random

def rps():
    cpu = ["rock","scissor","paper"]
    cp = 0
    pp = 0
    k = int(input("How many rounds of Rock, Paper, Scissor do you want to play?\n"))
    print("Enter Rock, Paper, Scissor")
    print("You will get only three turns")
    print("Enter you choice")
    while k != 0:
        n = random.randint(0,2)
        choice = cpu[n]
        player = input("->").lower()
        print(f"{choice}\t{player}")
        if choice == "rock" and player == "paper":
            pp = pp + 1
        elif choice == "rock" and player == "scissor":
            cp = cp + 1
        elif choice == "scissor" and player == "rock":
            pp = pp + 1
        elif choice == "scissor" and player == "paper":
            cp = cp + 1
        elif choice == "paper" and player == "rock":
            cp = cp + 1
        elif choice == "paper" and player == "scissor":
            pp = pp + 1
        k = k - 1
    
    print(f"Computer Points = {cp}\nPlayer points = {pp}")
    if cp > pp:
        print("Computer Wins")
    elif pp > cp:
        print("You Win!!")
    else:
        print("It's a draw")

    again = input("Do you want to play again?").lower()
    if again == "y" or again == "yes":
        rps()

rps()