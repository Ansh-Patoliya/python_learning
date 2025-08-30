"""
=============================================================================
            Python File I/O Operations - Day 6 Learning Module
=============================================================================

OVERVIEW:
    This script demonstrates fundamental file handling operations in Python using
    context managers (with statement) for proper resource management. The code
    showcases various file modes, reading/writing techniques, and file pointer
    manipulation on a text file called "Demo.txt".

KEY CONCEPTS COVERED:
    • File Modes: 'w' (write/overwrite), 'a' (append), 'r' (read)
    • Context Managers: Automatic file closure with 'with' statement
    • File Methods: write(), writelines(), read(), readline(), readlines()
    • File Pointer Operations: tell() for position, seek() for repositioning
    • Error Handling: Checking file accessibility before operations


BEST PRACTICES DEMONSTRATED:
    ✓ Using context managers for automatic resource cleanup
    ✓ Validating file accessibility before performing operations
    ✓ Understanding different reading strategies for various use cases
    ✓ Proper file pointer management and position tracking

=============================================================================
"""

# Writing to a file (overwrites existing content)
with open("Demo.txt","w") as f:
    if f.writable():
        f.writelines(["hi , ", "my name is ansh.\n", "and your?"])
    else:
        print("file is not writable")

# Appending to a file (adds content to the end)
with open("Demo.txt", "a") as f:
    f.write("hi,my name is ansh".title())
    f.write("\nHow are you?")
    print("good", file=f)
    f.close()

# Reading from a file
with open("Demo.txt","r") as f:
    if f.readable():
        print(f.read())
    else :
        print("file is not readable")
    f.close()

# Reading specific number of characters and checking file pointer position
with open("Demo.txt","r") as f:
    if f.readable():
        print(f.tell())
        print(f.read(2))
        print(f.tell())
    else :
        print("file is not readable")
    f.close()


# Reading line by line
with open("Demo.txt","r") as f:
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
    print(f"line 1 = {line1}")
    print(f"line 2 = {line2}")
    print(f"line 3 = {line3}")
    f.close()


# Reading all lines and checking file pointer position
with open("Demo.txt","r") as f:
    print(f.tell())
    for line in f:
        print(f"line = {line.strip()}")
    print(f.tell())
    f.close()


# Reading all lines into a list
with open("Demo.txt","r") as f:
    lines=f.readlines()
    print(lines)


# Demonstrating seek() to reset file pointer and read specific characters multiple times
with open("Demo.txt","r") as f:
    for i in range(0,11):
        print(f.read(4),end="")
        f.seek(0)