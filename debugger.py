import random
import time

print("Let's play Rock Paper Scissors!")

# Challenge
# Find the bugs below:

while True:
    userInput = input("Do you want to play rock, paper, or scissors?\n").lower()
    computerSelection = random.choice(["rock", "paper", "scissors"])

    print(f"You played: {userInput} and the computer played: {computerSelection}")
    if userInput == computerSelection:
        print("It's a tie!")
        time.sleep(2)
    elif userInput == "rock" and computerSelection == "paper" or userInput == "paper" and computerSelection == "scissors" or userInput == "scissors" and computerSelection == "rock":
        print("You Lose!")
        time.sleep(2.5)
    else:
        print("You Win!")
        time.sleep(2.5)
        #I just wanted to try something
