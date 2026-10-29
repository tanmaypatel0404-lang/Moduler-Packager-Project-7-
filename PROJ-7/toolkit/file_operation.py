# FILE OPERATIONS

import os


# CREATE FILE

def create_file():
    """Create a new text file."""

    filename = input("\nEnter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "w") as file:
            content = input("Enter content for the file: ")
            file.write(content)

        print(f"\nFile '{filename}' created successfully.")

    except OSError as error:
        print(f"Error creating file: {error}")


# WRITE TO FILE

def write_to_file():
    """Write content to an existing file."""

    filename = input("\nEnter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    if not os.path.exists(filename):
        print("File does not exist.")
        return

    try:
        content = input("Enter content to write: ")

        with open(filename, "w") as file:
            file.write(content)

        print("Content written successfully.")

    except OSError as error:
        print(f"Error writing to file: {error}")


# READ FILE

def read_file():
    """Read and display file content."""

    filename = input("\nEnter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    if not os.path.exists(filename):
        print("File does not exist.")
        return

    try:
        with open(filename, "r") as file:
            content = file.read()

        print("\nFile Content:")
        print(content)

    except OSError as error:
        print(f"Error reading file: {error}")


# APPEND TO FILE

def append_to_file():
    """Append content to an existing file."""

    filename = input("\nEnter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    if not os.path.exists(filename):
        print("File does not exist.")
        return

    try:
        content = input("Enter content to append: ")

        with open(filename, "a") as file:
            file.write("\n" + content)

        print("Content appended successfully.")

    except OSError as error:
        print(f"Error appending to file: {error}")


# DELETE FILE

def delete_file():
    """Delete an existing file."""

    filename = input("\nEnter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    if not os.path.exists(filename):
        print("File does not exist.")
        return

    try:
        os.remove(filename)

        print(f"File '{filename}' deleted successfully.")

    except OSError as error:
        print(f"Error deleting file: {error}")


# LIST FILES

def list_files():
    """Display text files in the current directory."""

    try:
        files = [
            file for file in os.listdir()
            if file.endswith(".txt")
        ]

        if not files:
            print("\nNo text files found.")
            return

        print("\nAvailable Text Files:")

        for number, file in enumerate(files, start=1):
            print(f"{number}. {file}")

    except OSError as error:
        print(f"Error listing files: {error}")


# FILE MENU

def file_menu():
    """Display file operations menu."""

    while True:

        print("\n" + "=" * 45)
        print("           FILE OPERATIONS")
        print("=" * 45)

        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Append to File")
        print("5. Delete File")
        print("6. List Text Files")
        print("7. Back to Main Menu")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            write_to_file()

        elif choice == "3":
            read_file()

        elif choice == "4":
            append_to_file()

        elif choice == "5":
            delete_file()

        elif choice == "6":
            list_files()

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")


# MAIN CHECK

if __name__ == "__main__":
    file_menu()