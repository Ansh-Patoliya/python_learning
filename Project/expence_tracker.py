"""
===============================================================================
                        PERSONAL EXPENSE TRACKER APPLICATION
===============================================================================

DESCRIPTION:
    A comprehensive command-line expense management system that helps users
    track their daily expenses with full CRUD (Create, Read, Update, Delete)
    operations. The application stores data in a plain text file with a
    structured table format for easy readability and portability.

AUTHOR:
    Developer: Ansh Patoliya
    Created: 2025
    Version: 1.0.0
    License: Open Source

FEATURES:
    ✅ Add New Expenses - Record expense with name, amount, category, and date
    ✅ View All Expenses - Display complete expense history in table format
    ✅ Update Expenses - Modify existing expense amounts by ID
    ✅ Delete Expenses - Remove unwanted expenses from records
    ✅ Total Summary - Calculate and display total spending
    ✅ Search by Date - Find all expenses for a specific date
    ✅ Data Validation - Ensures valid inputs for all fields
    ✅ Automatic Sorting - Keeps expenses sorted chronologically
    ✅ Sequential IDs - Maintains proper ID numbering after operations

CATEGORIES SUPPORTED:
    1. Food - Restaurant meals, groceries, snacks
    2. Travel - Transportation, fuel, tickets
    3. Shopping - Clothing, electronics, general purchases
    4. Entertainment - Movies, games, events
    5. Bills - Utilities, rent, subscriptions
    6. Others - Miscellaneous expenses

INPUT VALIDATIONS:
    • Expense Name: Only alphabetic characters and spaces allowed
    • Amount: Must be positive numbers, rounded to 2 decimal places
    • Category: Must select from predefined list (1-6)
    • Date: Must be in DD-MM-YYYY format and valid date
    • Menu Choice: Must be integer between 1-7

FILE STRUCTURE:
    Data stored in: my_expense.txt
    Format: Fixed-width table with headers
    Layout: ID | Expense Name | Amount | Category | Date
    Header Size: 191 characters (used for file seeking)

ERROR HANDLING:
    • Custom NumberError exception for domain-specific validation
    • ValueError handling for invalid numeric inputs
    • File operation safety with proper exception handling
    • User-friendly error messages with emoji indicators

DATA PERSISTENCE:
    • All data automatically saved to text file
    • File recreated on each update operation
    • Chronological sorting maintained
    • ID renumbering after deletions

TECHNICAL DETAILS:
    • Object-oriented design with custom exception class
    • Functional programming with pure functions
    • File I/O operations with seek positioning
    • List comprehensions for data transformation
    • Dictionary-based data structures
    • Input validation loops for user experience

FUTURE ENHANCEMENTS:
    • Category-wise expense summaries
    • Date range filtering
    • Export to CSV functionality
    • Backup and restore features
    • Multiple currency support
    • Data visualization charts

===============================================================================
"""
import datetime


class NumberError(Exception):
    """Custom error for invalid numbers like negative amounts or wrong menu choices"""
    pass


def print_separator():
    """Prints a line of equal signs to separate sections on screen"""
    print("=" * 60)


def print_header(title):
    """
    Shows a nice header with title in the center
    Used for all main screens in the app
    """
    print_separator()
    print(f"{title.upper():^60}")
    print_separator()


def show_menu():
    """Displays the main menu with all available options"""
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
    """
    Gets expense name from user
    Only allows letters and spaces, no numbers or special characters
    Returns the name with first letter capitalized
    """
    while True:
        e_name = input("📝 Enter expense name: ").strip()
        if e_name.replace(" ", "").isalpha():
            return e_name.capitalize()
        else:
            print("❌ Error: Expense name should contain only alphabets (A-Z, a-z) and spaces")


def input_expense_amount():
    """
    Gets expense amount from user
    Must be a positive number (greater than 0)
    Returns amount rounded to 2 decimal places
    """
    while True:
        try:
            e_amount = float(input("💰 Enter expense amount ($): "))
            if e_amount <= 0:
                raise NumberError("Amount must be greater than 0.")
            return round(e_amount, 2)  # Round to 2 decimal places for money
        except ValueError:
            print("❌ Error: Please enter only numbers (0-9) with optional decimal point")
        except NumberError as e:
            print(f"❌ Error: {e}")


def input_expense_category():
    """
    Shows list of expense categories and gets user choice
    Returns the selected category name as string
    """
    # Available expense categories
    categories = {1: "Food", 2: "Travel", 3: "Shopping", 4: "Entertainment", 5: "Bills", 6: "Others"}

    while True:
        print("\n📂 Select expense category:")
        # Show all category options
        for key, value in categories.items():
            print(f"\t{key}. {value}")

        try:
            category_choice = int(input("Enter choice (1-6): "))
            if category_choice in categories:
                return categories[category_choice]  # Return category name
            else:
                raise NumberError("Enter valid choice (1-6)")
        except ValueError:
            print("❌ Error: Please enter only digits (1-6)")
        except NumberError as e:
            print(f"❌ Error: {e}")


