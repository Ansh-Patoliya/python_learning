header_list = ["id", "name", "amount", "category", "date"]
expenses = []
with open("my_expense.txt", "r") as f:
    f.seek(191)
    for i in f:
        lines = i.split()
        expense_dict = dict(zip(header_list, lines))
        expenses.append(expense_dict)

date = input("enter date to search = ")
search_list = [expense for expense in expenses if expense["date"] == date]

print("-" * 61)
print(
    "Id".ljust(6, " ") + "Expense name".ljust(20, " ") + "Amount".ljust(10, " ") + "Category".ljust(15,
                                                                                                    " ") + "Date".ljust(
        12, " "))
print("-" * 61)
for e in search_list:
    # proper formatting for display
    print(e["id"].ljust(6, " ") + e["name"].ljust(20, " ") + str(e["amount"]).ljust(10, " ") + e[
        "category"].ljust(15, " ") + e["date"].ljust(12, " "))
