# UTILITY OPERATIONS

import math


# CHECK PRIME NUMBER

def check_prime():
    """Check whether a number is prime."""

    try:
        number = int(input("\nEnter a number: "))

        if number < 2:
            print(f"{number} is not a prime number.")
            return

        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                print(f"{number} is not a prime number.")
                return

        print(f"{number} is a prime number.")

    except ValueError:
        print("Please enter a valid integer.")


# CHECK PALINDROME

def check_palindrome():
    """Check whether a string is a palindrome."""

    text = input("\nEnter a word or text: ")

    cleaned_text = text.replace(" ", "").lower()

    if cleaned_text == cleaned_text[::-1]:
        print("The given text is a palindrome.")
    else:
        print("The given text is not a palindrome.")


# CALCULATE GCD

def calculate_gcd():
    """Calculate the greatest common divisor."""

    try:
        first = int(input("\nEnter first number: "))
        second = int(input("Enter second number: "))

        result = math.gcd(first, second)

        print(f"\nGCD of {first} and {second}: {result}")

    except ValueError:
        print("Please enter valid integers.")


# CALCULATE LCM

def calculate_lcm():
    """Calculate the least common multiple."""

    try:
        first = int(input("\nEnter first number: "))
        second = int(input("Enter second number: "))

        if first == 0 or second == 0:
            print("LCM cannot be calculated for zero.")
            return

        result = abs(first * second) // math.gcd(first, second)

        print(f"\nLCM of {first} and {second}: {result}")

    except ValueError:
        print("Please enter valid integers.")


# CALCULATE POWER

def calculate_power():
    """Calculate the power of a number."""

    try:
        number = float(input("\nEnter base number: "))
        exponent = float(input("Enter exponent: "))

        result = math.pow(number, exponent)

        print(f"\nResult: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# UTILITY MENU

def utility_menu():
    """Display utility operations menu."""

    while True:

        print("\n" + "=" * 45)
        print("           UTILITY OPERATIONS")
        print("=" * 45)

        print("1. Check Prime Number")
        print("2. Check Palindrome")
        print("3. Calculate GCD")
        print("4. Calculate LCM")
        print("5. Calculate Power")
        print("6. Back to Main Menu")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            check_prime()

        elif choice == "2":
            check_palindrome()

        elif choice == "3":
            calculate_gcd()

        elif choice == "4":
            calculate_lcm()

        elif choice == "5":
            calculate_power()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


# MAIN CHECK

if __name__ == "__main__":
    utility_menu()