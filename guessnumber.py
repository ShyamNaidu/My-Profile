import random

guess = input("Guess a No between 0 to 10: ")
r = random.randrange(10)

if int(guess) == r:
    print("Hurray! Your guess is absolutely correct")
else:
    print(f"Oops. it's {r}. Better luck next time")