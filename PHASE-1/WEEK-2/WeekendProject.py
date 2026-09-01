"""
Weekend Project: OOP CLI Expense Tracker. Refactor your Week 1 
Expense Tracker using OOP by creating an Expense class and an 
ExpenseManager class. The application should add expenses, store 
them in a JSON file, load existing expenses, display all expenses, 
and print a summary of total expenses by category.
"""

import json
import uuid
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")
        
    def to_dict(self):
        return{
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }
class ExpenseManager:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_data()
        
    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Invalid JSON file.")
            return []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)
            
    def add_expense(self, amount, category, description):
        expense = Expense(
            amount,
            category,
            description
        )

        self.expenses.append(expense.to_dict())
        self.save_data()

        print("Expense added successfully!")
        
    def show_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("\n--- Expenses ---")

        for expense in self.expenses:
            print(f"ID: {expense['id']}")
            print(f"Amount: ₹{expense['amount']:.2f}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Date: {expense['date']}")
            print()

    def summary_by_category(self):
        summary = {}

        for expense in self.expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category not in summary:
                summary[category] = 0

            summary[category] += amount

        return summary

    def show_summary(self):
        summary = self.summary_by_category()

        if not summary:
            print("No expenses found.")
            return

        print("\n--- Expense Summary ---")

        for category, total in summary.items():
            print(f"{category}: ₹{total:.2f}")


def main():
    manager = ExpenseManager()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")

                manager.add_expense(
                    amount,
                    category,
                    description
                )

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "2":
            manager.show_expenses()

        elif choice == "3":
            manager.show_summary()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
