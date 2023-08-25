"""Number Guessing Game with hints.

Author: Hao Sun
Creation Date: 20/Aug/2023
"""

import random


def generate_random_number():
    """Generate a random four-digit number."""
    return str(random.randint(1000, 10000))


def get_hints(guess, number):
    """Return hints based on the guess and actual number.

    Args:
    - guess (str): The guessed number.
    - number (str): The actual number to guess.

    Returns:
    - list: A list of hints.
    """
    hints = []

    for i in range(4):
        if guess[i] == number[i]:
            hints.append("O")  # Append O for correctly positioned digits
        elif guess[i] in number:
            hints.append("x")  # Append x for correct digits in wrong position
        else:
            hints.append("-")  # Append '-' for completely wrong digits

    return hints


def play_game():
    """Main function to play the game."""
    welcome_message()
    number = generate_random_number()
    attempts = 0

    while True:
        guess = input("Guess a four-digit number or type 'quit' to exit: ")

        # Check if the user wants to quit
        if guess.lower() == 'quit':
            print(f"The number was {number}.")
            return

        # Validate guess
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid four-digit number.")
            continue

        attempts += 1

        if guess == number:
            print(
                "Congratulations! You guessed the number in "
                f"{attempts} attempts."
            )
            break
        hints = get_hints(guess, number)
        print(" ".join(hints))

    # Ask if the user wants to play again
    again = input("Do you want to play again? (yes/quit): ").lower()
    while again not in ['yes', 'quit']:
        print("Invalid input. Please enter 'yes' or 'quit'.")
        again = input("Do you want to play again? (yes/quit): ").lower()

    if again == 'yes':
        play_game()


def welcome_message():
    """Showing welcome message to player."""
    print("************** Welcome to the guess number game **************")
    print("* You are required to enter a four-digit number to guess it")
    print(
        "* You will get hints of X if the numbers are correct but in wrong "
        "places"
    )
    print(
        "* You will get hints of O if the numbers are correct and also in "
        "correct places"
    )
    print("* Any guessing number was not correct will shown as -")
    print("**************************************************************")


if __name__ == "__main__":
    play_game()
