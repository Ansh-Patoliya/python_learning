"""
================================================================================
            PYTHON DATA STRUCTURES - LISTS, TUPLES, DICTIONARIES, SETS
================================================================================
Author: Ansh Patoliya
Date: Day 4 of Python Learning Journey
Description: Complete implementation and examples of Python's core data structures:
             Lists, Tuples, Dictionaries, and Sets with practical examples

Learning Objectives:
- Understand mutable vs immutable data structures
- Master CRUD operations on different data types
- Learn data structure methods and best practices
- Implement type casting between different structures
- Practice with real-world examples and use cases

================================================================================


                                TABLE OF CONTENTS
================================================================================
PART 1: LISTS - Mutable Ordered Collections
PART 2: TUPLES - Immutable Ordered Collections
PART 3: DICTIONARIES - Key-Value Pair Collections
PART 4: SETS - Unique Element Collections
PART 5: TYPE CASTING - Converting Between Data Structures

================================================================================
"""
# ================================================================================
#                           PART 1: LISTS - MUTABLE ORDERED COLLECTIONS
# ================================================================================
"""
LISTS OVERVIEW:
- Mutable: Can be modified after creation
- Ordered: Elements maintain their position
- Indexed: Access elements by position (0-based indexing)
- Heterogeneous: Can store different data types
- Dynamic: Size can change during runtime
- Use Cases: Shopping carts, user lists, dynamic data storage
"""

# Creating a list
my_list=[1,2,3.1,'hello',[4,5],4]
print(my_list)

# Accessing elements
print(my_list[2])
print(my_list[4][1])

# Modifying elements
my_list.append("ansh")
my_list.insert(3,4)
print(my_list)
my_list.extend([7,8,9])
print(my_list)

# List slicing
sub_list=my_list[1:5]
print(sub_list)

# List methods
print(f"count = {my_list.count(4)}")
print(f"index = {my_list.index(4,4,8)}")
print(f"len = {len(my_list)}")

new_list=[32,31,89,2,0,3]
new_list.sort()
print(f"sorted = {new_list}")
new_list.reverse()
print(f"reverse = {new_list}")

# Removing elements
my_list.remove("hello")
ele=my_list.pop(4)
my_list.pop()
print(f"poped element = {ele} , list = {my_list}")

# Iterating through a list
for listed in my_list:
    print(listed,end="-->")

# copying a list
copy_list=my_list.copy()
print(f" copy list = {copy_list}")
my_list.pop()
print(f"after change , old list = {my_list} , copy list = {copy_list}")

# Clearing a list
my_list.clear()
print(my_list)

# List comprehension
squared=[x**2 for x in range(6)]  # Create a list of squares
print(squared)                    # Display squared list
# Lists are versatile and widely used in Python for various applications, from simple data storage to complex data manipulation tasks.

'''
    # list of all important list methods in python
        1. append(x) - Adds an item x to the end of the list.
        2. extend(iterable) - Extends the list by appending elements from the iterable.
        3. insert(i, x) - Inserts an item x at a given position i.
        4. remove(x) - Removes the first occurrence of an item x from the list.
        5. pop([i]) - Removes and returns the item at position i (default is the last item).
        6. clear() - Removes all items from the list.
        7. index(value,start,end) - Returns the index of the first occurrence of an item x (optionally within a specified range).
        8. count(x) - Returns the number of occurrences of an item x in the list.
        9. sort(key=None, reverse=False) - Sorts the items of the list in place
        10. reverse() - Reverses the elements of the list in place.
        11. copy() - Returns a shallow copy of the list.

--> what is shallow copy and deep copy in python with example
    ->Shallow Copy: A shallow copy of an object creates a new object, but inserts references into it to the objects found in the original.
                    This means that if the original object contains other objects (like lists or dictionaries), the shallow copy will reference those same objects, not create new ones.
 
    ->Deep Copy: A deep copy of an object creates a new object and recursively adds copies of nested objects found in the original.
                This means that all objects are duplicated, and the new object is completely independent of the original.
    
Example:

        original = [1, 2, [3, 4]]
        shallow_copied = copy.copy(original)
        deep_copied = copy.deepcopy(original)
        print("Original:", original)               # Output: [1, 2, [3, 4]]
        print("Shallow Copied:", shallow_copied)   # Output: [1, 2, [3, 4]]
        print("Deep Copied:", deep_copied)               # Output: [1, 2, [3, 4]]
        # Modifying the nested list in the original
        original[2][0] = 'Changed'
        print("After modifying original:")
        print("Original:", original)               # Output: [1, 2, ['Changed', 4]]
        print("Shallow Copied:", shallow_copied)   # Output: [1, 2, ['Changed', 4]]
        print("Deep Copied:", deep_copied)               # Output: [1, 2, [3, 4]]
# As you can see, the shallow copy reflects changes made to the nested list in the original, while the deep copy remains unaffected.
'''

'''
practice problems on list in python
1. Write a Python program to create a list of the first 10 square numbers (1, 4, 9, ..., 100).
2. Write a Python program to find the largest and smallest numbers in a list of integers.
3. Write a Python program to remove duplicates from a list while preserving the order of elements.
'''

# 1. Write a Python program to create a list of the first 10 square numbers (1, 4, 9, ..., 100).
print([x**2 for x in range(11)])

# 2. Write a Python program to find the largest and smallest numbers in a list of integers.
my_list=[27,43,67,12,8]
my_list.sort()
print(f"max = {my_list[len(my_list)-1]} , min =  {my_list[0]}")

# 3. Write a Python program to remove duplicates from a list while preserving the order of elements.
my_list=[1,2,3,4,3,2,1,5,6,7,5]
new_list=[]
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

