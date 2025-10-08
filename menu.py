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
    
        dice_selection = 2
        menu_selection = input("Please select a number option from the list: ")

        match menu_selection:
            case '1':
                print("coin")
            case '2':
                print("d4")
            case '3':
                dice_selection = int(input("How many dice would you like to roll? "))
                result = app.roll_dice(6, dice_selection)
                print(result)
            case '4':
                print("d8")
            case '5':
                print("d10")
            case '6':
                print("d12")
            case '7':
                print("d20")
            case '8':
                print("d100")
            case '9':
                print("percentile")
            case '0':
                print("Exiting program now.\n")
                break
            case _:
                print(f"{menu_selection} is an invalid option. Please try again.\n")
                
        input("Press any key to continue...")