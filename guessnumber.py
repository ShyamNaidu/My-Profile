import random

#randrange: Return a randomly selected element from range(start, stop, step). Excludes top extreme values
#randrange: Return a randomly selected element from range(start, stop, step). Includes top extreme values
r = random.randrange(10)    # the range is 0 to 9
#r = random.randint(0,9)

# check if the entered value is a number and convert to int
# isdigit: Return True if all characters in the string are digits and there is at least one character, False otherwise.
guess = input("Guess a No between 0 to 10: ")
while True:
    if guess.isdigit():
        guess = int(guess)
        if guess >= 0 and guess <= 9:
            break
    guess = input("Wrong Entry... Please Enter correct number between 0 to 9: ")    



# while guess >= 0 and guess <= 9:
#     input("Wrong Entry... Please Enter correct number between 0 to 9: ")

# if guess.isdigit():
#     guess = int(guess)
# else:
#     print("Wrong Entry...")
#     quit()

# if guess < 0:
#     print("Wrong Entry...")
#     quit()    

# if guess > 9:
#     print("Wrong Entry...")
#     quit()


if int(guess) == r:
    print("Hurray! Your guess is absolutely correct")
elif int(guess) > r:
    print(f"Oops. it's {r}. You are above the number. Retry")
else:
    print(f"Oops. it's {r}. You are below the number. Retry")