import random

initial_value = 1
head_count = 0
tail_count = 0

while int(initial_value) > 0:
    x = input("Head or Tail? ")
    print("You choose " + x) 

    shuffle = random.choice(["Head", "Tail"])
    print(shuffle)
