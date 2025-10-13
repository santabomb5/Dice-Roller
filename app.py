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


def dice_num():
    return int(input("How many dice would you like to roll? "))


def coin_num():
    return int(input("How many coins would you like to flip? "))


def coin_flip(coin_num):
    coin_list = []
    choices = ["heads", "tails"]

    if coin_num == 0:
            return "Oops! You selected to flip zero coins."
    elif coin_num == 1:
        coin_list.append(random.choice(choices))
        return coin_list
    else:
        for coin in range(coin_num):
            coin_list.append(random.choice(choices))
        return tuple(coin_list)

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