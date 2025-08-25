"""
🐍 WELCOME TO PYTHON - DAY 1 LEARNING JOURNEY! 🐍
=====================================================

Hello! Welcome to my first day of Python programming! This file will teach you
the fundamental building blocks of Python. I've organized
this to help you understand each concept step by step.

TODAY YOU'LL LEARN:
✅ How to display text with print()
✅ How to get input from users
✅ How to store data in variables
✅ Different types of data (text, numbers, true/false)
✅ How to work with text (strings)
✅ Basic math operations
✅ How to check what type of data you have

Let's start your coding adventure! 🚀
"""
import math

# ═══════════════════════════════════════════════════════════════════════════════
# 📝 LESSON 1: BASIC PRINTING - YOUR FIRST PYTHON WORDS!
# ═══════════════════════════════════════════════════════════════════════════════

# This is your first Python command! print() displays text on the screen
print("hello world")  # Output: hello world

# You can print multiple things at once - Python puts spaces between them automatically
print("hello","world",sep='...')  # Output: hello...world (custom separator)

# The 'end' parameter changes what happens at the end (normally it goes to new line)
print("hello","world",end="...")  # Output: hello world... (then stays on same line)

# Watch this! The next print will continue on the same line because of end="..."
print("hello world",end="->")  # This doesn't go to new line, it ends with ->
print("my name is ansh")        # This appears right after the -> symbol

# You can combine BOTH sep and end parameters!
print("my","name","is","ansh",sep="-",end="!")  # Output: my-name-is-ansh!
print("hello world")  # This continues on the same line after the !

# ═══════════════════════════════════════════════════════════════════════════════
# 💬 LESSON 2: GETTING INPUT FROM USERS - MAKING PROGRAMS INTERACTIVE!
# ═══════════════════════════════════════════════════════════════════════════════

# Method 1: Ask a question first, then get the answer
print("what is your name?")  # Ask the question
name = input()               # Wait for user to type something and press Enter
print("hello",name)          # Say hello to whatever they typed

# Method 2: Ask the question and get input in one line (more efficient!)
age=input("what is your age?\n")  # \n means "go to new line" - makes it look neater
print("your age is :- ",age)       # Show them what they entered

# Getting multiple pieces of information from the user
name=input("what is your name? ")   # Note: This replaces the previous 'name' variable
like=input("what is your like? ")   # Get their favorite thing
print(name,"likes",like)            # Combine their answers: "John likes pizza"

# ═══════════════════════════════════════════════════════════════════════════════
# 📦 LESSON 3: VARIABLES - STORING INFORMATION IN BOXES!
# ═══════════════════════════════════════════════════════════════════════════════

# Think of variables as labeled boxes where you store different types of information
employee_name="ansh"     # A text box (string) - notice the quotes
employee_age=19          # A number box (integer) - whole numbers, no quotes
salary=100000.21         # A decimal number box (float) - numbers with decimal points

# You can display multiple variables at once
print("name : ",employee_name," age = ",employee_age,"salary = ",salary)

# ═══════════════════════════════════════════════════════════════════════════════
# 🔤 LESSON 4: WORKING WITH TEXT (STRINGS) - QUOTE RULES!
# ═══════════════════════════════════════════════════════════════════════════════

# Smart quote usage: Use double quotes when your text has single quotes inside
st="hi,'hello world'!"  # The single quotes inside don't cause problems
print(st)

# Use single quotes when your text has double quotes inside
st='hi,"hello world"!'  # The double quotes inside don't cause problems
print(st)

# len() function tells you how many characters (letters, spaces, symbols) are in text
print(len(st))  # Counts every character in the st variable

# ═══════════════════════════════════════════════════════════════════════════════
# 🔧 LESSON 5: USEFUL STRING TRICKS AND FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

# Even empty text has a length (which is 0)
print(len(""))  # Output: 0

# You can join (concatenate) text pieces together with the + symbol
line=employee_name+","+st  # Joins: "ansh" + "," + "hi,"hello world"!"
print(line)  # Output: ansh,hi,"hello world"!

# ═══════════════════════════════════════════════════════════════════════════════
# 📊 LESSON 6: ANALYZING USER INPUT - TEXT DETECTIVE WORK!
# ═══════════════════════════════════════════════════════════════════════════════

