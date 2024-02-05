import random

user_wins = 0
computer_wins = 0
options = ["rock","scissors","paper"]

while True:
    user_input = input("Type Rock/Scissors/Paper or Q for quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    rand_number = random.randint(0,2)
    #rock = 0, scissors = 1, paper = 3
    computer_pick = options[rand_number]
    print("Computer Picked", computer_pick + ",")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!!")
        user_wins += 1
    else:
        print("Computer Won!!")
        computer_wins += 1

print("You won ", user_wins , " times")
print("Computer won " , computer_wins , " times")
print("Good Bye")
