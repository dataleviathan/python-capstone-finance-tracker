# Project: Calculator with Exception Handling
import logging

# Setup logging to a file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

# Function to get a valid number
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e}")

# Main calculator loop
def calculator():
    while True:
        print("\nWelcome to the Error-Free Calculator!")
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("> ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            try:
                if choice == '1':
                    result = num1 + num2
                    print(f"Result: {result}")
                elif choice == '2':
                    result = num1 - num22
                    
                    print(f"Result: {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"Result: {result}")
                elif choice == '4':
                    result = num1 / num2
                    print(f"Result: {result}")

            except ZeroDivisionError as e:
                print("Oops! Division by zero is not allowed.")
                logging.error(f"ZeroDivisionError occurred: {e}")

            except Exception as e:
                print("An unexpected error occurred.")
                logging.error(f"Unexpected error: {e}")

            else:
                print("Calculation completed successfully!")

            finally:
                print("Returning to the main menu...\n")
        else:
            print("Invalid option. Please select a number from 1 to 5.")

# Run the calculator
calculator()