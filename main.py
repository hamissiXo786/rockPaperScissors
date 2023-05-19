import  random
"""this is a classic game of rock paper scissors"""

import random, time, sys
print(""" Rock paper scissors by Hamissi
rock beats scissors
scissors beats paper
paper beats rock 
""")

wins = 0
losses = 0
ties = 0

while True:
    while True:
        print("{} Wins, {} Losses,{}Ties".format(wins, losses, ties))
        print("enter your move: (R)ock (P)aper or (S)cissors or (Q)uit")
        playerMove = input(" > ")
        if playerMove == "Q":
            print("Thanks for playing!")
            sys.exit()

        if playerMove == "R" or playerMove == "P" or playerMove == "S":
            break
        else:
            print("Type one of, R, P, S, or Q")

    # Display what the player chose:
    if playerMove == "R":
        print("ROCK versus....")
        playerMove = "ROCK"
    elif playerMove == "P":
        print("PAPER versus...")
        playerMove = "PAPER"
    elif playerMove == "S":
        print("SCISSORS versus...")
        playerMove = "SCISSORS"
    # Count to threee with dramatic pauses:
    time.sleep(0.5)
    print("1....")
    time.sleep(0.25)
    print("2......")
    time.sleep(0.25)
    print("3......")
    time.sleep(0.25)

    #Dislplay what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "ROCK"
    elif randomNumber == 2:
        computerMove = "PAPER"
    elif randomNumber == 3:
        computerMove = "SCISSORS"
    print(computerMove)
    time.sleep(0.5)

    #Display and record the win/loss/tie:
    if playerMove == computerMove:
        print("it's a tie!")
        ties = ties + 1
    elif playerMove == "ROCK" and computerMove == "SCISSORS":
        print("You Win!!")
        wins += 1
    elif playerMove == "PAPER" and computerMove == "ROCK":
        print("You Win!!")
        wins += 1
    elif playerMove == "SCISSORS" and computerMove == "PAPER":
        print("You Win!!")
        wins += 1
    elif playerMove == "ROCK" and computerMove == "PAPER":
        print("You lose!!")
        losses += 1
    elif playerMove == "PAPER" and computerMove == "SCISSORS":
        print("You lose!!")
        losses += 1
    elif playerMove == "SCISSORS" and computerMove == "ROCK":
        print("You loser!!")
        losses += 1