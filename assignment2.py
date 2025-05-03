# Eligible Elector Program
# This program checks if a user is old enough to vote.

# Step 1: Ask for the user's age
age = int(input("How old are you? "))

# Step 2: Determine voter eligibility using conditionals
if age >= 18:
    print("🎉 Congratulations! You are eligible to vote. Go make a difference!")
else:
    years_left = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {years_left} more year(s) to go!")
