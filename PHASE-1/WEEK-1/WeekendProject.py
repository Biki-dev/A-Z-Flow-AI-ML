"""
Weekend Project: CLI Expense Tracker. Build a command-line application that asks the user for expenses,
stores them in a JSON file, and can print out a summary by category.
"""

import json
import uuid
from datetime import datetime

def loaddata():
    try:
        with open("expences.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    except json.JSONDecodeError:
        print("Invalid JSON")
        expenses = []
    return expenses

def savedata(amount, category, description):
    expenses = loaddata()
    data = {
        "id": str(uuid.uuid4()),
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    expenses.append(data)
    with open("expences.json", "w") as file:
        json.dump(expenses, file, indent=4)

def ask():
    number_of_expense = int(input("Total Expense: "))
    for i in range(1, number_of_expense + 1):
        
        suffix = "st" if i == 1 else "nd" if i == 2 else "rd" if i == 3 else "th"
        amount_input = float(input(f"Enter {i}{suffix} amount (e.g., 12.50): "))
        category_input = input(f"Enter {i}{suffix} Category: ")
        discription_input = input(f"Enter {i}{suffix} Description: ")
        
        savedata(amount_input, category_input, discription_input)
    
ask()
