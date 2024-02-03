print("Welcome to Computer Quiz!!!")

response = input("Do you want to answer a question? (Y/N) ")

if response.lower() == "y":
    print("Great! Let's start")
else:
    quit()

answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("You are correct. Thanks for playing")
else:
    print("Wrong. Try again")


