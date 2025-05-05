# Assignment: Check Your Knowledge on Errors

# Task 1: Understanding Python Exceptions
print("Task 1: Divide 100 by User Input")

while True:
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"100 divided by {num} is {result}")
        break

# Task 2: Types of Exceptions
print("\nTask 2: Intentional Exceptions")

# IndexError: accessing out-of-range index
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError: accessing a missing key in a dictionary
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError: adding incompatible types
try:
    result = "Hello" + 5
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

# Task 3: try...except...else...finally
print("\nTask 3: Robust Division")

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    division = a / b
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter numeric values.")
else:
    print(f"The result is {division}")
finally:
    print("This block always executes.")
