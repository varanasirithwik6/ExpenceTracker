import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Initialize CSV file if not exists
def initialize_file():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., Food, Travel, Bills): ")
    amount = float(input("Enter amount: ₹"))
    desc = input("Enter description: ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, desc])

    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Date: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]} | Note: {row[3]}")
    except FileNotFoundError:
        print("❌ No expenses found. Add some first!")

def total_expense():
    total = 0
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                total += float(row[2])
        print(f"\n💰 Total Spent: ₹{total}")
    except FileNotFoundError:
        print("❌ No data available!")

def delete_all():
    confirm = input("⚠️ Are you sure you want to delete all records? (y/n): ")
    if confirm.lower() == 'y':
        open(FILENAME, 'w').close()
        initialize_file()
        print("🗑️ All records deleted.")
    else:
        print("Operation cancelled.")

def main():
    initialize_file()
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Delete All Records")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            delete_all()
        elif choice == '5':
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter again.")

if __name__ == "__main__":
    main()
