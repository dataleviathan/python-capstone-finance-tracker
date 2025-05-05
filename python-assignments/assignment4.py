# Number Guessing Game
import random

# Step 1: Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

# Step 2: Loop until the user guesses correctly or runs out of attempts
while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.\n")
    elif guess > number_to_guess:
        print("Too high! Try again.\n")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        break
else:
    print(f"Game over! The number was {number_to_guess}. Better luck next time!")