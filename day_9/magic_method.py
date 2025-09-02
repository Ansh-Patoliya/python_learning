###########################################################
#                   MAGIC METHODS
###########################################################
"""
- Magic methods in Python are special methods that start and end with double underscores (also known as dunder methods).
- They allow you to define the behavior of your objects for built-in operations, such as arithmetic operations, comparisons, and type conversions.
- By implementing these methods in your classes, you can make your objects behave like built-in types.
- Common magic methods include:
    - `__init__`: Constructor method, called when an object is created.
    - `__new__`: Called to create a new instance of a class.
    - `__str__`: Defines the string representation of an object, used by the `str()` function and `print()`.
    - `__repr__`: Defines the official string representation of an object, used by the `repr()` function.
    - `__add__`: Defines behavior for the addition operator (`+`).
    - `__sub__`: Defines behavior for the subtraction operator (`-`).
    - `__mul__`: Defines behavior for the multiplication operator (`*`).
    - `__truediv__`: Defines behavior for the division operator (`/`).
    - `__eq__`: Defines behavior for the equality operator (`==`).
    - `__lt__`: Defines behavior for the less-than operator (`<`).
    - `__gt__`: Defines behavior for the greater-than operator (`>`).
    - `__len__`: Defines behavior for the built-in `len()` function.
    - `__getitem__`: Defines behavior for indexing and slicing.
    - `__setitem__`: Defines behavior for setting values via indexing.
    - `__delitem__`: Defines behavior for deleting values via indexing.
    - `__iter__`: Defines behavior for iteration.
    - `__enter__`: Defines behavior for context managers (used with `with` statements).
    - `__exit__`: Defines behavior for context managers (used with `with` statements
"""


# give an example complete of all magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vector):
            return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vector):
            return (self.x ** 2 + self.y ** 2) > (other.x ** 2 + other.y ** 2)
        return NotImplemented

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")

    def __delitem__(self, index):
        if index == 0:
            del self.x
        elif index == 1:
            del self.y
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        yield self.x
        yield self.y

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


# Example usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1)  # Output: Vector(2, 3)
print(v2)  # Output: Vector(4, 5)
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)
v4 = v2 - v1
print(v4)  # Output: Vector(2, 2)
v5 = v1 * 3
print(v5)  # Output: Vector(6, 9)
v6 = v2 / 2
print(v6)  # Output: Vector(2.0, 2.5)
print(v1 == v2)  # Output: False
print(v1 < v2)  # Output: True
print(v1 > v2)  # Output: False
print(len(v1))  # Output: 3
print(v1[0], v1[1])  # Output: 2 3
v1[0] = 10
print(v1)  # Output: Vector(10, 3)
del v1[1]
print(v1)  # Output: Vector(10, 3)
for component in v1:
    print(component)  # Output: 10 3
with v1 as vec:
    print(vec)  # Output: Vector(10, 3)
