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

## 🗓️ Day 12 - Learning Numpy (Phase 3,Phase 4) (Sep 5, 2025)

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
---

## 🗓️ Day 13 - Learning Numpy (Phase 5) (Sep 6, 2025)

### ✅ Concepts Learned
- Phase 5:
    - `Vectorization` concept
    - `Linear Algebra` operations: `np.dot()`, `np.cross()`, `np.linalg.inv()`, `np.linalg.det()`, `np.linalg.eig()`
    - `Saving` and `Loading` arrays using `np.save()`, `np.load()`, `np.savetxt()`, `np.loadtxt()`
    - `Copying` arrays using `np.copy()`, `view()`, and understanding deep vs shallow copy
    - `Iterating` over arrays using `nditer()`
    - `Memory Layout` of arrays using `flags` attribute
---

## 🗓️ Day 14 - Project: Sales Data Analyzer (Part 1) (Sep 7, 2025)

### ✅ Work Done

- Created project notebook and dataset; generated reproducible 3x12x4 sales array with NumPy
- Implemented helpers: `get_monthly_sale`, `get_yearly_product_sale`, `get_yearly_total_sale`
- Core analyses:
  - Per-product totals and averages across all years
  - Highest-sales product in 2023; highest total-sales year
  - Lowest-sales product in 2022; peak laptop month in 2024

---

## 🗓️ Day 15 - Project: Sales Data Analyzer (Part 2) (Sep 8, 2025)

### ✅ Work Done

- Advanced analyses and metrics:
  - Consistency via standard deviation; growth from 2022→2024 (percentage)
  - Inter-product correlations; threshold counts (>500) in 2023
  - 3-period moving averages per product (convolution)
  - Medians; Q1 2023 top product; lowest total-sales year; per-product ranges
  - December top product; skewness classification using mean vs median vs std
- Polished outputs with formatted strings and rounding

---

## 🗓️ Day 16 - JSON and CSV Modules (Sep 9, 2025)

### ✅ Concepts Learned
- JSON Module:
    - Understanding JSON format and its uses
    - Reading JSON data from a file using `json.load()`
    - Writing JSON data to a file using `json.dump()`
    - Converting Python objects to JSON strings using `json.dumps()`
    - Converting JSON strings to Python objects using `json.loads()`
- CSV Module:
    - Understanding CSV format and its uses
    - Reading CSV data from a file using `csv.reader()` and `csv.DictReader()`
    - Writing CSV data to a file using `csv.writer()` and `csv.DictWriter()`
---

## 🗓️ Day 17 - Learning Pandas (Part 1) (Sep 10, 2025)

### ✅ Concepts Learned
- Introduction to Pandas and its advantages
- how to read data from CSV file using `pd.read_csv()`, `pd.read_excel()`, `pd.read_json()`
- how to write data to CSV file using `to_csv()`, `to_excel()`, `to_json()`
- how to create Series and DataFrames using `pd.Series()`, `pd.DataFrame()`
- DataFrame attributes: `shape`, `columns`, `index`, `dtypes`, `info()`, `head()`, `tail()`, `describe()`
- Series attributes: `index`, `values`, `dtype`, `shape`, `head()`, `tail()`, `describe()`
---

## 🗓️ Day 18 - Learning Pandas (Part 2) (Sep 11, 2025)

### ✅ Concepts Learned
- Data selection and filtering using `loc[]`, `iloc[]`, boolean indexing
- column operations: adding, removing, renaming columns
---

## 🗓️ Day 19 - Learning Pandas (Part 3) (Sep 12, 2025)

### ✅ Concepts Learned
- Handling missing data using `isnull()`, `notnull()`, `dropna()`, `fillna()`
---

## 🗓️ Day 20 - Day 21 - Short break for Hackathon event (Sep 13 - 14, 2025)

### ✅ Work Done
- Participated in a Hackathon event to enhance coding skills and collaborate with others.
- Gained experience in problem-solving and working under time constraints.
- Took a break from regular learning to refresh and recharge.
---

## 🗓️ Day 22 - Learning Pandas (Part 4) (Sep 15, 2025)

### ✅ Concepts Learned

- Sorting using `sort_values()`, `sort_index()`
- Ranking using `rank()`
---
