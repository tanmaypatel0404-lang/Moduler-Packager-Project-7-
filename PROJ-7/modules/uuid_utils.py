# UUID UTILITIES

import uuid


# GENERATE UUID4

def generate_uuid4():
    """Generate a random UUID4 identifier."""

    unique_id = uuid.uuid4()

    print("\nGenerated UUID4:")
    print(unique_id)


# GENERATE MULTIPLE UUIDs

def generate_multiple_uuids():
    """Generate multiple unique UUID4 identifiers."""

    try:
        count = int(input("\nHow many UUIDs do you want to generate? "))

        if count <= 0:
            print("Please enter a positive number.")
            return

        print("\nGenerated UUIDs:")

        for number in range(1, count + 1):
            unique_id = uuid.uuid4()
            print(f"{number}. {unique_id}")

    except ValueError:
        print("Please enter a valid number.")


# UUID MENU

def uuid_menu():
    """Display UUID operations menu."""

    while True:

        print("\n" + "=" * 45)
        print("          UUID OPERATIONS")
        print("=" * 45)

        print("1. Generate UUID4")
        print("2. Generate Multiple UUIDs")
        print("3. Back to Main Menu")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_uuid4()

        elif choice == "2":
            generate_multiple_uuids()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


# MAIN CHECK

if __name__ == "__main__":
    uuid_menu()