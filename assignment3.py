# Assignment: Explore Loops in Python

# Task 1: Countdown Timer
print("\n--- Task 1: Countdown ---")
start = int(input("Enter the starting number for the countdown: "))
while start > 0:
    print(start, end=" ")
    start -= 1
print("Blast off!")

# Task 2: Multiplication Table
print("\n\n--- Task 2: Multiplication Table ---")
num = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Task 3: Factorial
print("\n\n--- Task 3: Factorial ---")
factorial_input = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, factorial_input + 1):
    factorial *= i
print(f"The factorial of {factorial_input} is {factorial}.")