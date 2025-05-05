# Task 1 - Variables: Your First Python Intro

# Creating variables to describe a person
name = "Jason"
age = 22
height = 5.10

# Printing a friendly message
print(f"Hey there, my name is {name}! I’m {age} years old and {height} feet tall.")

# Task 2 - Operators: Playing with Numbers

# Picking two numbers
num1 = 15
num2 = 4

# Addition
print("The sum of", num1, "and", num2, "is", num1 + num2)

# Subtraction
print("When you subtract", num2, "from", num1, "you get", num1 - num2)

# Multiplication
print("Multiplying", num1, "and", num2, "gives", num1 * num2)

# Division
print("Dividing", num1, "by", num2, "results in", num1 / num2)

# Task 3 - Conditional Statements: The Number Checker

# Asking user to enter a number
user_input = input("Enter a number and I’ll tell you something cool about it: ")

# Convert the input to a number (float allows decimals)
number = float(user_input)

# Checking if the number is positive, negative, or zero
if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")
