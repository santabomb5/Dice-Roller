# Write a program that simulates rolling a pair of dice. Each time the program 
# runs, it should randomly generate two numbers between 1 and 6 (inclusive), 
# representing the result of each die. The program should then display the 
# results and ask if the user would like to roll again.

# Optional Enhancements
# • Modify the program so the user can specify how many dice they want to roll.
# • Add a feature that keeps track of how many times the user has rolled the 
#   dice during the session. This will require a counter that increments each 
#   time the dice are rolled.


import menu
import random


def roll_dice(high, dice_num, low=1):
    dice_list = []

    if dice_num == 0:
        return "Oops! You selected to roll zero dice."
    elif dice_num == 1:
        return random.randint(low,high)
    else:
        for dice in range(dice_num):
            dice_list.append(random.randint(low, high))
        return tuple(dice_list)


if __name__ == "__main__":
    menu.menu()