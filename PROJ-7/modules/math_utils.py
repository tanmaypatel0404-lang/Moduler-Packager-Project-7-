# ============================================================
# MATHEMATICAL UTILITIES
# ============================================================

import math

# FACTORIAL


def calculate_factorial():
    """Calculate factorial of a number."""

    try:
        number = int(input("\nEnter a number: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return

        result = math.factorial(number)

        print(f"Factorial of {number}: {result}")

    except ValueError:
        print("Please enter a valid integer.")


# COMPOUND INTEREST

def calculate_compound_interest():
    """Calculate compound interest."""

    try:
        principal = float(input("\nEnter principal amount: "))
        rate = float(input("Enter rate of interest (%): "))
        years = float(input("Enter time (in years): "))

        amount = principal * (1 + rate / 100) ** years
        interest = amount - principal

        print(f"\nCompound Interest: {interest:.2f}")
        print(f"Final Amount: {amount:.2f}")

    except ValueError:
        print("Please enter valid numbers.")

# TRIGONOMETRIC CALCULATIONS


def trigonometric_calculations():
    """Perform trigonometric calculations."""

    try:
        angle = float(input("\nEnter angle in degrees: "))

        radians = math.radians(angle)

        print(f"\nsin({angle}) = {math.sin(radians):.4f}")
        print(f"cos({angle}) = {math.cos(radians):.4f}")
        print(f"tan({angle}) = {math.tan(radians):.4f}")

    except ValueError:
        print("Please enter a valid angle.")


# AREA OF SHAPES

def area_of_shapes():
    """Calculate area of different geometric shapes."""

    print("\nArea of Geometric Shapes")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":

            radius = float(input("Enter radius: "))

            if radius < 0:
                print("Radius cannot be negative.")
                return

            area = math.pi * radius ** 2

            print(f"Area of Circle: {area:.2f}")

        elif choice == "2":

            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            if length < 0 or width < 0:
                print("Length and width cannot be negative.")
                return

            area = length * width

            print(f"Area of Rectangle: {area:.2f}")

        elif choice == "3":

            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            if base < 0 or height < 0:
                print("Base and height cannot be negative.")
                return

            area = 0.5 * base * height

            print(f"Area of Triangle: {area:.2f}")

        elif choice == "4":

            side = float(input("Enter side: "))

            if side < 0:
                print("Side cannot be negative.")
                return

            area = side ** 2

            print(f"Area of Square: {area:.2f}")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numbers.")


# LOGARITHM


def calculate_logarithm():
    """Calculate natural and base-10 logarithms."""

    try:
        number = float(input("\nEnter a positive number: "))

        if number <= 0:
            print("Number must be positive.")
            return

        print(f"Natural Log: {math.log(number):.4f}")
        print(f"Log Base 10: {math.log10(number):.4f}")

    except ValueError:
        print("Please enter a valid number.")


# MATH MENU

def math_menu():
    """Display mathematical operations menu."""

    while True:

        print("\n" + "=" * 45)
        print("          MATHEMATICAL OPERATIONS")
        print("=" * 45)

        print("1. Calculate Factorial")
        print("2. Calculate Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Calculate Logarithm")
        print("6. Back to Main Menu")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_factorial()

        elif choice == "2":
            calculate_compound_interest()

        elif choice == "3":
            trigonometric_calculations()

        elif choice == "4":
            area_of_shapes()

        elif choice == "5":
            calculate_logarithm()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


# MAIN CHECK


if __name__ == "__main__":
    math_menu()