import module_demo
import math
import random
import datetime
import os

############################################################################
#               MODULES - REUSING CODE FROM OTHER FILES
############################################################################
'''
modules - reusing code from other files
- A module is a file containing Python code (functions, variables, classes) that can be imported and used in other Python files.
- This helps organize code, avoid duplication, and promote code reuse.
- You can create your own modules or use built-in/third-party modules.
- To create a module, simply save your code in a .py file (e.g., module_demo.py).
- To use a module, you import it using the import statement.
- You can import the entire module or specific functions/variables from it.
'''
sum1=module_demo.add(10,4)
print(sum1)

from module_demo import sub
sub1=sub(12,10)
print(sub1)

############################################################################
#               MATH MODULE - WORKING WITH MATHEMATICAL FUNCTIONS
############################################################################
'''
important math module - working with mathematical functions
functions to explore:
- math.pi - value of π (3.14159...)
- math.e - value of e (2.71828...)
- math.tau - value of τ (6.28318...)
- math.sqrt(x) - square root of x   
- math.factorial(n) - factorial of n (n!)
- math.pow(x, y) - x raised to the power of y (x^y)
- math.ceil(x) - smallest integer >= x (rounds up)
- math.floor(x) - largest integer <= x (rounds down)
- math.sin(x), math.cos(x), math.tan(x) - trigonometric functions
- math.log(x, base) - logarithm of x to the given base
- math.gcd(a, b) - greatest common divisor of a and b
- math.lcm(a, b) - least common multiple of a and b (Python 3.9+)
- math.radians(x) - convert degrees to radians
- math.degrees(x) - convert radians to degrees
- math.isqrt(n) - integer square root of n (Python 3.8+)
- math.dist(p, q) - Euclidean distance between points p and q (Python 3.8+)
'''
print(f"Value of pi = {math.pi}")
print(f"Value of e = {math.e}")
print(f"Value of tau = {math.tau}")
print(f"Value of sqrt(2) = {math.sqrt(2)}")

############################################################################
#               RANDOM MODULE - WORKING WITH RANDOM NUMBERS
############################################################################
'''
important random module - working with random numbers
functions to explore:
    - random.random() - random float in [0.0, 1.0)
    - random.uniform(a, b) - random float between a and b ex. [1.0, 10.0)
    - random.randint(a, b) - random integer between a and b ex. [1, 10]
    - random.choice(seq) - randomly select an element from a non-empty sequence
    - random.choices(seq, weights=None, k=1) - randomly select k elements from a sequence with optional weights  
    - random.shuffle(seq) - shuffle the sequence in place
    - random.sample(population, k) - return a new list of k unique elements chosen from the population sequence
        → choices() allows duplicates, sample() does not.
    - random.seed(a=None) - initialize the random number generator with a seed for reproducibility
        ⚡ Seed value → "Randomness repeat karva no password".
        ⚡ Same seed → same sequence of random numbers.
'''
print(f"Random float between 0 and 1 = {random.random()}")
print(f"Random float between 1 and 10 = {random.uniform(1,10)}")
print(f"Random integer between 1 and 10 = {random.randint(1,10)}")
my_list=["apple","banana","cherry","date"]
print(f"Random choice from list = {random.choice(my_list)}")
random.shuffle(my_list)
print(f"Shuffled list = {my_list}")

##############################################################################
#               DATETIME MODULE - WORKING WITH DATES AND TIMES
##############################################################################
'''
important datetime module - working with dates and times
functions to explore:
    - datetime.datetime.now() - current date and time
    - datetime.datetime(year, month, day, hour, minute, second) - create specific date and time
    - datetime.date(year, month, day) - create a date object
    - datetime.time(hour, minute, second) - create a time object
    - datetime.timedelta(days, seconds, weeks) - represent a duration
    - datetime.datetime.strftime(format) - format date to string
    - datetime.datetime.strptime(date_string, format) - parse string to date
    - datetime.date.today() - current date
    - datetime.date.weekday() - day of the week (0=Monday, 6=Sunday)
'''
now=datetime.datetime.now()
print(f"Current date and time = {now}")
print(f"Current year = {now.year}")
print(f"Current month = {now.month}")
print(f"Current day = {now.day}")
print(f"Current hour = {now.hour}")
print(f"Current minute = {now.minute}")
print(f"Current second = {now.second}")

future_date=now + datetime.timedelta(days=10)
print(f"Date after 10 days = {future_date.date()}")

past_date=now-datetime.timedelta(weeks=5)
print(f"Date 5 weeks ago = {past_date.date()}")

# Formatting date to string
formatted_date=now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted current date and time = {formatted_date}")

# Parsing string to date
date_string="2023-08-15 14:30:00"
parsed_date=datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S")
print(f"Parsed date from string = {parsed_date}")

# user input date parsing
while True:
    user_date_str=input("Enter a date (YYYY-MM-DD): ")
    try:
        user_date=datetime.datetime.strptime(user_date_str,"%d-%m-%Y")
        print(f"You entered the date: {user_date.date()}")
        break
    except ValueError as e:
        print(e)

# sorting list of dates
date_list=["27-8-2025","1-1-2024","15-12-2023"]
date_objects=[datetime.datetime.strptime(date,"%d-%m-%Y") for date in date_list]
date_objects.sort()
sorted_dates=[date.strftime("%d-%m-%Y") for date in date_objects]
print(f"Sorted dates = {type(sorted_dates)}")

# sorting list of dicts by date
events=[
    {"name":"Event A","date":"15-09-2023"},
    {"name":"Event B","date":"01-01-2024"},
    {"name":"Event C","date":"10-08-2023"}
]

events.sort(key=lambda x: datetime.datetime.strptime(x["date"],"%d-%m-%Y"))
print("Events sorted by date:")
for event in events:
    print(f"{event['name']} on {event['date']}")

##############################################################################
#               OS MODULE - INTERACTING WITH THE OPERATING SYSTEM
##############################################################################
'''
os module - interacting with the operating system
functions to explore:
- os.getcwd() - get current working directory
- os.mkdir() - create a new directory
- os.chdir() - change current working directory
- os.listdir() - list files and directories in a path
- os.rmdir() - remove an empty directory
- os.remove() - delete a file
'''

print(f"Current working directory = {os.getcwd()}") # C:\Users\ansh\PycharmProjects\python_learning\day_7
print(f"Contents of current directory = {os.listdir()}") # ['module.py', 'module_demo.py', 'some_file.txt', '__init__.py', '__pycache__']
os.mkdir("test_dir")  # create a new directory named 'test_dir'
os.chdir("test_dir")  # change into the new directory
print(f"Changed working directory = {os.getcwd()}") # C:\Users\ansh\PycharmProjects\python_learning\day_7\test_dir
os.chdir("..")  # go back to parent directory (.. means "up one level")
print(f"Back to parent directory = {os.getcwd()}") # C:\Users\ansh\PycharmProjects\python_learning\day_7
os.rmdir("test_dir")  # remove the empty directory
print(f"Contents after removing test_dir = {os.listdir()}") # ['module.py', 'module_demo.py', 'some_file.txt', '__init__.py', '__pycache__']
os.remove("some_file.txt")  # delete a file named 'some_file.txt'
print(f"Contents after removing some_file.txt = {os.listdir()}") # ['module.py', 'module_demo.py', '__init__.py', '__pycache__']

# Note: Be careful with os.remove() and os.rmdir() as they permanently delete files/directories.
# Always ensure the file/directory exists and you have permission to delete it.