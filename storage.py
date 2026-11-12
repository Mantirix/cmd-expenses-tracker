
"""File operations for expense records."""

import json


def save_expenses(expense_list, filename):
    """Save expenses to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(expense_list, indent=4))

        print(f"Expenses saved to {filename}")

    except OSError as error:
        print(f"Unable to save file: {error}")


def open_expenses(filename):
    """Open an existing JSON expense file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.loads(file.read())

        if not isinstance(data, list):
            print("Invalid expense file format.")
            return None

        for expense in data:
            if not isinstance(expense, dict):
                print("Invalid expense record.")
                return None

            if not all(key in expense for key in
                       ("date", "category", "amount", "description")):
                print("Expense record is missing information.")
                return None

            if not isinstance(expense["date"], str):
                print("Invalid expense date.")
                return None

            if not isinstance(expense["category"], str):
                print("Invalid expense category.")
                return None

            if not isinstance(expense["description"], str):
                print("Invalid expense description.")
                return None

            if (not isinstance(expense["amount"], (int, float))
                    or isinstance(expense["amount"], bool)):
                print("Invalid expense amount.")
                return None

        print(f"Opened {filename} successfully!")
        return data

    except (OSError, ValueError) as error:
        print(f"Unable to open file: {error}")
        return None


def csv_value(value):
    """Prepare a value for CSV output."""
    text = str(value)
    text = text.replace('"', '""')
    return '"' + text + '"'


def export_expenses(expense_list, filename):
    """Export expense records to a CSV file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Date,Category,Amount,Description\n")

            for expense in expense_list:
                row = [
                    expense["date"],
                    expense["category"],
                    expense["amount"],
                    expense["description"]
                ]

                values = []

                for value in row:
                    values.append(csv_value(value))

                file.write(",".join(values) + "\n")

        print(f"Expenses exported to {filename}")

    except OSError as error:
        print(f"Unable to export file: {error}")
