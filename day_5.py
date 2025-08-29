"""
################################################################################
#                           PYTHON LEARNING - DAY 5
#                    ADVANCED DATA STRUCTURES & FUNCTIONS
################################################################################

COMPLETE OVERVIEW:
================================================================================
This module demonstrates advanced Python concepts focusing on type casting and
function programming paradigms. As a comprehensive learning resource, it covers:

📚 LEARNING OBJECTIVES:
    • Master type conversion between Python data structures
    • Understand function creation patterns and best practices
    • Implement various argument passing techniques
    • Apply real-world scenarios for each concept

🛠️ COVERED TOPICS:
    PART 1: Type Casting & Data Structure Conversions
        - List ↔ Tuple ↔ Set ↔ Dictionary conversions
        - String to collection type transformations
        - Practical use cases and memory considerations

    PART 2: Function Creation Patterns
        - Functions without parameters/return values
        - Parameterized functions with/without returns
        - Default parameter implementations
        - Function design best practices

    PART 3: Advanced Function Arguments
        - Positional vs Keyword arguments
        - Default parameter handling
        - Variable-length arguments (*args, **kwargs)
        - Argument unpacking techniques

    PART 4: Recursion Functions
        - Factorial calculation
        - Fibonacci sequence generation
        - GCD and LCM computation
        - String reversal and palindrome checking
        - List summation and maximum element finding
        - String permutations
        - Nested list flattening
        - Tower of Hanoi solution

💡 REAL-WORLD APPLICATIONS:
    • Data preprocessing and normalization
    • API response formatting
    • Configuration management
    • Dynamic function calling
    • Code modularity and reusability


"""

# ================================================================================
#                    PART 1: TYPE CASTING - DATA STRUCTURE CONVERSIONS
# ================================================================================
"""
🔄 TYPE CASTING DEEP DIVE:

Type casting is fundamental for data manipulation in Python. This section explores
systematic conversion between Python's core data structures, demonstrating both
the mechanics and practical applications.

KEY CONCEPTS:
    • Implicit vs Explicit type conversion
    • Memory efficiency considerations
    • Data integrity during conversion
    • Performance implications of different casting operations

CONVERSION MATRIX:
    List    → Tuple, Set, Dictionary (via zip)
    Tuple   → List, Set, Dictionary (via zip) 
    Set     → List, Tuple, Dictionary (via zip)
    Dict    → List (keys/values), Tuple (keys/values), Set (keys/values)
    String  → List, Tuple, Set (character-wise)

PRACTICAL USE CASES:
    ✓ Data preprocessing for ML pipelines
    ✓ API response formatting
    ✓ Database query result transformation
    ✓ Configuration file parsing
"""

# typecasting in tuple, list, set, dictionary

name = ["abc", "bcd", "cda", "dbc"]
age = [83, 4, 21, 23]
print(f"Original List: {name}, Type: {type(name)}")
# 1. List to Tuple
list_tuple = tuple(name)
print(f"List to Tuple: {list_tuple}, Type: {type(list_tuple)}")
# 2. List to Dictionary
list_dict = dict(zip(name, age))
print(f"List to Dictionary: {list_dict}, Type: {type(list_dict)}")
# 3. List to Set
list_set = set(age)
print(f"List to Set: {list_set}, Type: {type(list_set)}")

name = tuple(name)
age = tuple(age)
print(f"Original Tuple: {name}, Type: {type(name)}")
# 4. Tuple to List
tuple_list = list(name)
print(f"Tuple to List: {tuple_list}, Type: {type(tuple_list)}")
# 5. Tuple to Dictionary
tuple_dict = dict(zip(name, age))
print(f"Tuple to Dictionary: {tuple_dict}, Type: {type(tuple_dict)}")
# 6. Tuple to Set
tuple_set = set(name)
print(f"Tuple to Set: {tuple_set}, Type: {type(tuple_set)}")

name = set(name)
age = set(age)
print(f"Original Set: {name}, Type: {type(name)}")
# 7. Set to List
set_list = list(name)
print(f"Set to List: {set_list}, Type: {type(set_list)}")
# 8. Set to Tuple
set_tuple = tuple(name)
print(f"Set to Tuple: {set_tuple}, Type: {type(set_tuple)}")
# 9. Set to Dictionary
set_dict = dict(zip(name, age))
print(f"Set to Dictionary: {set_dict}, Type: {type(set_dict)}")

