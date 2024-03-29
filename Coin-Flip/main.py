import random

# Initialize the initial value
initial_value = 1
head_count = 0
tail_count = 0

while int(initial_value) > 0: # If it is true then it will keep running
    x = input("Head or Tail? \n") # Calling user for an input
    print("You choose " + x)

    shuffle = random.choice(["Head", "Tail"]) # Return "Head" or "Tail"
    print("Head & Tail output by machine is: " + shuffle)

    if (x == shuffle):
        print(x + " and " + shuffle + " are the same")
    else: 
        print(x + " and " + shuffle + " are not the same")

    if (x == shuffle):
        head_count += 1
        tail_count += 1
    else:
        head_count -= 1
        tail_count -= 1

    print("Head count is " + str(head_count) + " and " + " ," + "Tail count is " + str(tail_count))
    initial_value = input("To play again type more than 1 else less than 0 \n") # To end the game
