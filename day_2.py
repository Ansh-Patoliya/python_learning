#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Day 2: Python Data Types and Type Casting Learning Module

This is a simple python program to demonstrate complex numbers
    have a real part and an imaginary part
The imaginary part is represented by 'j' in Python

Learning Objectives:
1. Understanding complex number representation in Python
2. Basic arithmetic operations with complex numbers
3. Type casting between different Python data types
4. Understanding type conversion limitations and best practices

Author: Python Learning Journey
Version: 1.0
"""

# =============================================================================
# SECTION 1: Complex Numbers Demonstration
# =============================================================================

# Complex number initialization
# Note: Python uses 'j' for imaginary unit (mathematical 'i')
# Format: real_part + imaginary_part*j
a = 5 + 3j  # Complex number with real part 5, imaginary part 3
b = 2 + 8j  # Complex number with real part 2, imaginary part 8

# Display complex numbers and their data types
# Using f-string formatting for better readability
print(f"a = {a,type(a)}")  # Shows value and type information
print(f"b = {b,type(b)}")  # Shows value and type information

# Basic arithmetic operations on complex numbers
# Python's complex type supports all standard arithmetic operators
print(a+b)  # Complex addition: (5+3j) + (2+8j) = (7+11j)
print(a-b)  # Complex subtraction: (5+3j) - (2+8j) = (3-5j)

# =============================================================================
# SECTION 2: Type Casting in Python
# =============================================================================

'''
    *typecasting in python*
    
    Type casting is the process of converting one data type to another.
    Python provides built-in functions for type conversion:
    
    1. int() - converts a value to an integer
       - Truncates decimal part when converting from float
       - Raises ValueError for invalid string formats
       
    2. float() - converts a value to a float
       - Can handle integer and valid string representations
       - Provides decimal precision
       
    3. str() - converts a value to a string
       - Works with any data type
       - Returns string representation of the object
       
    4. complex() - converts a value to a complex number
       - Can take one or two arguments (real, imaginary)
       - Sets imaginary part to 0 if not specified
       
    5. bool() - converts a value to a boolean
       - Returns True for non-zero numbers, non-empty containers
       - Returns False for zero, empty containers, None

    IMPORTANT SECURITY NOTE:
    if you enter string characters in int() or float() or complex() it will give value error
    Always validate input data before type casting in production code
    
'''

# Type casting demonstration chain
# Starting with string representation of a number
x = "10"  # Initial value as string literal

# Step 1: Display original string value and its type
print(f"x1 = {x, type(x)}")  # Shows ("10", <class 'str'>)

# Step 2: Convert string to integer
# int() function parses the string and converts to integer type
x = int(x)
print(f"x2 = {x, type(x)}")  # Shows (10, <class 'int'>)

# Step 3: Convert integer to float
# float() function converts integer to floating-point representation
x = float(x)
print(f"x3 = {x, type(x)}")  # Shows (10.0, <class 'float'>)

# Note: This demonstrates the type conversion chain: str -> int -> float
# Each conversion maintains the numeric value while changing the data type
# This pattern is commonly used in data processing and user input validation

# Step 4: Convert float to complex number
# complex() function creates a complex number with real part from float, imaginary part = 0
x = complex(x)
print(f"x4 = {x, type(x)}")  # Shows ((10+0j), <class 'complex'>)

# =============================================================================
# SECTION 3: Type Casting Error Handling Examples
# =============================================================================

'''
    Error Case 1: Cannot convert complex number back to int
    
    TypeError occurs when trying to convert complex to int
    line 40, in <module>
        x=int(x)
    TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
    
    Reason: Complex numbers cannot be directly converted to integers
    Solution: Extract real part first: int(x.real)
'''
# x=int(x)  # This would cause TypeError - commented out for safety
# print(f"x5 = {x,type(x)}")

'''
    Error Case 2: Invalid string format for numeric conversion
    
    ValueError occurs when string contains non-numeric characters
    line 48, in <module>
        x=int(x)
    ValueError: invalid literal for int() with base 10: 'hi'
    
    Reason: "hi" is not a valid numeric representation
    Solution: Validate input before conversion or use try-except blocks
'''
# x="hi"  # This would cause ValueError - commented out for safety
# x=int(x)
# print(f"x6 = {x,type(x)}")

# =============================================================================
# SECTION 4: Practical Applications - User Input and Validation
# =============================================================================

# Age verification program
# Demonstrates type casting with user input and conditional logic
age = int(input("enter your age: "))  # Convert string input to integer
if age >= 18:
    print("you are eligible for licence.")
else:
    print("you are not eligible for licence.")

# Finding maximum of three numbers
# Demonstrates nested if-else statements with type casting
n1 = int(input("enter n1 = "))  # Convert user input to integer
n2 = int(input("enter n2 = "))  # Convert user input to integer
n3 = int(input("enter n3 = "))  # Convert user input to integer

# Nested conditional logic to find maximum
if n1 > n2:
    if n1 > n3:
        print(f"{n1} is max")
    else:
        print(f"{n3} is max")
else:
    if n2 > n3:
        print(f"{n2} is max")
    else:
        print(f"{n3} is max")

# Grade calculation system
# Demonstrates float type casting and multiple conditional branches
marks1 = float(input("enter your marks1 = "))  # Convert to float for decimal precision
marks2 = float(input("enter your marks2 = "))  # Convert to float for decimal precision
marks3 = float(input("enter your marks3 = "))  # Convert to float for decimal precision

# Calculate total and percentage
total_marks = marks1 + marks2 + marks3
pr = total_marks / 3  # Calculate average percentage
print(pr)

# Grade assignment using elif ladder
if pr >= 85:
    print("your rank is A+")
elif 80 <= pr < 85:
    print("your rank is A")
elif 70<=pr<80:
    print("your rank is B")
elif 35<=pr<70:
    print("you are pass")
else:
    print("your are fail")

# =============================================================================
# SECTION 5: Comparison Operators
# =============================================================================

# Comparison Operators
'''
    Comparison operators are used to compare two values.
    They return a boolean value (True or False) based on the comparison.
    The common comparison operators are:
    - Equal to (==): Checks if two values are equal
    - Not equal to (!=): Checks if two values are not equal
    - Greater than (>): Checks if left value is greater than right
    - Less than (<): Checks if left value is less than right
    - Greater than or equal to (>=): Checks if left >= right
    - Less than or equal to (<=): Checks if left <= right
'''
a = 10
b = 20
print(a == b)  # False - 10 is not equal to 20
print(a != b)  # True - 10 is not equal to 20
print(a > b)   # False - 10 is not greater than 20
print(a < b)   # True - 10 is less than 20
print(a >= b)  # False - 10 is not greater than or equal to 20
print(a <= b)  # True - 10 is less than or equal to 20

# =============================================================================
# SECTION 6: Logical Operators
# =============================================================================

# Logical Operators
'''
    Logical operators are used to combine multiple boolean expressions.
    They follow boolean algebra rules:
    - and: Returns True if both expressions are True (logical AND)
    - or: Returns True if at least one expression is True (logical OR)
    - not: Returns True if the expression is False (logical NOT/negation)
'''
x = 5
print(x > 0 and x < 10)        # True - both conditions are true (5 > 0 AND 5 < 10)
print(x > 0 or x < 3)          # True - first condition is true (5 > 0 OR 5 < 3)
print(not (x > 0 and x < 10))  # False - negation of True is False

# =============================================================================
# SECTION 7: Membership Operators
# =============================================================================

# Membership Operators
'''
    Membership operators are used to test if a sequence contains a specific value.
    They work with strings, lists, tuples, sets, and dictionaries:
    - 'in': Returns True if the value is found in the sequence
    - 'not in': Returns True if the value is not found in the sequence
    
    Time Complexity: O(n) for lists/tuples, O(1) average for sets/dictionaries
'''
name = "ansh"
print('an' in name)      # True - substring 'an' exists in 'ansh'
print('an' not in name)  # False - substring 'an' does exist in 'ansh'

# =============================================================================
# SECTION 8: Identity Operators
# =============================================================================

# Identity Operators
"""
    Identity operators compare object identity (memory location), not value equality.
    Important distinction from equality operators:
    - 'is': Returns True if both variables point to the same object in memory
    - 'is not': Returns True if variables point to different objects in memory
    
    Note: Small integers (-5 to 256) are cached by Python for performance
