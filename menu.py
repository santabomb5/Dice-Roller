import app


def menu():
    while True:
        result = []

        print("=" * 10)
        print("Menu options:")
        print("1. Flip coins")
        print("2. Roll four sided dice")
        print("3. Roll six sided dice")
        print("4. Roll eight sided dice")
        print("5. Roll ten sided dice")
        print("6. Roll twelve sided dice")
        print("7. Roll twenty sided dice")
        print("8. Roll hundred sided dice")
        print("9. Roll percentile dice")
        print("0. Exit the program")
        print("=" * 10)
    
        menu_selection = input("Please select a number option from the list: ")

        match menu_selection:
            case '1':
                coin_selection = app.coin_num()
                result = app.coin_flip(coin_selection)
                print(result)
            case '2':
                dice_selection = app.dice_num()
                result = app.roll_dice(4, dice_selection)
                print(result)
            case '3':
                dice_selection = app.dice_num()
                result = app.roll_dice(6, dice_selection)
                print(result)
            case '4':
                dice_selection = app.dice_num()
                result = app.roll_dice(8, dice_selection)
                print(result)
            case '5':
                dice_selection = app.dice_num()
                result = app.roll_dice(10, dice_selection)
                print(result)
            case '6':
                dice_selection = app.dice_num()
                result = app.roll_dice(12, dice_selection)
                print(result)
            case '7':
                dice_selection = app.dice_num()
                result = app.roll_dice(20, dice_selection)
                print(result)
            case '8':
                dice_selection = app.dice_num()
                result = app.roll_dice(100, dice_selection)
                print(result)
            case '9':
                print("percentile")
            case '0':
                print("Exiting program now.\n")
                break
            case _:
                print(f"{menu_selection} is an invalid option. Please try again.\n")
                
        input("Press any key to continue...")