name_age = dict(zip(name, age))
print(f"Original Dictionary: {name_age}, Type: {type(name_age)}")
# 10. Dictionary to List
dict_list = list(name_age.keys())
print(f"Dictionary to List: {dict_list}, Type: {type(dict_list)}")
# 11. Dictionary to Tuple
dict_tuple = tuple(name_age.values())
print(f"Dictionary to Tuple: {dict_tuple}, Type: {type(dict_tuple)}")
# 12. Dictionary to Set
dict_set = set(name_age.values())
print(f"Dictionary to Set: {dict_set}, Type: {type(dict_set)}")

name = "Unknown"
print(f"Original String: {name}, Type: {type(name)}")
# 13. String to List
str_list = list(name)
print(f"String to List: {str_list}, Type: {type(str_list)}")
# 14. String to Tuple
str_tuple = tuple(name)
print(f"String to Tuple: {str_tuple}, Type: {type(str_tuple)}")
# 15. String to Set
str_set = set(name)
print(f"String to Set: {str_set}, Type: {type(str_set)}")
# Note: String to Dictionary conversion is not straightforward and typically requires a specific format.

# ================================================================================
#                      PART 2: FUNCTION CREATION - DESIGN PATTERNS
# ================================================================================
"""
🏗️ FUNCTION ARCHITECTURE PATTERNS:

Functions are the building blocks of modular programming. This section demonstrates
various function creation patterns, each serving specific use cases in software
development.

FUNCTION DESIGN PRINCIPLES:
    • Single Responsibility Principle
    • Clear input/output contracts
    • Predictable behavior and side effects
    • Appropriate naming conventions

PATTERN CATEGORIES:
    1. Pure Functions: No side effects, deterministic output
    2. Procedures: Perform actions, may have side effects
    3. Factory Functions: Create and return objects/data
    4. Utility Functions: Helper functions for common operations

BEST PRACTICES DEMONSTRATED:
    ✓ Function naming conventions
    ✓ Parameter design patterns
    ✓ Return value strategies
    ✓ Documentation and type hints readiness
"""


# 1. Function without parameters and return value
def sum_digit():
    a = 10
    b = 5
    return a + b


# 2. Function with parameters but no return value
def sum_digit1(a, b):
    total = a + b
    print(f"total = {total}")


# 3. Function with parameters and return value
def sum_num(a, b):
    return a + b


# 4. Function with default parameters
def sum_num1():
    a = 11
    b = 4
    total1 = a + b
    print(f"total1 = {total1}")


# function calls
result = sum_digit()
print(f"Sum without parameters and return value: {result}")
sum_digit1(10, 20)
result1 = sum_num(20, 30)
print(f"Sum with parameters and return value: {result1}")
sum_num1()

# ================================================================================
#                   PART 3: FUNCTION ARGUMENTS - ADVANCED TECHNIQUES
# ================================================================================
"""
🎛️ ARGUMENT HANDLING MASTERY:

Advanced argument handling enables flexible, reusable functions that can adapt
to various calling patterns. This section covers all argument types and their
strategic applications.

ARGUMENT TYPE HIERARCHY:
    1. Positional Arguments: Required, order-dependent
    2. Keyword Arguments: Named, order-independent  
    3. Default Arguments: Optional with fallback values
    4. Variable Arguments: Handle arbitrary input (*args, **kwargs)

ADVANCED TECHNIQUES:
    • Argument unpacking and packing
    • Mixed argument type functions
    • Dynamic function signatures
    • Flexible API design patterns

PROFESSIONAL APPLICATIONS:
    ✓ API endpoint handlers
    ✓ Configuration managers
    ✓ Data processing pipelines
    ✓ Plugin architectures
    ✓ Decorator implementations
"""


# 1. Positional Arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")


display_info("Alice", 30)


# 2. Keyword Arguments
def display_info1(name, age):
    print(f"Name: {name}, Age: {age}")


display_info1(age=25, name="Bob")


# 3. Default Arguments
def display_info2(name, age=18):
    print(f"Name: {name}, Age: {age}")


display_info2("Charlie")
display_info2("David", 22)


