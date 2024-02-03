qNo = 1
score = 0

def qBlock(ques,ans):
    global qNo
    global score
    response = input(ques)
    if response.lower() == ans:
        print("You are correct. Here is your next question")
        qNo += 1
        score += 1
        return True
    else:
        print("You are wrong :(")
        print(f"You have answered {score} questions with " + str(round((score/qNo) * 100,2)) + "%")
        return False
        
print("Welcome to Computer Quiz!!!")
response = input("Do you want to answer few question? (Y/N) ")

if response.lower() == "y":
    print("Great! Let's start")
else:
    quit()

if not qBlock("What is the full form of CPU? ","central processing unit"): quit()
if not qBlock("What is the full form of RAM? ","random access memory"): quit()

print("Congrats! You have completed the quiz")
print(f"You have answered {score} questions with " + str(round((score/qNo) * 100,2)) + "%")

