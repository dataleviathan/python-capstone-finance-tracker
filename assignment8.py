# Project: Inventory Manager

# Step 1: Create the inventory
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

# Function to display inventory
def display_inventory():
    print("\nCurrent Inventory:")
    for item, (qty, price) in inventory.items():
        print(f"Item: {item}, Quantity: {qty}, Price: ${price}")
    print()

# Function to calculate total value
def total_inventory_value():
    total = sum(qty * price for qty, price in inventory.values())
    print(f"Total value of inventory: ${total:.2f}")

# Interactive Menu
print("Welcome to the Inventory Manager!")

while True:
    display_inventory()
    print("Options:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Update an item")
    print("4. View total inventory value")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter item name to add: ").lower()
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[item] = (qty, price)
        print(f"{item.title()} added successfully!")

    elif choice == '2':
        item = input("Enter item name to remove: ").lower()
        if item in inventory:
            del inventory[item]
            print(f"{item.title()} removed successfully.")
        else:
            print("Item not found.")

    elif choice == '3':
        item = input("Enter item name to update: ").lower()
        if item in inventory:
            qty = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[item] = (qty, price)
            print(f"{item.title()} updated successfully.")
        else:
            print("Item not found.")

    elif choice == '4':
        total_inventory_value()

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
