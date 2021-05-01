import random

def guess(x):
    random_num = random.randint(1, x) # Return a random number
    guess = 0

    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: ")) # Make it an integer
        if guess < random_num:
            print("Guess again, it's too low.")
        elif guess > random_num:
            print("Guess again, it's too high.")
    
    print(f"You have guessed the number {random_num}")

def comp_guess(x):
    low = 1
    high = x
    reply = ""

    while reply != "T" and low != high: # t = true
        guess = random.randint(low, high)
        reply = input(f"Is ${guess} too high (H), too low (L), or true(T)? ").lower()

        if reply == "h":
            high = guess - 1
        elif reply == "l":
            low = guess + 1
        
        
    print(f"The computer guesse your number, {guess}")

# guess(5) 
# comp_guess(5);