# ================================================================================
#                           PART 2: TUPLES - IMMUTABLE ORDERED COLLECTIONS
# ================================================================================
"""
TUPLES OVERVIEW:
- Immutable: Cannot be modified after creation
- Ordered: Elements maintain their position
- Indexed: Access elements by position (0-based indexing)
- Heterogeneous: Can store different data types
- Fixed Size: Size is determined at creation and cannot change
- Use Cases: Coordinate pairs, RGB color values, fixed data collections
"""
# Tuple

my_tuple=(1,2,3.1,'hello',(4,5),4)
print(my_tuple)
# Accessing elements
print(my_tuple[2])
print(my_tuple[4][1])
# Modifying elements - Tuples are immutable, so we cannot modify them directly
# However, we can create a new tuple by concatenation
new_tuple=my_tuple[:3]+('ansh',)+my_tuple[3:]
print(new_tuple)
# Tuple slicing
sub_tuple=my_tuple[1:5]
print(sub_tuple)
# Tuple methods
print(f"count = {my_tuple.count(4)}")
print(f"index = {my_tuple.index(4,4,8)}")
print(f"len = {len(my_tuple)}")
# Iterating through a tuple
for tup in my_tuple:
    print(tup,end="-->")
# Tuple comprehension is not possible, but we can use generator expressions
squared=tuple(x**2 for x in range(6))  # Create a tuple of squares
print(squared)                        # Display squared tuple
# Tuples are widely used in Python for various applications, especially when an immutable sequence of data is needed.



'''
    # tuple all important methods
        1. count(x) - Returns the number of occurrences of an item x in the tuple.
        2. index(value,start,end) - Returns the index of the first occurrence of an item x (optionally within a specified range).
'''

# ================================================================================
#                       PART 3: DICTIONARIES - KEY-VALUE PAIR COLLECTIONS
# ================================================================================
"""
DICTIONARIES OVERVIEW:
- Mutable: Can be modified after creation
- Unordered: No guaranteed order of elements
- Indexed by Keys: Access values by their unique keys
- Heterogeneous: Can store different data types
- Dynamic: Size can change during runtime
- Use Cases: Storing user data, configuration settings, mapping relationships
"""
# Creating a dictionary
my_dict={
    'name':"Ansh",
    'roll_no':18,
    "email":'ap1331@gmail.com',
    'interest':["sport","coding"]
}
print(my_dict)

key=my_dict.keys() # get all keys
print(f"keys = {key} , type = {type(key)}")

value=my_dict.values() # get all values
print(f"values = {value} , type = {type(value)}")

item=my_dict.items() # get all items
print(f"items = {item} , type = {type(item)}")

print(f"get = {my_dict.get("interest")}") # get value of key

new_dict={
    "interest":["sport","coding","reading"]
}

print(f"before updated dict. = {my_dict}")
my_dict.update(new_dict) # update dictionary
print(f"after updated dict. = {my_dict}")

my_dict.setdefault("city","ahmedabad") # set default value if key not present
print(f"city add = {my_dict}")

print(f"before pop = {my_dict}")
my_dict.pop("interest") # remove key and return its value
print(f"after pop = {my_dict}")

print(f"before pop = {my_dict}")
my_dict.popitem() # remove and return an arbitrary (key, value) pair
print(f"after pop = {my_dict}")

'''
    # dictionary all important methods
        1. keys() - Returns a view object that displays a list of all the keys in the dictionary.
        2. values() - Returns a view object that displays a list of all the values in the dictionary.
        3. items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs.
        4. get(key, default=None) - Returns the value for key if key is in the dictionary, else default.
        5. update([other]) - Updates the dictionary with the key/value pairs from other, overwriting existing keys.
        6. setdefault(key, default=None) - Returns the value of key if it is in the dictionary; if not, inserts key with a value of default and returns default.
        7. pop(key, default=None) - Removes the specified key and returns the corresponding value. If key is not found, default is returned if provided, otherwise KeyError is raised.
        8. popitem() - Removes and returns an arbitrary (key, value) pair from the dictionary. Raises KeyError if the dictionary is empty.
        9. copy() - Returns a shallow copy of the dictionary.
        10. clear() - Removes all items from the dictionary.
'''

# ================================================================================
#                           PART 4: SETS - UNIQUE ELEMENT COLLECTIONS
# ================================================================================
"""
SETS OVERVIEW:
- Mutable: Can be modified after creation
- Unordered: No guaranteed order of elements
- Unindexed: Cannot access elements by position
- Heterogeneous: Can store different data types
- Dynamic: Size can change during runtime
- Use Cases: Removing duplicates, membership testing, mathematical set operations
"""

'''
    # set all important methods
        1. add(elem) - Adds an element elem to the set.
        2. update(*others) - Updates the set, adding elements from all others.
        3. remove(elem) - Removes an element elem from the set. Raises KeyError if elem is not found.
        4. discard(elem) - Removes an element elem from the set if it is a member. Does nothing if elem is not found.
        5. pop() - Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
        6. clear() - Removes all elements from the set.
        7. union(*others) - Returns a new set with elements from the set and all others.
        8. intersection(*others) - Returns a new set with elements common to the set and all others.
        9. difference(*others) - Returns a new set with elements in the set that are not in the others.
        10. symmetric_difference(other) - Returns a new set with elements in either the set or other but not in both.
        11. difference_update(*others) - Removes elements found in others from the set.
        12. intersection_update(*others) - Updates the set, keeping only elements found in it and all others.
        13. symmetric_difference_update(other) - Updates the set with the symmetric difference of itself and other.
        14. isdisjoint(other) - Returns True if the set has no elements in common with other.
        15. issubset(other) - Returns True if every element in the set is in other.
        16. issuperset(other) - Returns True if every element in other is in the set.
        17. copy() - Returns a shallow copy of the set.
'''

