import ast
from datetime import datetime

EXPENSE_FILE = "expenses.txt"
data=[]

def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        file.write(str(expenses))

def add_expense():
    date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (Food, Transport, etc.): ")
    amount = float(input("Enter amount: "))
    note = input("Optional note: ")

    expenses = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    data.append(str(expenses))
    save_expenses(data)
    print("✅ Expense added!")

def view_expenses():
    expenses = load_expenses()
    expenses_list = ast.literal_eval(expenses)
    print("\n--- Expense List ---")
    expenses_dict = [ast.literal_eval(item) for item in expenses_list]
    for exp in expenses_dict:
        print(f"Date: {exp['date']}, Category: {exp['category']}, Amount: ₹{exp['amount']}, Note: {exp['note']}")
    
def category_summary():
    expenses = load_expenses()
    expenses_list = ast.literal_eval(expenses)
    expenses_dict = [ast.literal_eval(item) for item in expenses_list]
    arr1=[]
    arr2=[]
    amount=0

    category_totals = {}
    for e in expenses_dict:
        cat = e['category']
        amt = e['amount']
        if cat in category_totals:
            category_totals[cat] += amt
        else:
            category_totals[cat] = amt

    arr1 = list(category_totals.values())  
    arr2 = list(category_totals.keys())    

    print("\n--- Summary ---")
    for c, a in category_totals.items():
        print(f"Category: {c}, Total Amount: ₹{a}")


def main():
    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            print("👋 Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
