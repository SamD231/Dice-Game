import random


def roll_dice():
    # Roll the dice and return the result
    return random.randint(1, 6)


def display_dice(num):
    # Display the dice with the given number of dots
    print("+-------+")
    if num == 1:
        print("|       |")
        print("|   •   |")
        print("|       |")
    elif num == 2:
        print("| •     |")
        print("|       |")
        print("|     • |")
    elif num == 3:
        print("| •     |")
        print("|   •   |")
        print("|     • |")
    elif num == 4:
        print("| •   • |")
        print("|       |")
        print("| •   • |")
    elif num == 5:
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
    else:
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
    print("+-------+")


def play_game():
    # Ask the player if they want to play
    play = input("Do you want to play? (y/n) ")

    # Loop until the player doesn't want to play anymore
    while play == "y":
        # Roll the dice for the player and computer
        player_roll = roll_dice()
        computer_roll = roll_dice()

        # Display the dice for the player and computer
        print("Your roll:")
        display_dice(player_roll)
        print("Computer's roll:")
        display_dice(computer_roll)

        # Determine the winner
        if player_roll > computer_roll:
            print("You win!")
        elif player_roll < computer_roll:
            print("The computer wins!")
        else:
            print("It's a tie!")

        # Ask the player if they want to play again
        play = input("Do you want to play again? (y/n) ")


# Call the play_game() function to start the game
play_game()
