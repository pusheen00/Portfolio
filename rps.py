from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

tie = 0
win = 0
lose = 0
player = input("Do you want to play Rock, Paper, Scissors?")
while player != "no":
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
        tie = tie + 1
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            lose = lose + 1
        else:
            print("You win!", player, "smashes", computer)
            win = win + 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            lose = lose + 1
        else:
            print("You win!", player, "covers", computer)
            win = win + 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            lose = lose + 1
        else:
            print("You win!", player, "cut", computer)
            win = win + 1
    else:
        print("That's not a valid play. Check your spelling!")
    computer = t[randint(0,2)]
else:
    print("score is... wins", win)
    print ("losses", lose)
    print("ties", tie)
