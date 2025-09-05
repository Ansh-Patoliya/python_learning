# 📈 Python Learning Progress Log

---

## 🗓️ Day 0 – Setup (August 24, 2025)

### ✅ Setup

- Installed Python 3
- Configured Pycharm Code for Python development
- Connected Pycharm with GitHub

---

## 🗓️ Day 1 – Python Basics + Output Formatting (Aug 25, 2025)

### ✅ Concepts Learned

- Using `print()` with `sep` and `end` parameters
- Single-line (`#`) and multi-line (`'''...'''` or `"""..."""`) comments
- Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`
- Difference between string concatenation and numeric addition
- Using `input()`  to read multiple inputs

## 🗓️ Day 2 – Python Basics (Aug 26, 2025)

### ✅ Concepts Learned

- Variables and data types: `int`, `float`, `str` , `bool` , `complex`'
- Type conversion: `int()`, `float()`, `str()` , `bool()` , `complex()`
- Conditional statements: `if`, `elif`, `else`
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- Membership and identity operators: `in`, `not in`, `is`, `is not`
- loops: `for`, `while`
- Control statements: `break`, `continue`, `pass`

## 🗓️ Day 3 – python Basics (Aug 27, 2025)

### ✅ Concepts Learned

- String manipulation: indexing, slicing, methods like `upper()`, `lower()`, `find()`, `replace()`, `split()`, `join()`,
  `strip()`, `startswith()`, `endswith()`, `len()`, `count()`, `format()`, `isalpha()`, `isdigit()`, `islower()`,
  `isupper()` , `isalnum()`
- Escape sequences: `\n`, `\t`, `\\`, `\'`, `\"`

---

## 🗓️ Day 4 – Data Structures (Aug 28, 2025)

### ✅ Concepts Learned

- Lists: creation, indexing, slicing, methods like `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`,
  `reverse()`, `len()`, `count()`, `index()`, `clear()`, `copy()`,
- tuples: creation, indexing, slicing, immutability
- Dictionaries: creation, accessing values, adding/removing key-value pairs, methods like `keys()`, `values()`,
  `items()`, `get()`, `update()` , `pop()`, `popitem()`, `clear()`, `copy()`, `len()`
- Sets: creation, adding/removing elements, methods like `add()`, `remove()`, `discard()`, `union()`, `intersection()`,
  `difference()`, `symmetric_difference()`, `len()`, `clear()`, `copy()`

---

## 🗓️ Day 5 – Functions (Aug 29, 2025)

### ✅ Concepts Learned

- Type casting between data structures (list, tuple, dict, set)
- Function definition using `def`
- Function parameters and arguments (positional, keyword, default, variable-length)
- Return values using `return`
- Scope of variables (local vs global)
- Recursion

---

## 🗓️ Day 6 – File I/O and Exception Handling (Aug 30, 2025)

### ✅ Concepts Learned

- File operations: `open()`, `read()`, `readline()`, `readlines()`, `write()`, `writelines()`, `close()`
- File modes: `'r'`, `'w'`, `'a'`
- Using `with` statement for file handling
- Exception handling using `try`, `except`, `else`, `finally`
- Raising exceptions with `raise`
- Creating custom exceptions by defining new exception classes

---

## 🗓️ Day 7 – Modules , Packages, and Oops(part 1: basic concepts) (Aug 31, 2025)

### ✅ Concepts Learned

- Importing modules using `import` and `from ... import ...`
- Exploring built-in modules: `math`, `random`, `datetime`, `os`
- Python OS Module `getcwd()`, `chdir()`, `mkdir()`, `listdir()`, `remove()`,`rmdir()`
- Creating and using packages
- Object-Oriented Programming (OOP) concepts: classes, objects, attributes, methods

---

## 🗓️ Day 8 – Oops(part 2: advanced concepts) (Sep 1, 2025)

### ✅ Concepts Learned

- Encapsulation (public,private, protected attributes)
- Inheritance (single, multi-level, hierarchical, multiple,mro, super())
- Class methods using `@classmethod`
- Static methods using `@staticmethod`
- Instance methods

