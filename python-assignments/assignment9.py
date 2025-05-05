# Assignment: Functions and Recursion

# Task 1: Writing Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(a, b):
    return a + b

greet_user("Alice")
print("The sum of 5 and 10 is", add_numbers(5, 10))

# Task 2: Using Default Parameters
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Task 3: Variable Arguments
def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")

make_sandwich("Lettuce", "Tomato", "Cheese")

# Task 4: Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFactorial of 5 is {factorial(5)}.")
print(f"The 6th Fibonacci number is {fibonacci(6)}.")