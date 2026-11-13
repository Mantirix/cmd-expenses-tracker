
"""Functions for managing expense records."""


def valid_date(date):
    """Check the YYYY-MM-DD date format."""
    parts = date.split("-")

    if len(parts) != 3:
        return False

    if len(parts[0]) != 4:
        return False

    if len(parts[1]) != 2 or len(parts[2]) != 2:
        return False

    if not all(part.isdigit() for part in parts):
        return False

    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])

    if year < 1 or month < 1 or month > 12:
        return False

    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and
            (year % 100 != 0 or year % 400 == 0)):
        days[1] = 29

    return 1 <= day <= days[month - 1]


def add_expense(expense_list):
    """Ask the user to enter a new expense."""
    print("\nADD NEW EXPENSE")

    date = input("Date (YYYY-MM-DD): ").strip()

    if not valid_date(date):
        print("Invalid date.")
        return

    category = input("Category: ").strip()

    if category == "":
        print("Category cannot be empty.")
        return

    amount_text = input("Amount: ").strip()

    try:
        amount = round(float(amount_text), 2)

        if not (0 < amount < 1000000000000):
            print("Enter a valid positive amount.")
            return

    except ValueError:
        print("Amount must be a number.")
        return

    description = input("Description: ").strip()

    if description == "":
        print("Description cannot be empty.")
        return

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expense_list.append(expense)
    print("Expense added successfully!")


def print_expenses(expense_list):
    """Display expenses and their total."""
    if len(expense_list) == 0:
        print("\nNo expenses found.")
        return

    print("\nEXPENSE RECORDS")
    print("-" * 65)
    print(f"{'Date':<12} {'Category':<15} "
          f"{'Amount':>10}  Description")
    print("-" * 65)

    total = 0

    for expense in expense_list:
        print(f"{expense['date']:<12} "
              f"{expense['category']:<15} "
              f"{expense['amount']:>10.2f}  "
              f"{expense['description']}")

        total += expense["amount"]

    print("-" * 65)
    count = len(expense_list)
    average = total / count

    print(f"Total Expenses: ${total:.2f}")
    print(f"Number of Records: {count}")
    print(f"Average Expense: ${average:.2f}")


def filter_expenses(expense_list):
    """Filter records by category and/or date range."""
    print("\nFILTER EXPENSES")
    print("Leave a field blank to skip that filter.")

    category = input("Category: ").strip().lower()
    start = input("Start date (YYYY-MM-DD): ").strip()
    end = input("End date (YYYY-MM-DD): ").strip()

    if start != "" and not valid_date(start):
        print("Invalid start date.")
        return []

    if end != "" and not valid_date(end):
        print("Invalid end date.")
        return []

    if start != "" and end != "" and start > end:
        print("Start date must be before end date.")
        return []

    results = []

    for expense in expense_list:
        matches = True

        if category != "":
            expense_category = expense["category"].lower()

            if category not in expense_category:
                matches = False

        if start != "":
            if expense["date"] < start:
                matches = False

        if end != "":
            if expense["date"] > end:
                matches = False

        if matches:
            results.append(expense)

    return results
