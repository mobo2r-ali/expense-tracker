from datetime import datetime
import csv
from colorama import Fore

expenses = []


def add_expense():
    try:
        amount = float(input(Fore.MAGENTA+"enter amount: "))

        if amount <= 0:
            print(Fore.RED+"amount must be greater than zero.")
            return

    except ValueError:
        print(Fore.RED+"please enter a valid number.")
        return

    category = input(Fore.BLUE+"enter category: ")
    description = input(Fore.BLUE+"enter description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    expenses.append(expense)
    save_expenses()

    print(Fore.GREEN+"\nExpense added successfully!")


def view_expenses():
    if not expenses:
        print(Fore.RED+"No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(Fore.GREEN+f"\nExpense #{index}")
        print(Fore.GREEN+f"amount: {expense['amount']}")
        print(Fore.GREEN+f"category: {expense['category']}")
        print(Fore.GREEN+f"description: {expense['description']}")
        print(Fore.GREEN+f"date: {expense['date']}")


def show_total():
    if not expenses:
        print(Fore.RED+"NO expenses found.")
        return
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(Fore.BLUE+f"\ntotal expenses: {total:.2f}")


def load_expenses():
    global expenses

    try:
        with open("expenses.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            expenses = []

            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        expenses = []


def save_expenses():
    with open("expenses.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["amount", "category", "description", "date"]
        )
        writer.writeheader()
        writer.writerows(expenses)


def show_category_summary():
    if not expenses:
        print(Fore.RED+"No expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    print(Fore.CYAN+"\n===== Expenses by category =====")

    for category, total in category_totals.items():
        print(Fore.BLUE+f"{category}:{total:.2f}")