def input_expense_date():
    """
    Gets date from user in DD-MM-YYYY format
    Validates the date and returns datetime object
    """
    while True:
        e_date_str = input("Enter a date (DD-MM-YYYY): ")

        try:
            # Convert string to datetime object
            e_date = datetime.datetime.strptime(e_date_str, "%d-%m-%Y")
            print(f"You entered the date: {e_date.date()}")
            return e_date
        except ValueError:
            print("❌ Error: Please enter valid date in DD-MM-YYYY format")


def add_expense():
    """
    Main function to add a new expense
    Gets all details from user, saves to file, keeps expenses sorted by date
    """
    print_header("ADD NEW EXPENSE")

    # Get all expense details from user
    e_name = input_expense_name()
    e_amount = input_expense_amount()
    e_category = input_expense_category()
    e_date = input_expense_date()

    # Create expense dictionary
    new_expense = {
        "name": e_name,
        "amount": e_amount,
        "category": e_category,
        "date": e_date.strftime("%d-%m-%Y")  # Convert date to string
    }

    # Show confirmation to user
    print(f"\n✅ Expense added successfully!")
    print(f"📝 Name: {new_expense['name']}")
    print(f"💰 Amount: ${new_expense['amount']:.2f}")
    print(f"📂 Category: {new_expense['category']}")
    print(f"📅 Date: {new_expense['date']}")

    # Read existing expenses from file
    header_list = ["id", "name", "amount", "category", "date"]
    expenses = []
    with open("my_expense.txt", "r") as f:
        print(f.tell())  # Show current file position
        f.seek(191)  # Skip header section (first 191 characters)
        for i in f:
            lines = i.split()  # Split line into parts
            expense_dict = dict(zip(header_list, lines))  # Create dictionary
            expenses.append(expense_dict)

    # Add new expense to list
    expenses.append(new_expense)
    # Sort expenses by date to keep them in order
    expenses.sort(key=lambda expense: datetime.datetime.strptime(expense["date"], "%d-%m-%Y"))
    # Give each expense a new ID number starting from 1
    add_id = [{**expense, "id": i + 1} for i, expense in enumerate(expenses)]
    expenses = add_id

    print(expenses)  # Show all expenses for debugging

    # Write all expenses back to file
    with open("my_expense.txt", "w") as f:
        # Write header section
        f.write("-" * 61)
        f.write(
            "\n" + "Id".ljust(6, " ") + "Expense name".ljust(20, " ") + "Amount".ljust(10, " ") + "Category".ljust(15,
                                                                                                                   " ") + "Date".ljust(
                12,
                " ") + "\n")
        f.write("-" * 61)

        # Write each expense as a formatted line
        for e in expenses:
            f.write("\n" + str(e["id"]).ljust(6, " ") + e["name"].ljust(20, " ") + str(e["amount"]).ljust(10, " ") + e[
                "category"].ljust(15, " ") + e["date"].ljust(12, " "))


def read_expense_lines(seek_value=0):
    """
    Reads lines from expense file starting from a specific position
    seek_value: where to start reading (0 = from beginning)
    Returns list of lines from the file
    """
    with open("my_expense.txt", "r") as f:
        f.seek(seek_value)  # Move to specific position in file
        expenses = f.readlines()  # Read all remaining lines
    return expenses


def view_expense():
    """Shows all expenses by printing the entire file content"""
    print_header("ALL EXPENSES")
    expenses = read_expense_lines()  # Read from beginning of file
    if expenses:
        for e in expenses:
            print(e.strip())  # Remove extra whitespace and print
    else:
        return


def load_expenses():
    """
    Loads expense data from file and converts to list of dictionaries
    Skips the header section and only reads expense data
    Returns list of expense dictionaries
    """
    header_list = ["id", "name", "amount", "category", "date"]
    expenses = []
    list_expenses = read_expense_lines(191)  # Start reading after header (position 191)
    for i in list_expenses:
        lines = i.split()  # Split each line into parts
        expense_dict = dict(zip(header_list, lines))  # Create dictionary from parts
        expenses.append(expense_dict)
    return expenses


