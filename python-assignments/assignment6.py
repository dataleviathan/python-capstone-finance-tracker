# Password Strength Checker

import string

# Step 1: Get password from user
password = input("Enter a password to check its strength: ")

# Step 2: Define checks
length_check = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

# Step 3: Generate feedback
issues = []

if not length_check:
    issues.append("at least 8 characters")
if not has_upper:
    issues.append("an uppercase letter")
if not has_lower:
    issues.append("a lowercase letter")
if not has_digit:
    issues.append("a digit")
if not has_special:
    issues.append("a special character (e.g. @, #, $)")

# Step 4: Print result
if not issues:
    print("Your password is strong!")
else:
    print("Your password needs:", ", ".join(issues))

# Bonus: Strength meter (score out of 10)
score = 0
if length_check: score += 2
if has_upper: score += 2
if has_lower: score += 2
if has_digit: score += 2
if has_special: score += 2

print(f"Password strength score: {score}/10")