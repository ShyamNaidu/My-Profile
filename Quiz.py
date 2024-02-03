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
        print("Answer :")
        print(ans)
        print(f"You have answered {score} questions with " + str(round((score/qNo) * 100,2)) + "%")
        return False
        
print("Welcome to Computer Quiz!!!")
response = input("Do you want to answer few question? (Y/N) ")

if response.lower() == "y":
    print("Great! Let's start")
else:
    quit()

if not qBlock("Who developed Python Programming Language? ","guido van rossum"): quit()
if not qBlock("Which type of Programming does Python support? ","object-oriented, structured and functional programming"): quit()
if not qBlock("Is Python case sensitive when dealing with identifiers? ","yes"): quit()
if not qBlock("Which of the following is the correct extension of the Python file? ","py"): quit()
if not qBlock("Is Python code compiled or interpreted? ","python code is both compiled and interpreted"): quit()
if not qBlock("All keywords in Python are in _________","not case sensitive"): quit()
if not qBlock("What will be the value of the following Python expression? 4 + 3 % 5 ","7"): quit()
if not qBlock("What is used to define a block of code in Python language? ","Indentation"): quit()
if not qBlock("Which keyword is used for function in Python language? ","def"): quit()
if not qBlock("Which of the following character is used to give single-line comments in Python? ","#"): quit()
if not qBlock("Which of the following functions can help us to find the version of python that we are currently working on? ","sys.version"): quit()
if not qBlock("Python supports the creation of anonymous functions at runtime, using a construct called __________ ","lambda"): quit()
if not qBlock("What is the order of precedence in python? ","parentheses, exponential, multiplication, division, addition, subtraction"): quit()
if not qBlock("What will be the output of the following Python code snippet if x=1? code: x<<2 ","4"): quit()
if not qBlock("What does pip stand for python? ","Preferred Installer Program"): quit()
if not qBlock("What is the limit length of variable names in Python? ","unlimited length"): quit()
if not qBlock("Which of the following is the truncation division operator in Python? ","//"): quit()



print("Congrats! You have completed the quiz")
print(f"You have answered {score} questions with " + str(round((score/qNo) * 100,2)) + "%")