def update_expense():
    """
    Updates the amount of an existing expense
    Shows all expenses, asks user to pick ID, gets new amount
    """
    print_header("UPDATE EXPENSE")
    expenses = load_expenses()  # Load current expenses
    list_expenses = read_expense_lines(191)  # Get raw lines for display

    # Show current expenses to user
    if list_expenses:
        for e in list_expenses:
            print(e.strip())
    else:
        return

    # Get which expense to update and new amount
    user_id = input("enter id for edit expense = ")
    user_amount = float(input("enter new amount = "))

    # Update the expense with matching ID
    updated_expenses = [
        {**expense, "amount": user_amount} if expense["id"] == user_id else expense
        for expense in expenses
    ]

    # Write updated expenses back to file
    with open("my_expense.txt", "w") as f:
        # Write header section
        f.write("-" * 61)
        f.write(
            "\n" + "Id".ljust(6, " ") + "Expense name".ljust(20, " ") + "Amount".ljust(10, " ") + "Category".ljust(15,
                                                                                                                   " ") + "Date".ljust(
                12,
                " ") + "\n")
        f.write("-" * 61)
        # Write each updated expense
        for e in updated_expenses:
            f.write("\n" + e["id"].ljust(6, " ") + e["name"].ljust(20, " ") + str(e["amount"]).ljust(10, " ") + e[
                "category"].ljust(15, " ") + e["date"].ljust(12, " "))


def delete_expense():
    """
    Deletes an expense by removing it from the list
    Shows all expenses, asks user to pick ID to delete
    Reassigns ID numbers after deletion
    """
    print_header("DELETE EXPENSE")
    expenses = load_expenses()  # Load current expenses
    list_expenses = read_expense_lines(191)  # Get raw lines for display

    # Show current expenses to user
    if list_expenses:
        for e in list_expenses:
            print(e.strip())
    else:
        return

    # Get which expense to delete
    user_id = input("enter id for delete expense = ")
    # Keep all expenses except the one with matching ID
    delete_expenses = [expense for expense in expenses if expense["id"] != user_id]
    # Give new ID numbers starting from 1
    add_id = [{**expense, "id": i + 1} for i, expense in enumerate(delete_expenses)]
    delete_expenses = add_id

    # Write remaining expenses back to file
    with open("my_expense.txt", "w") as f:
        # Write header section
        f.write("-" * 61)
        f.write(
            "\n" + "Id".ljust(6, " ") + "Expense name".ljust(20, " ") + "Amount".ljust(10, " ") + "Category".ljust(15,
                                                                                                                   " ") + "Date".ljust(
                12,
                " ") + "\n")
        f.write("-" * 61)
        # Write each remaining expense
        for e in delete_expenses:
            f.write("\n" + str(e["id"]).ljust(6, " ") + e["name"].ljust(20, " ") + str(e["amount"]).ljust(10, " ") + e[
                "category"].ljust(15, " ") + e["date"].ljust(12, " "))


def total_expense():
    """
    Calculates and shows the total of all expense amounts
    Adds up all the money spent
    """
    print_header("EXPENSE SUMMARY")
    expenses = load_expenses()  # Get all expenses
    total_expenses = 0
    # Add up all expense amounts
    for expense in expenses:
        total_expenses += float(expense["amount"])
    print(f"💰Total Expense: {total_expenses}")


def search_expense():
    """
    Searches for expenses by date
    User enters a date and sees all expenses from that date
    """
    print_header("SEARCH EXPENSES")
    expenses = load_expenses()  # Get all expenses
    date = input("enter date to search = ")  # Get date to search for
    # Find all expenses with matching date
    search_list = [expense for expense in expenses if expense["date"] == date]

    # Show results in formatted table
    print("-" * 61)
    print(
        "Id".ljust(6, " ") + "Expense name".ljust(20, " ") + "Amount".ljust(10, " ") + "Category".ljust(15,
                                                                                                        " ") + "Date".ljust(
            12, " "))
    print("-" * 61)
    # Print each matching expense
    for e in search_list:
        print(e["id"].ljust(6, " ") + e["name"].ljust(20, " ") + str(e["amount"]).ljust(10, " ") + e[
            "category"].ljust(15, " ") + e["date"].ljust(12, " "))


def main():
    """
    Main function that runs the app
    Shows welcome message and keeps showing menu until user exits
    """
    print_header("WELCOME TO EXPENSE TRACKER")
    print("💡 Manage your personal expenses efficiently!")

    # Keep running until user chooses to exit
    while True:
        show_menu()  # Show menu options
        try:
            choice = int(input("🎯 Enter your choice (1-7): "))
            # Handle user choice
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
                    # Exit the program
                    print_header("THANK YOU")
                    print("👋 Thank you for using Expense Tracker!")
                    print("💫 Have a great day!")
                    break
                case _:
                    print("❌ Error: Please enter a valid choice (1-7)")
        except ValueError:
            print("❌ Error: Please enter only digits (1-7)")


# Start the program if this file is run directly
if __name__ == "__main__":
    main()
