from datetime import datetime


def get_valid_age():
    while True:
        try:
            age = int(input("Enter pet age: "))

            if age < 0:
                print("Age cannot be negative.")
            else:
                return age

        except ValueError:
            print("Please enter a valid number.")


def get_valid_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date

        except ValueError:
            print("Invalid date format. Try again.")


def display_heading(title):
    print("\n" + "=" * 30)
    print(title.center(30))
    print("=" * 30)
