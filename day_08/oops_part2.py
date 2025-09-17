################################################################################
#              ENCAPSULATION (Access Modifiers in Python)                     #
################################################################################

"""
🔹 What is Encapsulation?
    - Encapsulation = binding data (variables/attributes) and methods (functions) together into a single unit (class).
    - It also means restricting direct access to some data for security, hiding internal implementation, and providing controlled access.

🔹 Access Modifiers in Python
    - Unlike Java/C++, Python does not have strict keywords (public, private, protected).
    - Instead, it uses naming conventions with underscores:

    (1) Public (default)
        - No underscore → accessible everywhere (inside & outside the class).
        - Example: self.name

    (2) Protected (_single_underscore)
        - Meant for internal use, but still accessible outside.
        - Just a convention (developers should not use it directly).
        - Example: self._salary

    (3) Private (__double_underscore)
        - Python name-mangles it → __variable becomes _ClassName__variable.
        - Cannot be accessed directly outside the class.
        - Example: self.__password
"""


class Employee:
    def __init__(self, name, salary, password):
        self.name = name
        self._salary = salary
        self.__password = password

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"Password: {self.__password}")

    def update_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Old password is incorrect.")


# Creating an Employee object
emp = Employee("Alice", 50000, "mypassword")
emp.show_details()
print()
# Accessing public attribute
print(emp.name)  # Alice
# Accessing protected attribute (not recommended)
print(emp._salary)  # 50000
# Accessing private attribute (will raise AttributeError)
# print(emp.__password)  # AttributeError
# Accessing private attribute using name mangling (not recommended)
print(emp._Employee__password)  # mypassword
print()
# Updating password using method
emp.update_password("mypassword", "newpassword")
emp.show_details()
# Trying to update password with wrong old password
emp.update_password("wrongpassword", "anotherpassword")
emp.show_details()

################################################################################
#                             INHERITANCE                                    #
################################################################################

'''
🔹 What is Inheritance?
    - Inheritance = acquiring properties (attributes) and behavior (methods) of one class into another.
    - Promotes code reusability and hierarchical relationships.
    - Existing class = Parent/Base/Superclass
    - New class = Child/Derived/Subclass
    
🔹 Types of Inheritance in Python

    (1) Single Inheritance
        - One child inherits from one parent.      
        
    (2) Multi-level Inheritance
        - A chain of inheritance.
        
    (3) Multiple Inheritance
        - One child inherits from multiple parents.
        
    (4) Hierarchical Inheritance
        - Multiple children inherit from one parent.
        
    (5) Hybrid Inheritance
        - Combination of two or more types.
        - Uses MRO (Method Resolution Order) to solve conflicts.
        
🔹 Method Resolution Order (MRO)
    - In multiple inheritance, Python follows the C3 linearization (MRO algorithm).
    - Order can be checked by:
    - print(C.__mro__)   # or C.mro()        
    
🔹 super() Function
    - Used to call parent class constructor or methods.
    - Helps avoid rewriting and supports MRO.
    
🔹  Method Overriding
    - Child class can provide its own implementation of a method defined in the parent class.
    - Allows dynamic behavior based on the object type.
'''


# 1. Single Inheritance
class Parent:
    def parent(self):
        print("parent class method")


class Child(Parent):
    def child(self):
        print("child class method")

    def parent(self):    # Overriding parent class method
        print("overridden parent class method in child class")


p = Parent() # Creating an object of Parent class
c = Child() # Creating an object of Child class

p.parent() # Accessing parent class method
c.parent() # Accessing inherited parent class method
c.child() # Accessing child class method
print()

# 2. Multi-level Inheritance
class GrandParent:
    def grand_parent(self):
        print("grand parent class method")


class Parent(GrandParent):
    def parent(self):
        print("parent class method")


class Child(Parent):
    def child(self):
        print("child class method")

    def parent(self):     # Overriding parentclass method
        print("overridden parent class method in child class")

gp=GrandParent()
p=Parent()
c=Child()

gp.grand_parent() # Accessing grand parent class method
p.grand_parent() # Accessing inherited grand parent class method
p.parent() # Accessing parent class method
c.grand_parent() # Accessing inherited grand parent class method
c.parent() # Accessing inherited parent class method
c.child() # Accessing child class method
print()

# 3. Multiple Inheritance
class Father:
    def father(self):
        print("father class method")

    def common(self):
        print("common method from father class")

class Mother:
    def mother(self):
        print("mother class method")

    def common(self):
        print("common method from mother class")

class Child(Mother,Father):
    def child(self):
        print("child class method")


c=Child()
c.father() # Accessing inherited father class method
c.mother() # Accessing inherited mother class method
c.child() # Accessing child class method
print(Child.__mro__) # Checking MRO
c.common() # Accessing common method (from Mother class due to MRO)

# super() function example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"[Person __init__] Name: {self.name}, Age: {self.age}")

    def display_info(self):
        print(f"Person Info → Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        # Parent class constructor call using super()
        super().__init__(name, age)
        self.student_id = student_id
        print(f"[Student __init__] Student ID: {self.student_id}")

    # Method overriding
    def display_info(self):
        # Calling parent class method using super()
        super().display_info()
        print(f"Student Info → ID: {self.student_id}")


# --- Testing ---
s1 = Student("Ansh", 22, "S101")
print("\nCalling display_info():")
s1.display_info()
