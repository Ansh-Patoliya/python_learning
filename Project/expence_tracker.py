import datetime


class NumberError(Exception):
    """Custom exception for numeric validation errors (e.g., non-positive amounts, invalid menu/category choices)."""
    pass


def print_separator():
    """Print a consistent horizontal separator line used across screens."""
    print("=" * 60)


def print_header(title):
    """Render a centered uppercase header with surrounding separators."""
    print_separator()
    print(f"{title.upper():^60}")
    print_separator()


def show_menu():
    """Display the main menu options each loop iteration."""
    print_header("EXPENSE TRACKER MENU")
    print("\t1. Add Expense")
    print("\t2. View All Expenses")
    print("\t3. Update Expense")
    print("\t4. Delete Expense")
    print("\t5. Total Expense Summary")
    print("\t6. Search Expense")
    print("\t7. Exit")
    print_separator()


def input_expense_name():
    """Prompt until a valid alphabetic (plus spaces) expense name is entered; returns normalized capitalized name."""
    while True:
        e_name = input("📝 Enter expense name: ").strip()
        if e_name.replace(" ", "").isalpha():
            return e_name.capitalize()
        else:
            print("❌ Error: Expense name should contain only alphabets (A-Z, a-z) and spaces")


def input_expense_amount():
    """Prompt until a valid positive float amount is entered; returns amount rounded to 2 decimals."""
    while True:
        try:
            e_amount = float(input("💰 Enter expense amount ($): "))
            if e_amount <= 0:
                raise NumberError("Amount must be greater than 0.")
            return round(e_amount, 2)
        except ValueError:
            print("❌ Error: Please enter only numbers (0-9) with optional decimal point")
        except NumberError as e:
            print(f"❌ Error: {e}")


def input_expense_category():
    """Display selectable category list and return the chosen category label; loops until valid selection (1-6)."""
    categories = {1: "Food", 2: "Travel", 3: "Shopping", 4: "Entertainment", 5: "Bills", 6: "Others"}

    while True:
        print("\n📂 Select expense category:")
        for key, value in categories.items():
            print(f"\t{key}. {value}")

        try:
            category_choice = int(input("Enter choice (1-6): "))
            if category_choice in categories:
                return categories[category_choice]
            else:
                raise NumberError("Enter valid choice (1-6)")
        except ValueError:
            print("❌ Error: Please enter only digits (1-6)")
        except NumberError as e:
            print(f"❌ Error: {e}")


def input_expense_date():
    while True:
        e_date_str = input("Enter a date (DD-MM-YYYY): ")

        try:
            e_date = datetime.datetime.strptime(e_date_str, "%d-%m-%Y")
            print(f"You entered the date: {e_date.date()}")
            return e_date
        except ValueError:
            print("❌ Error: Please enter valid date in DD-MM-YYYY format")


def add_expense():
    """Collect expense details and display a confirmation summary.

    NOTE: Persistence not yet implemented; currently only echoes input.
    """
    print_header("ADD NEW EXPENSE")

    e_name = input_expense_name()
    e_amount = input_expense_amount()
    e_category = input_expense_category()
    e_date = input_expense_date()

    new_expense = {
        "name": e_name,
        "amount": e_amount,
        "category": e_category,
        "date": e_date.strftime("%d-%m-%Y")
    }

    # Confirmation message (future: integrate with storage / ID generation)
    print(f"\n✅ Expense added successfully!")
    print(f"📝 Name: {new_expense["name"]}")
    print(f"💰 Amount: ${new_expense["amount"]:.2f}")
    print(f"📂 Category: {new_expense["category"]}")
    print(f"📅 Date: {new_expense["date"]}")

    header_list = ["id", "name", "amount", "category", "date"]
    expenses = []
    with open("my_expense.txt", "r") as f:
        print(f.tell())
        f.seek(191)
        for i in f:
            lines = i.split()
            expense_dict = dict(zip(header_list, lines))
            expenses.append(expense_dict)

    expenses.append(new_expense)
    expenses.sort(key=lambda expense: datetime.datetime.strptime(expense["date"], "%d-%m-%Y"))
    add_id = [{**expense, "id": i + 1} for i, expense in enumerate(expenses)]
    expenses = add_id

    print(expenses)

    with open("my_expense.txt", "w") as f:
        f.write("-" * 61)
        f.write(
            "\n" + "Id".ljust(6, " ") + "Expense name".ljust(20, " ") + "Amount".ljust(10, " ") + "Category".ljust(15,
                                                                                                                   " ") + "Date".ljust(
                12,
                " ") + "\n")
        f.write("-" * 61)

        for e in expenses:
            f.write("\n" + str(e["id"]).ljust(6, " ") + e["name"].ljust(20, " ") + str(e["amount"]).ljust(10, " ") + e[
                "category"].ljust(15, " ") + e["date"].ljust(12, " "))


def view_expense():
    """Placeholder: Will list all stored expenses when persistence is added."""
    print_header("ALL EXPENSES")

    with open("my_expense.txt", "r") as f:
        expense = f.read()
        if len(expense) > 171:
            print(expense)
        else:
            print("No more expenses")


def update_expense():
    """Placeholder: Will allow modifying an existing expense by ID."""
    print_header("UPDATE EXPENSE")

    header_list = ["id", "name", "amount", "category", "date"]
    expenses = []
    with open("my_expense.txt", "r") as f:
        print(f.tell())
        f.seek(191)
        for i in f:
            lines = i.split()
            expense_dict = dict(zip(header_list, lines))
            expenses.append(expense_dict)

    view_expense()
    user_id = input("enter id for edit expense = ")
    user_amount = float(input("enter new amount = "))

    updated_expenses = [
        {**expense, "amount": user_amount} if expense["id"] == user_id else expense
        for expense in expenses
    ]

    with open("my_expense.txt", "w") as f:
        f.write("-" * 61)
        f.write(
            "\n" + "Id".ljust(6, " ") + "Expense name".ljust(20, " ") + "Amount".ljust(10, " ") + "Category".ljust(15,
                                                                                                                   " ") + "Date".ljust(
                12,
                " ") + "\n")
        f.write("-" * 61)

        for e in updated_expenses:
            f.write("\n" + e["id"].ljust(6, " ") + e["name"].ljust(20, " ") + str(e["amount"]).ljust(10, " ") + e[
                "category"].ljust(15, " ") + e["date"].ljust(12, " "))


def delete_expense():
    """Placeholder: Will remove an existing expense by ID."""
    print_header("DELETE EXPENSE")


def total_expense():
    """Placeholder: Will compute and display aggregate totals / category breakdown."""
    print_header("EXPENSE SUMMARY")


def search_expense():
    """Placeholder: Will search expenses by name / category / amount criteria."""
    print_header("SEARCH EXPENSES")


def main():
    """Entry point: show welcome screen then main loop handling menu choices until exit."""
    print_header("WELCOME TO EXPENSE TRACKER")
    print("💡 Manage your personal expenses efficiently!")
    while True:
        show_menu()

        try:
            choice = int(input("🎯 Enter your choice (1-7): "))

            match choice:
                case 1:
                    add_expense()
                case 2:
                    view_expense()
                case 3:
                    update_expense()
                case 4:
                    delete_expense()
                case 5:
                    total_expense()
                case 6:
                    search_expense()
                case 7:
                    print_header("THANK YOU")
                    print("👋 Thank you for using Expense Tracker!")
                    print("💫 Have a great day!")
                    break
                case _:
                    print("❌ Error: Please enter a valid choice (1-7)")

        except ValueError:
            print("❌ Error: Please enter only digits (1-7)")


if __name__ == "__main__":
    main()
