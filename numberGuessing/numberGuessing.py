# Number Guessing Game

import random

# Guess the number Human
def guess(x):
    num = random.randint(1, x)
    guess = None
    count = 0
    while guess != num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > num:
            print(f"Oops! {guess} is too high!")
        elif guess < num:
            print(f"Oops! {guess} is too low!")
        count += 1
    print(f"Yay Congrats! You guessed the number {guess}")
    print(f"You took {count} turns.")


# Guess the number Computer
def guessComputer(x):
    l = 1
    u = x
    guess = None
    status = None
    count = 0
    while status != 'c':
        guess = random.randint(l, u)
        status = input(f"Is {guess} too low(l), high(h) or correct(c): ")
        if status == 'l':
            l = guess + 1
        elif status == 'h':
            u = guess - 1
        count += 1
    print(f"Yay Congrats! You guessed the number {guess}")
    print(f"You took {count} turns.")


upper = int(input("Please enter the upper bound: "))
guessComputer(upper)