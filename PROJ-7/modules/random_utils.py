# RANDOM DATA UTILITIES

import random
import string

# RANDOM NUMBER

def generate_random_number():
    """Generate a random number within a given range."""

    try:
        minimum = int(input("\nEnter minimum value: "))
        maximum = int(input("Enter maximum value: "))

        if minimum > maximum:
            print("Minimum cannot be greater than maximum.")
            return

        number = random.randint(minimum, maximum)

        print(f"\nRandom Number: {number}")

    except ValueError:
        print("Please enter valid integers.")

# RANDOM LIST


def generate_random_list():
    """Generate a list of random numbers."""

    try:
        size = int(input("\nEnter list size: "))
        minimum = int(input("Enter minimum value: "))
        maximum = int(input("Enter maximum value: "))

        if size <= 0:
            print("List size must be positive.")
            return

        if minimum > maximum:
            print("Minimum cannot be greater than maximum.")
            return

        random_list = [
            random.randint(minimum, maximum)
            for _ in range(size)
        ]

        print("\nRandom List:")
        print(random_list)

    except ValueError:
        print("Please enter valid integers.")

# RANDOM PASSWORD

def generate_password():
    """Generate a random password."""

    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            return

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Please enter a valid length.")


# RANDOM OTP


def generate_otp():
    """Generate a random six-digit OTP."""

    otp = random.randint(100000, 999999)

    print(f"\nGenerated OTP: {otp}")


# RANDOM SAMPLING

def random_sampling():
    """Select random items from a predefined dataset."""

    data = [
        "Apple",
        "Banana",
        "Mango",
        "Orange",
        "Grapes",
        "Watermelon",
        "Pineapple",
        "Papaya"
    ]

    print("\nAvailable Dataset:")
    print(data)

    try:
        size = int(input("\nEnter sample size: "))

        if size <= 0:
            print("Sample size must be positive.")
            return

        if size > len(data):
            print(
                f"Sample size cannot exceed {len(data)}."
            )
            return

        sample = random.sample(data, size)

        print("\nRandom Sample:")
        print(sample)

    except ValueError:
        print("Please enter a valid number.")


# NUMBER GUESSING GAME

def guessing_game():
    """Run a simple number guessing game."""

    secret_number = random.randint(1, 10)

    print("\nGuess the number between 1 and 10.")

    try:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed correctly.")
        else:
            print(
                f"Wrong guess! The number was {secret_number}."
            )

    except ValueError:
        print("Please enter a valid number.")

# RANDOM MENU

def random_menu():
    """Display random data generation menu."""

    while True:

        print("\n" + "=" * 45)
        print("           RANDOM DATA GENERATION")
        print("=" * 45)

        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Dataset Sampling")
        print("6. Number Guessing Game")
        print("7. Back to Main Menu")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_random_number()

        elif choice == "2":
            generate_random_list()

        elif choice == "3":
            generate_password()

        elif choice == "4":
            generate_otp()

        elif choice == "5":
            random_sampling()

        elif choice == "6":
            guessing_game()

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")


# MAIN CHECK


if __name__ == "__main__":
    random_menu()