---

## 🗓️ Day 9 – Oops(part 3: advanced concepts) (Sep 2, 2025)

### ✅ Concepts Learned

- Polymorphism (method overloading, method overriding)
- Abstraction (abstract classes and methods using `abc` module)
- Magic methods (dunder methods) like `__init__`, `__str__`, `__repr__`, `__add__`, `__len__`, `__eq__`, `__lt__`, etc.

---

## 🗓️ Day 10 - Project work (Sep 3, 2025)

- completed the project and polished it.
- added comments and docstrings for better understanding.
- tested the project thoroughly to ensure all features work as expected.

--- 

## Project

## 🗓️ Day 7 - 10 - Expense Tracker Application (Aug 31 - Sep 3, 2025)

### ✅ Concepts Applied

- File I/O for data persistence
- Exception handling for robust user input handling
- Data structures for managing expenses and categories
- Functions for modular code
- User input and output formatting for better user experience
- Date and time handling using `datetime` module
- String manipulation for formatting and parsing data
- Conditional statements and loops for control flow
- Lists and dictionaries for storing and managing data

### Features Implemented

- Add Expense
- View Expenses Date wise
- Update Expense
- Delete Expense
- View Total Expense
- Search Expense by Date

---

## 🗓️ Day 11 - Learning Numpy (Phase 1,Phase 2) (Sep 4, 2025)

### ✅ Concepts Learned

- Introduction to NumPy and its advantages
- Phase 1:
    - Creating NumPy arrays using `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.random.random()`
    - Array attributes: `shape`, `dtype`, `size`, `ndim`
    - Basic array operations: addition, subtraction, multiplication, division
    - Reshaping arrays using `reshape()`, `flatten()`, `ravel()`, `transpose()`
    - difference between `flatten()` and `ravel()`

- Phase 2:
    - `Indexing` and `slicing` of arrays
    - `sorting` arrays using `np.sort()`
    - `Filtering`(`Boolean Indexing`) arrays without `mask` and with `mask`
    - `Fancy Indexing` vs. `where()` and conditional selection
    - `Stacking` arrays using `np.vstack()`, `np.hstack()`,
    - deleting elements using `np.delete()`

---  

## 🗓️ Day 12 - Learning Numpy (Phase 3) (Sep 5, 2025)

### ✅ Concepts Learned

- Phase 3:
    - dataset practice
    - `Mathematical Functions` : `np.sum()`, `np.mean()`, `np.min()`, `np.max()`, `np.argmin()`, `np.argmax()` ,
      `np.std()`, `np.var()`, `np.cumsum()`
    
- Phase 4:
    - `Universal` Functions : `np.comprod()`,`np.sqrt()`, `np.exp()`, `np.log()`, `np.sin()`, `np.cos()`,
      `np.tan()`, `np.arcsin()`, `np.arccos()`
    - `Rounding` functions : `np.round()`, `np.floor()`, `np.ceil()`, `np.trunc()`
    - `Statistical` functions : `np.median()`, `np.percentile()`, `np.corrcoef()`, `np.histogram()`
    - `Broadcasting` concept
    
[//]: # (- Phase 5:)

[//]: # (    - `Vectorization` concept)

[//]: # (    - `Linear Algebra` operations: `np.dot&#40;&#41;`, `np.cross&#40;&#41;`, `np.linalg.inv&#40;&#41;`, `np.linalg.det&#40;&#41;`, `np.linalg.eig&#40;&#41;`)

[//]: # (    - `Saving` and `Loading` arrays using `np.save&#40;&#41;`, `np.load&#40;&#41;`, `np.savetxt&#40;&#41;`, `np.loadtxt&#40;&#41;`)

[//]: # (    - `Copying` arrays using `np.copy&#40;&#41;`, `view&#40;&#41;`, and understanding deep vs shallow copy)

[//]: # (    - `Iterating` over arrays using `nditer&#40;&#41;`)

[//]: # (    - `Memory Layout` of arrays using `flags` attribute)

---