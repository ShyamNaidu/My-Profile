print("Welcome to Computer Quiz!!!")

response = input("Do you want to answer a question? (Y/N) ")

if response == "y":
    print("Great! Let's start")
    answer = input("What is the full form of CPU? ")
    if answer == "Central Process Unit":
        print("You are correct. Thanks for playing")
    else:
        print("Wrong. Try again")


