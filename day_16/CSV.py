# filepath: c:\Users\ansh\PycharmProjects\python_learning\day_16\CSV.py
"""
CSV module quick guide (Part-wise):
- Part 1: Write a simple table to CSV using csv.writer + writerows
- Part 2: Overwrite the same file with a header and rows using writerow
- Part 3: Read a CSV file into a list of rows using csv.reader
- Part 4: Write a list of dicts to CSV using csv.DictWriter
- Part 5: Read dict-based CSV using csv.DictReader and format output

Tips:
- On Windows, always open CSV files with newline='' to avoid blank lines.
- Use encoding='utf-8' for portability and to handle non-ASCII text.
- Mode 'w' overwrites; use 'a' to append.
"""

import csv

# -----------------------------
# Part 1 — Write multiple rows at once (writerows)
# -----------------------------
# Data as a list of lists (each inner list = one row)
data = [
    ["EmpID", "Name", "Department"],
    ["E01", "Riya", "HR"],
    ["E02", "Amit", "IT"],
    ["E03", "Sunita", "Finance"],
]

# Create/overwrite first.csv with the table above
with open("first.csv", "w", newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerows(data)  # Write all rows in one go

# -----------------------------
# Part 2 — Overwrite with a header + individual rows (writerow)
# -----------------------------
# NOTE: Opening with mode 'w' again will overwrite the previous content of first.csv.
with open("first.csv", "w", newline="", encoding="utf-8") as f:
    header = ["Name", "Age", "City"]
    first_row = ["ansh", 20, "ahmedabad"]
    second_row = ["priyansh", 21, "surat"]
    third_row = ["nihar", 19, "baroda"]

    write = csv.writer(f)
    write.writerow(header)      # Write header as first line
    write.writerow(first_row)   # Then write each data row
    write.writerow(second_row)
    write.writerow(third_row)

# -----------------------------
# Part 3 — Read CSV into a list of rows (csv.reader)
# -----------------------------
# Reader returns each row as a list of strings; numbers will be strings unless converted.
load_data = []
with open("first.csv", "r", encoding="utf-8") as f:
    read = csv.reader(f)
    # If you want to skip header: next(read)  # uncomment when needed
    for row in read:
        load_data.append(row)

print(load_data)

# -----------------------------
# Part 4 — Write dicts to CSV (csv.DictWriter)
# -----------------------------
# Each dict must contain the keys listed in fieldnames (order defined by fieldnames).
student_data = [
    {"Name": "ansh", "Age": 20, "City": "ahmedabad"},
    {"Name": "priyansh", "Age": 21, "City": "surat"},
    {"Name": "nihar", "Age": 19, "City": "baroda"},
]

field_name = ["Name", "Age", "City"]

with open("second.csv", "w", newline="", encoding="utf-8") as f:
    write = csv.DictWriter(f, fieldnames=field_name)
    write.writeheader()         # Writes: Name,Age,City
    write.writerows(student_data)

# -----------------------------
# Part 5 — Read dict rows and format output (csv.DictReader)
# -----------------------------
# DictReader maps each row to a dict using the header as keys.
with open("second.csv", "r", encoding="utf-8") as f:
    read = csv.DictReader(f)
    # header = next(read)  # Advance manually if you want to inspect header
    for row in read:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}.")