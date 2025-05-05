# finance_tracker.py
def print_welcome():
    print("Welcome to the Personal Finance Tracker!")

def add_expense(data):
    try:
        description = input("Enter expense description: ").strip()
        category = input("Enter category: ").strip()
        amount = float(input("Enter amount: "))

        if not description or not category:
            raise ValueError("Description and category cannot be empty.")

        if category not in data:
            data[category] = []
        data[category].append((description, amount))
        print("Expense added successfully.")
        
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_expenses(data):
    if not data:
        print("No expenses recorded yet.")
        return
    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary(data):
    if not data:
        print("No expenses to summarize.")
        return
    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amt for _, amt in expenses)
        print(f"{category}: ${total:.2f}")

def main():
    print_welcome()
    data = {}
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(data)
        elif choice == '2':
            view_expenses(data)
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()