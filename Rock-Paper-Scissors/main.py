import random

def play():
    user = input("'r' for rock, 'p' for paper and 's' for scissors\n") # Asking user for an input
    computer = random.choice(['r', 'p', 's']) # Return random rock, paper or scissors

    if user == computer:
        return "tie" # If user and computer get the same then it's a tie

    if is_win(user, computer):
        return "You won the game!"

    return "You lost"

def is_win(player_1, player_2):
    if (player_1 == 'r' and player_2 == 's') or (player_1 == 's' and player_2 == 'p') or (player_1 == 'p' and player_2 == 'r'): # Use conditional for check
        return True

print(play())