# Get user's name in parts
f_name=input("Enter first name: ")
l_name=input("Enter last name: ")

# Analyze and tell them about their name lengths
print("your f_name length is",len(f_name)," your l_name length is",len(l_name))

# ═══════════════════════════════════════════════════════════════════════════════
# 🎨 LESSON 7: CREATING MESSAGES WITH TEXT JOINING
# ═══════════════════════════════════════════════════════════════════════════════

# Set up some text variables for demonstration
name="ansh"      # A text variable
feel="happy"     # Another text variable

# Create personalized messages by joining text pieces
print("hi "+name+"!")                # Creates: "hi ansh!"
print("I'm glad you feel "+feel)     # Creates: "I'm glad you feel happy"

# ═══════════════════════════════════════════════════════════════════════════════
# 🔍 LESSON 8: DATA TYPES - UNDERSTANDING WHAT KIND OF DATA YOU HAVE!
# ═══════════════════════════════════════════════════════════════════════════════

# Python has different types of data - let's explore them!
w="hi"      # String (text) - always in quotes
x=1         # Integer (whole number) - no quotes
y=1.2       # Float (decimal number) - has a decimal point
z=True      # Boolean (True or False) - no quotes, capital T and F

# type() function tells you what kind of data you have
print(type(w),type(x),y,type(y),type(z))  # Shows the data types

# ═══════════════════════════════════════════════════════════════════════════════
# 🧮 LESSON 9: MATH OPERATIONS - PYTHON AS A CALCULATOR!
# ═══════════════════════════════════════════════════════════════════════════════

# Python follows math rules: parentheses first, then multiplication/division, then +/-
a=(1+2)*3  # First: 1+2=3, then: 3*3=9
print(a)   # Output: 9

# ** means "to the power of" (exponentiation)
a=2**3     # 2 to the power of 3 = 2×2×2 = 8
print(a)   # Output: 8

# Using math.pi gives us the value of π (pi), and we can make it negative
a=-math.pi # Negative pi ≈ -3.14159...
print(a)   # Output: -3.141592653589793

# Complex math: parentheses first, then power, then division
a=(1 + 3) ** 2 / 4  # First: (1+3)=4, then: 4**2=16, then: 16/4=4.0
print(a)            # Output: 4.0

# CAREFUL! Order matters: -4**2 means -(4**2) = -16, not (-4)**2 = 16
a=-4 ** 2  # This is -(4²) = -16
print(a)   # Output: -16

# ═══════════════════════════════════════════════════════════════════════════════
# 🎯 DAY 1 COMPLETE SUMMARY - WHAT YOU'VE LEARNED TODAY!
# ═══════════════════════════════════════════════════════════════════════════════

"""
🎉 CONGRATULATIONS! YOU'VE COMPLETED DAY 1 OF PYTHON! 🎉

HERE'S EVERYTHING YOU LEARNED TODAY:

1. 📝 PRINT FUNCTION:
   - print("text") displays text on screen
   - sep parameter changes spaces between items
   - end parameter changes what happens at the end of the line

2. 💬 USER INPUT:
   - input() gets text from the user
   - input("question") shows a question first
   - Always returns text (even if user types numbers)

3. 📦 VARIABLES:
   - Store information in named containers
   - name = "text" for text (strings)
   - age = 25 for whole numbers (integers)
   - price = 19.99 for decimal numbers (floats)

4. 🔤 STRINGS (TEXT):
   - Use quotes: "text" or 'text'
   - len() counts characters
   - + joins text pieces together
   - Mix quote types to avoid conflicts

5. 🔍 DATA TYPES:
   - str (string): text in quotes
   - int (integer): whole numbers
   - float: decimal numbers
   - bool (boolean): True or False
   - type() tells you what type your data is

6. 🧮 MATH OPERATIONS:
   - + (add), - (subtract), * (multiply), / (divide)
   - ** (power/exponent)
   - () (parentheses) for grouping
   - Python follows mathematical order of operations

7. 📚 IMPORTS:
   - import math gives you mathematical functions
   - math.pi gives you the value of π

You're doing great! Keep practicing and you'll be a Python programmer in no time! 🚀
"""
