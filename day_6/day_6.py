"""
Python File Operations and Exception Handling - Day 6 Learning Module

This module demonstrates fundamental Python concepts including:
1. File I/O operations (write, append, read modes)
2. File positioning and seeking mechanisms
3. Different methods of reading file content
4. Exception handling with try-except blocks
5. Custom exception creation and handling

The code is organized into three main sections:
- Part 1: File Operations (writing, appending, reading)
- Part 2: File Positioning and Reading Techniques
- Part 3: Exception Handling (built-in and custom exceptions)

Author: Ansh Patoliya
Date: Learning Session Day 6
Purpose: Understanding file operations and error handling in Python
"""

# =============================================================================
# PART 1: BASIC FILE OPERATIONS - WRITE AND APPEND
# =============================================================================

# Creating and writing to a new file in write mode
with open("../Demo.txt", "w") as f:
    if f.writable():
        f.writelines(["hi , ", "my name is ansh.\n", "and your?"])
    else:
        print("file is not writable")

# Appending additional content to the existing file
with open("../Demo.txt", "a") as f:
    f.write("hi,my name is ansh".title())
    f.write("\nHow are you?")
    print("good", file=f)
    f.close()

# =============================================================================
# PART 2: FILE READING OPERATIONS AND POSITIONING
# =============================================================================

# Reading the entire file content at once
with open("../Demo.txt", "r") as f:
    if f.readable():
        print(f.read())
    else :
        print("file is not readable")
    f.close()

# Demonstrating file pointer positioning with tell() and partial reading
with open("../Demo.txt", "r") as f:
    if f.readable():
        print(f.tell())  # Current file pointer position
        print(f.read(2))  # Read only 2 characters
        print(f.tell())  # New file pointer position after reading
    else :
        print("file is not readable")
    f.close()

# Reading file line by line using readline() method
with open("../Demo.txt", "r") as f:
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
    print(f"line 1 = {line1}")
    print(f"line 2 = {line2}")
    print(f"line 3 = {line3}")
    f.close()

# Iterating through file lines and tracking file pointer position
with open("../Demo.txt", "r") as f:
    print(f.tell())  # Initial position
    for line in f:
        print(f"line = {line.strip()}")  # Remove newline characters
    print(f.tell())  # Final position after reading all lines
    f.close()

# Reading all lines into a list using readlines()
with open("../Demo.txt", "r") as f:
    lines=f.readlines()
    print(lines)

# Demonstrating file seeking - reading same content multiple times
with open("../Demo.txt", "r") as f:
    for i in range(0,11):
        print(f.read(4),end="")  # Read 4 characters
        f.seek(0)  # Reset file pointer to beginning

# =============================================================================
# PART 3: EXCEPTION HANDLING - BUILT-IN AND CUSTOM EXCEPTIONS
# =============================================================================

# Basic exception handling - Division by zero
try :
    x=10/0
except ZeroDivisionError :
    print("Oops! number not divide by 0")

# Multiple exception handling - Catching different error types
try:
    num = int("abc")  # This will raise ValueError, not ZeroDivisionError
except ZeroDivisionError:
    print("Divide by zero error!")
except ValueError:
    print("Invalid number conversion!")

# Exception handling with else clause - executes when no exception occurs
try:
    x=10//3  # Integer division, no exception expected
except ZeroDivisionError:
    print("Divide by zero error!")
else :
    print("answer = ",x)  # This will execute since no exception occurred

# Custom exception class definition
class NegativeNumberException(Exception):
    """Custom exception for handling negative number validation"""
    pass

# Function that raises custom exception for negative numbers
def check_positive(no):
    """
    Validates if a number is positive, raises custom exception if negative
    Args: no (int/float): Number to validate
    Raises: NegativeNumberException: If number is negative
    """
    if no<0:
        raise NegativeNumberException("number is negative")
    else:
        print("Number is positive:", no)

# Testing custom exception handling
try:
    check_positive(-7)  # This will raise NegativeNumberException
except NegativeNumberException as e:
    print(e)
