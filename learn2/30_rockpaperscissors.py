import random

user_wins = 0
computer_wins = 0

options = ["rock" , "paper" , "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        #quit() #konczy program
        break #wychodzi z petli while

    if user_input not in options:
        continue #wraca na początek pętli

    random_number = random.randint(0,2)
    #rock:0, paper:1, scissors:2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" or computer_pick == "scissors":
        print("You won!")
        user_wins +=1
        continue

    elif user_input == "scissors" or computer_pick == "paper":
        print("You won!")
        user_wins +=1
        continue

    elif user_input == "paper" or computer_pick == "rock":
        print("You won!")
        user_wins +=1

    else:
        print("You Lost!")
        computer_wins +=1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")