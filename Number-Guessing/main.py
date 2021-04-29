import random

def guess(x):
    random_num = random.randint(1, x); # Return a random number
    guess = 0

    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: ")) # Make it an integer
        if guess < random_num:
            print("Guess again, it's too low.")
        elif guess > random_num:
            print("Guess again, it's too high.")
    
    print(f"You have guessed the number {random_num}")

guess(5)