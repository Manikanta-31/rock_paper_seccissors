#rock paper scissors game

import random
print("welcome to the game.")
user = input("type your name here: ")
print("hello", user, "lets start the game choose one")
print("to stop the game type 'quit' ")

while True:
    player = input("rock,paper,scissors? : ")
    computer = random.choice(['rock','paper','scissors'])

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("you lose!", computer, "covers", player)
        else:
            print("you win", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("you lose!", computer, "cuts", player)
        else:
            print("you win",player,"covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("you lose!", computer, "smashes", player)
        else:
            print("you win", player, "cut", computer)
    elif player == "quit":
        print("thanks for playing see you again ")
        break

    else:
         print("check your spelling!")

