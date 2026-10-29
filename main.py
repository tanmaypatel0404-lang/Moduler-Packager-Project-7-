# MODULAR & PACKAGER
# MULTI-UTILITY TOOLKIT

from modules import datetime_utils
from modules import math_utils
from modules import random_utils
from modules import uuid_utils

from toolkit import file_operation
from toolkit import utility_operations


# MODULE EXPLORER

def explore_modules():
    """Explore attributes of different modules using dir()."""

    while True:

        print("\n" + "=" * 50)
        print("          MODULE ATTRIBUTE EXPLORER")
        print("=" * 50)

        print("1. Explore datetime_utils")
        print("2. Explore math_utils")
        print("3. Explore random_utils")
        print("4. Explore uuid_utils")
        print("5. Explore file_operations")
        print("6. Explore utility_operations")
        print("7. Back to Main Menu")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAttributes of datetime_utils:")
            print(dir(datetime_utils))

        elif choice == "2":
            print("\nAttributes of math_utils:")
            print(dir(math_utils))

        elif choice == "3":
            print("\nAttributes of random_utils:")
            print(dir(random_utils))

        elif choice == "4":
            print("\nAttributes of uuid_utils:")
            print(dir(uuid_utils))

        elif choice == "5":
            print("\nAttributes of file_operations:")
            print(dir(file_operation))

        elif choice == "6":
            print("\nAttributes of utility_operations:")
            print(dir(utility_operations))

        elif choice == "7":
            break

        else:
            print("\nInvalid choice. Please try again.")


# MAIN MENU

def main():
    """Run the Multi-Utility Toolkit."""

    while True:

        print("\n" + "=" * 50)
        print("             MULTI-UTILITY TOOLKIT")
        print("=" * 50)

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Utility Operations (Custom Module)")
        print("7. Explore Module Attributes (dir())")
        print("8. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_utils.datetime_menu()

        elif choice == "2":
            math_utils.math_menu()

        elif choice == "3":
            random_utils.random_menu()

        elif choice == "4":
            uuid_utils.uuid_menu()

        elif choice == "5":
            file_operation.file_menu()

        elif choice == "6":
            utility_operations.utility_menu()

        elif choice == "7":
            explore_modules()

        elif choice == "8":
            print("\nThank you for using Multi-Utility Toolkit!")
            print("Program exited successfully.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")


# PROGRAM ENTRY POINT

if __name__ == "__main__":
    main()
