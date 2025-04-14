#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 14, 2025
# This program adds all whole numbers from 0 to the number entered by the user.


def main():
    try:
        # Get user input and convert to integer
        user_number = int(input("Enter a positive whole number: "))

        # Check for negative input
        if user_number < 0:
            print("Invalid input. Number must be 0 or greater.")
        else:
            total = 0
            counter = 0

            # While loop to add numbers from 0 to user_number
            while counter <= user_number:
                total += counter
                counter += 1

            print(f"The sum of all whole numbers up to {user_number} is: {total}")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
