import random

initial_value = 1
head_count = 0
tail_count = 0

while int(initial_value) > 0:
    x = input("Head or Tail?\n")
    print("You choose " + x)

    shuffle = random.choice(["Head", "Tail"])
    print("Head & Tail output by machine is: " + shuffle)

    if (x == shuffle):
        print(x + " and " + shuffle + " are the same")
    else: 
        print(x + " and " + shuffle + " are not the same")

    if (x ==  shuffle):
        head_count += 1
        tail_count += 1
    else:
        head_count -= 1
        tail_count -= 1

    print("Head count is " + str(head_count) + " and " + " ," + "Tail count is " + str(tail_count))
