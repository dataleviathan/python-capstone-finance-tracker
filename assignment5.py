# Assignment: Exploring String Methods

# Task 1: String Slicing and Indexing
print("--- Task 1: String Slicing and Indexing ---")
text = "Python is amazing!"

first_word = text[:6]
amazing_part = text[10:17]
reversed_text = text[::-1]

print("First word:", first_word)
print("Amazing part:", amazing_part)
print("Reversed string:", reversed_text)

# Task 2: String Methods
print("\n--- Task 2: String Methods ---")
s = " hello, python world! "

print("Original string:", repr(s))
print("After strip():", s.strip())
print("After capitalize():", s.strip().capitalize())
print("After replace():", s.strip().replace("world", "universe"))
print("After upper():", s.strip().upper())

# Task 3: Check for Palindromes
print("\n--- Task 3: Palindrome Checker ---")
word = input("Enter a word: ")

if word == word[::-1]:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is not a palindrome.")