# 4. Variable-length Arguments
def display_info3(*args):
    print(f"type of args: {type(args)}")
    for arg in args:
        print(arg, end=",")
    print()


display_info3("Eve", 28, "Engineer")


def display_info4(**kwargs):
    print(f"type of kwargs: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=" , ")
    print()


display_info4(name="Frank", age=35, profession="Doctor")


def display_info5(name, rollno):
    print(f"Name: {name}, Roll No: {rollno}")


student_info = ["Grace", 101]
display_info5(*student_info)  # Unpacking list to positional arguments

# ================================================================================
#                   PART 4: RECURSION FUNCTIONS - PRACTICAL APPLICATIONS
# ================================================================================

'''
🔁 RECURSION FUNCTION INSIGHTS:
Recursion is a powerful programming technique where a function calls itself
to solve smaller instances of the same problem. 
This section explores various recursion patterns and their applications.
KEY CONCEPTS:
    • Base Case: The condition under which recursion stops
    • Recursive Case: The part where the function calls itself
    • Stack Overflow: Risk of excessive recursion depth
    • Tail Recursion: An optimized form of recursion PRACTICAL APPLICATIONS:
    ✓ Mathematical computations (factorials, Fibonacci)
    ✓ Data structure traversals (trees, graphs)
    ✓ Algorithm implementations (divide and conquer)
'''

'''
practice question recursion function
    1. Write a recursive function to calculate the factorial of a number.
    2. Write a recursive function to compute the nth Fibonacci number.
    3. Write a recursive function to find the greatest common divisor (GCD) of two numbers.
    4. Write a recursive function to reverse a string.
    5. Write a recursive function to sum the elements of a list.
    6. Write a recursive function to check if a string is a palindrome.
    7. Write a recursive function to find the maximum element in a list.
    8. Write a recursive function to generate all permutations of a string.
    9. Write a recursive function to flatten a nested list.
    10. Write a recursive function to solve the Tower of Hanoi problem.
'''


# 1. Write a recursive function to calculate the factorial of a number.
def fact_no(no):
    if no == 1:
        return no
    return no * fact_no(no - 1)


fact = fact_no(4)
print(f"factorial = {fact}")


# 2. Write a recursive function to compute the nth Fibonacci number.
def fibo(no, a=0, b=1):
    if no == 0:
        return
    print(a, end=",")
    c = a + b
    a = b
    b = c
    fibo(no - 1, a, b)


fibo(10)
print()


# 3. Write a recursive function to find the greatest common divisor (GCD) of two numbers.
def gcd(n1, n2):
    if n1 % n2 == 0:
        return n2
    return gcd(n2, n1 % n2)


n1 = 12
n2 = 8
gcd_no = gcd(n1, n2)
print(f'gcd = {gcd_no}')
lcm_no = (n1 * n2) // gcd_no
print(f'lcm = {lcm_no}')

# 4. Write a recursive function to reverse a string.
# 6. Write a recursive function to check if a string is a palindrome.

name = input("enter string = ")


def rev(name1):
    if len(name1) <= 1:
        return name1
    return rev(name1[1:]) + name1[0]


reverse = rev(name)
print(f'reverse string = {reverse}')

if reverse in name:
    print(f"{name} is palindrome")
else:
    print(f"{name} is not palindrome")


# 5. Write a recursive function to sum the elements of a list.
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])


numbers = [1, 2, 3, 4, 5]
total_sum = sum_list(numbers)
print(f"Sum of list elements: {total_sum}")


# 7. Write a recursive function to find the maximum element in a list.
def max_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = max_in_list(lst[1:])
        if lst[0] > max_of_rest:
            return lst[0]
        else:
            return max_of_rest

print(f"max = {max_in_list(numbers)}")

# 8. Write a recursive function to generate all permutations of a string.
def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)
print("permutations of string:")
permute("ABC")

# 9. Write a recursive function to flatten a nested list.
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
nested = [1, [2, [3, 4], 5], 6, [7, 8]]
flat = flatten(nested)
print(f"Flattened list: {flat}")

# 10. Write a recursive function to solve the Tower of Hanoi problem.
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)
num_disks = 3
print("Tower of Hanoi solution:")
tower_of_hanoi(num_disks, 'A', 'C', 'B')