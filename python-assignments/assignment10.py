# Project: About Menu - Recursion in Action
import turtle

# Factorial Function (Recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci Function (Recursive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Bonus: Recursive Fractal Tree
def draw_fractal_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def start_fractal():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)
    t.speed(1)
    draw_fractal_tree(75, t)
    screen.mainloop()

# Input Helper with Validation
def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0:
                return num
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Menu Program
def main_menu():
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci Number")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            n = get_positive_int("Enter a number to find its factorial: ")
            print(f"The factorial of {n} is {factorial(n)}.")

        elif choice == '2':
            n = get_positive_int("Enter the position of the Fibonacci number: ")
            print(f"The {n}th Fibonacci number is {fibonacci(n)}.")

        elif choice == '3':
            print("Drawing fractal tree... close the window to continue.")
            start_fractal()

        elif choice == '4':
            print("Thanks for exploring recursion! Goodbye")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")

# Start the program
main_menu()
