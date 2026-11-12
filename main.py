
"""Main program for the Expense Command Center."""

import expenses
import storage


def show_help():
    """Display the available commands."""
    print("\nEXPENSE COMMAND CENTER")
    print("----------------------")
    print("ADD    - Enter a new expense")
    print("LIST   - Display all expenses")
    print("FILTER - Search expenses")
    print("SAVE   - Save expenses to JSON")
    print("OPEN   - Open an expense file")
    print("EXPORT - Export expenses to CSV")
    print("HELP   - Show available commands")
    print("EXIT   - Close the program")


def main():
    """Run the expense manager."""
    expense_list = []

    print("Welcome to the Expense Command Center!")
    print("Type HELP to see available commands.")

    while True:
        command = input("\nExpense> ").strip().upper()

        if command == "ADD":
            expenses.add_expense(expense_list)

        elif command == "LIST":
            expenses.print_expenses(expense_list)

        elif command == "FILTER":
            results = expenses.filter_expenses(expense_list)
            expenses.print_expenses(results)

        elif command == "SAVE":
            filename = input("JSON filename: ").strip()
            if filename == "":
                filename = "expenses.json"
            storage.save_expenses(expense_list, filename)

        elif command == "OPEN":
            filename = input("JSON filename: ").strip()
            if filename == "":
                filename = "expenses.json"
            loaded = storage.open_expenses(filename)
            if loaded is not None:
                expense_list = loaded

        elif command == "EXPORT":
            filename = input("CSV filename: ").strip()
            if filename == "":
                filename = "expenses.csv"
            storage.export_expenses(expense_list, filename)

        elif command == "HELP":
            show_help()

        elif command == "EXIT":
            print("Thank you for using Expense Command Center!")
            break

        else:
            print("Unknown command. Type HELP for assistance.")


if __name__ == "__main__":
    main()
