# Assignment: Hands on Python Data Structures

# Task 1: Working with Lists
print("Task 1: Lists")
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", fruits)

# Append a new fruit
fruits.append('fig')
print("After adding a fruit:", fruits)

# Remove one fruit
fruits.remove('apple')
print("After removing a fruit:", fruits)

# Reverse list using slicing
reversed_fruits = fruits[::-1]
print("Reversed list:", reversed_fruits)

# Task 2: Exploring Dictionaries
print("\nTask 2: Dictionaries")
me = {
    "name": "Jason",
    "age": 22,
    "city": "Columbus"
}

# Add a new key-value pair
me["favorite color"] = "Green"

# Update the city
me["city"] = "Chicago"

# Print keys and values
print("Keys:", ", ".join(me.keys()))
print("Values:", ", ".join(str(value) for value in me.values()))

# Task 3: Using Tuples
print("\nTask 3: Tuples")
favorites = ("Inception", "Bohemian Rhapsody", "1984")
print("Favorite things:", favorites)

# Attempt to modify a tuple element
try:
    favorites[0] = "The Matrix"
except TypeError:
    print("Oops! Tuples cannot be changed.")

# Print length of tuple
print("Length of tuple:", len(favorites))