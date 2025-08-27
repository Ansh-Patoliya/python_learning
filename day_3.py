"""String fundamentals practice.
Demonstrates:
 - Indexing & negative indexing
 - Slicing (start:stop semantics)
 - Immutability workaround via concatenation
 - Common transformation helpers (case change)
 - Whitespace trimming methods
 - Searching (find / rfind) & replacing
 - Splitting & joining
 - Prefix / suffix checks
 - Character category predicates (is* methods)
 - Counting substrings
 - Basic alignment & zero‑padding utilities

Notes:
 - All operations here return new string objects (strings are immutable in Python).
 - Examples intentionally print outputs directly for quick REPL-style feedback.
 - Edge cases (empty strings, absent substrings, multi-byte chars) can be explored similarly.
 - CPython stores small strings interning sometimes; not relied upon here.
"""

name="AnshPatoliya"  # Sample identifier-like string for experimentation
# Access is O(1); IndexError if you go outside bounds (not shown here).
print(name[0])    # First character
print(name[3])    # Fourth character (0-based index)
print(name[-3])   # Third from the end  # Negative indices offset from end.

# slicing
print(name[:4])   # First four chars (0..3)
print(name[4:])   # From index 4 to end  # Safe even if start >= len -> ''
print(name[3:6])  # Chars at indices 3,4,5  # Stop is non-inclusive.
# Slicing never raises IndexError when bounds exceed length; it clamps.

# name[0]="a" # error
# # str are immutable
print(name)
new_name="a"+name[1:]  # Rebuild string by concatenation (idiomatic immutability workaround)
# For many modifications consider list() or io.StringIO for efficiency.

# for changing case
'''
    upper() - ALL CAPS
    lower() - all small
    capitalize() - First letter capital
    title() - First letter of each word capital
'''
sentence="welcome to python programming"
print(sentence)             # Original
print(sentence.upper())     # All caps (locale-insensitive basic mapping)
print(sentence.lower())     # All lowercase (Unicode-aware but not locale-specialized)
print(sentence.capitalize())# First letter uppercase, rest lower
print(sentence.title())     # Title-case heuristic; may not handle apostrophes ideally in some locales
# Casefold() (not shown) is stronger form of lower() for caseless comparisons.

# removing spaces
'''
    lstrip() - remove left spaces
    rstrip() - remove right spaces
    strip() - remove both side spaces
'''
word="   hi   "
print(word,end=",")        # Shows raw with spaces preserved
print(word.lstrip(),end=",")  # Leading spaces removed (only whitespace chars)
print(word.rstrip(),end=",")  # Trailing spaces removed
print(word.strip(),end=",")   # Both sides removed
print()  # Newline separator
# strip does not alter internal spaces.

# finding and replacing
'''
    find() - find first occurrence of substring
    rfind() - find last occurrence of substring
    replace() - replace all occurrences of substring
    replace(old,new,count) - replace 'count' occurrences of old with new
'''
sentence = "I like java programming. java"
print(sentence)
print(sentence.find("java"))          # First occurrence index (or -1 if absent)
print(sentence.rfind("java"))         # Last occurrence index
print(sentence.replace("java","python"))      # Replace all occurrences (non-overlapping scan)
print(sentence.replace("java","python",1))    # Replace only first occurrence
# find vs index: index() raises ValueError if substring absent; find() returns -1.

# splitting and joining
'''
    split() - split string into list of substrings based on delimiter (default space)
    join() - join list of strings into single string with specified delimiter
'''
dates="27-8-2025"
print(f"date = {dates}")
date_parts=dates.split("-")   # ['27','8','2025']  # split(maxsplit=N) limits splits if needed.
print(f"date_parts = {date_parts}")

new_date="/".join(date_parts)  # Recombine with different delimiter; every element must be str.
print(f"new_date = {new_date}")
# join() more efficient than repeated concatenation in loops.

file_name="ap1331.txt"
print(file_name.startswith('ap'))  # True if prefix matches (can pass tuple for multiple prefixes)
print(file_name.endswith("pdf"))   # False example for suffix (tuple also supported)

# checking string content
'''
    isalnum() - checks if all characters are alphanumeric (letters and numbers)
    isalpha() - checks if all characters are alphabetic (letters only)
    isdigit() - checks if all characters are digits (numbers only)
    islower() - checks if all characters are lowercase
    isupper() - checks if all characters are uppercase
    isspace() - checks if all characters are whitespace (spaces, tabs, newlines)
'''
name='Ap1331'
print(name.isalnum())  # True: letters + digits
print(name.isalpha())  # False: digits present
print(name.isdigit())  # False: letters present (isdigit differs from isnumeric / isdecimal)
print(name.islower())  # False: has uppercase 'A'
print(name.isupper())  # False: not all uppercase
print(name.isspace())  # False: contains non-space chars
# isdigit() includes some Unicode digits; for numeric parsing prefer int(...) with try/except.

# counting occurrences
'''
count(substring) - counts how many times 'substring' appears in the string
'''
sentence="today is a rainy day, isn't it? though i like rainy days."
print(sentence)
print(sentence.count("rainy"))  # Non-overlapping; overlapping patterns require regex lookahead.
print(sentence.count("a"))      # Frequency of letter 'a'

# formatting strings
'''
    center(width,fillchar) - centers the string in a field of given width, padded
    ljust(width,fillchar) - left-justifies the string in a field of given width, padded
    rjust(width,fillchar) - right-justifies the string in a field of
    zfill(width) - pads the string on the left with zeros to fill the given width
'''
text="hello"
print(text.center(20,'*'))  # ******hello******* (balanced padding)  # If width <= len, returns original.
print(text.ljust(20,'*'))   # hello*************** (right padding)
print(text.rjust(20,'*'))   # ***************hello (left padding)
print(text.zfill(8))        # 000hello (numeric-style padding)  # Keeps sign ahead of zeros if present.

text="I am learning python. I am enjoying it."
print(text)
# find vs index: index() raises ValueError if substring absent; find() returns -1
print(text.index("am"))          # First occurrence index (raises ValueError if not found)
# print(text.index("hello"))      # Uncommenting this line would raise ValueError
# print(text.find("hello"))       # This would return -1 since "hello" is not in the text