"""
a = "10"  # String object
b = 10    # Integer object
c = 10    # References same cached integer object as 'b'
print(a is b)      # False - string "10" and integer 10 are different objects
print(a is not c)  # True - string "10" and integer 10 are different objects
print(b is c)      # True - both reference the same cached integer object

# =============================================================================
# SECTION 9: Loop Constructs
# =============================================================================

# For loop demonstration - printing odd numbers from 1 to 99
# range(start, stop, step) generates sequence: start to stop-1 with given step
for i in range(1, 100, 2):  # start=1, stop=100, step=2 (odd numbers)
    print(i, end=" ")        # Print on same line with space separator
print()  # New line after loop completion

# While loop demonstration - simple counter
# While loops continue until condition becomes False
i = 1
while i <= 5:
    print(i)  # Print current value
    i+=1      # Increment counter (equivalent to i = i + 1)

# =============================================================================
# SECTION 10: Break and Continue Statements
# =============================================================================

# break and continue
'''
    Control flow statements in loops:
    - break: Immediately exits the loop completely
    - continue: Skips current iteration and jumps to next iteration
    
    Practice questions using loops and conditional statements:
    1. Print all even numbers from 1 to 50.
    2. Calculate the factorial of a given number.
    3. Find the sum of all digits in a given number.
    4. Check if a given number is a prime number.
    5. Print the Fibonacci series up to a given number of terms.
'''

# Problem 1: Print all even numbers from 1 to 50
# Using while loop with continue statement for odd numbers
i=1
while i<=50:
    if i%2!=0:      # If number is odd (remainder when divided by 2 is not 0)
        i += 1
        continue    # Skip to next iteration without executing print
    else :
        print(i,end=",")  # Print even number
        i += 1
print()  # New line after completion

# Problem 2: Calculate factorial of a given number
# Factorial: n! = n × (n-1) × (n-2) × ... × 1
no=int(input("enter number = "))  # Get number from user
i=1
fact=1  # Initialize factorial result
while i<=no:
    fact*=i  # Multiply current number to factorial (fact = fact * i)
    i+=1     # Move to next number
print(f"factorial = {fact}")

# Problem 3: Find sum of all digits in a given number
# Algorithm: Extract last digit using modulo, add to sum, remove last digit using division
no=int(input("enter number = "))
total=0
while no>0:
    total=total+no%10  # Add last digit to total (no%10 gives last digit)
    no/=10             # Remove last digit (integer division by 10)
print(int(total))      # Convert to int to remove decimal places

# Problem 4: Check if a given number is prime
# Prime number: divisible only by 1 and itself
no = int(input("enter number = "))
found = True  # Assume number is prime initially
for i in range(2, no):  # Check divisors from 2 to no-1
    if no % i == 0:     # If divisible by any number
        found = False   # Not prime
        break           # No need to check further
if found:
    print(f"{no} is prime")
else:
    print(f"{no} is not prime ")

# Problem 5: Print Fibonacci series up to given number of terms
# Fibonacci: Each number is sum of two preceding numbers (0, 1, 1, 2, 3, 5, 8...)
no=int(input("enter number = "))
a=0  # First Fibonacci number
b=1  # Second Fibonacci number
i=1
while i<=no:
    print(a,end=",")  # Print current Fibonacci number
    c=a+b            # Calculate next Fibonacci number
    a=b              # Update: previous second becomes first
    b=c              # Update: calculated number becomes second
    i+=1             # Move to next position
