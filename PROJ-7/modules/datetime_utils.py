
import datetime
import time


def datetime_menu():
    while True:
        print("\nDATETIME AND TIME OPERATIONS")
        print("1. Current date and time")
        print("2. Difference between two dates")
        print("3. Format current date")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            now = datetime.datetime.now()
            print("Current date and time:", now)

        elif choice == "2":
            try:
                date1 = input("Enter first date (YYYY-MM-DD): ")
                date2 = input("Enter second date (YYYY-MM-DD): ")

                d1 = datetime.date.fromisoformat(date1)
                d2 = datetime.date.fromisoformat(date2)

                print("Difference:", abs((d2 - d1).days), "days")
            except ValueError:
                print("Please enter valid dates.")

        elif choice == "3":
            now = datetime.datetime.now()
            print(now.strftime("%d-%m-%Y %I:%M %p"))

        elif choice == "4":
            input("Press Enter to start...")
            start = time.time()
            input("Press Enter to stop...")
            print("Elapsed time:", round(time.time() - start, 2), "seconds")

        elif choice == "5":
            try:
                seconds = int(input("Enter seconds: "))
                if seconds < 0:
                    print("Enter a non-negative number.")
                    continue

                while seconds > 0:
                    print(seconds)
                    time.sleep(1)
                    seconds -= 1

                print("Time is up!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    datetime_menu()
