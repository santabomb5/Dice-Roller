# Project title: Dice Roller
# Name: Jackson A. Kelley
# Email: jacksonkelley13@gmail.com
# Url: https://github.com/santabomb5/Dice-Roller
# Description: This program will allow you to roll a specified number and type of dice.
#     The goal is to aid tabletop gamers with required dice rolls or decision making.
#     The application can handle dice rolls from a range of d4 to d100. As well as
#     support for coinflips and percentile dice rolls.
# 
# The eventual goal of this project is to produce an opensource mobile app that can
# be used in any tabletop environment.


import menu
import random


def dice_num():
    try:
        num_choice = int(input("How many dice would you like to roll? "))
    except ValueError:
        num_choice = 0
    return num_choice


def coin_num():
    try:
        num_choice = int(input("How many coins would you like to flip? "))
    except ValueError:
        num_choice = 0
    return num_choice


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


def percentile():
    dice_one = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
    dice_two = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    digit_one = random.choice(dice_one)
    digit_two = random.choice(dice_two)
    percentage = int(digit_one) + int(digit_two)

    # The result of percentile dice can only be non-zero
    # so the result of a 00 combined with a 0 roll is 100%
    if percentage == 0:
        percentage = 100

    return tuple([digit_one, digit_two, percentage])
    

if __name__ == "__main__":
    menu.menu()