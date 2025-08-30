import sqlite3
import datetime
import matplotlib.pyplot as plt
# Database

#sqlite connection

conn = sqlite3.connect("budget.db")
cursor = conn.cursor()

#transactions table

cursor.execute(""" 
                CREATE TABLE transactions1 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                amount REAL,
                category TEXT,
                date TEXT
                 ) """)  
conn.commit()

# Functions

def add_transaction(t_type, amount, category):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO transactions(type, amount, category, date) VALUES (?, ?, ?, ?)",
                   (t_type, amount, category, date))
    conn.commit()
    print(f"{t_type.capitalize()} of {amount} added  in category '{category}'")

def show_balance():
    cursor.execute("SELECT SUM (CASE WHEN type='income' THEN amount ELSE -amount END) FROM transactions")
    balance = cursor.fetchone()[0]
    print(f"\nCurrent Balance: {balance if balance else 0:.2f}\n")

def show_transactions():
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    print("\n--- All Transactions ---")
    for row in rows:
        print(row)
    print("------------------------\n")

# Menu
def menu():
    while True: 
        print("==== Budget Tracker ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Transactions")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter category (e.g., Salary, Gift): ")
            add_transaction("income", amount, category)

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter category (e.g., Food, Rent): ")
            add_transaction("expense", amount, category)

        elif choice == "3":
            show_balance()

        elif choice == "4":
            show_transactions()

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run App
menu()
conn.close()