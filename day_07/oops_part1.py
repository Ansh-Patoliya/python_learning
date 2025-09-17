############################################################
#          📚 CLASSES AND OBJECTS IN PYTHON 🐍
############################################################
"""
🔹 Class
    - A blueprint / template for creating objects.
    - Defines attributes (data) and methods (functions/behavior).

    - Example: Car design / plan.

        class Car:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model
--------------------------------------------------------------------------------
🔹 Object
    - A real instance of a class.
    - Stores actual data.

    - Example: Real car made from the design.

        car1 = Car("Toyota", "Fortuner")   # object
        car2 = Car("Tesla", "Model X")     # object
--------------------------------------------------------------------------------
🔹 Key Differences
    - Class = Definition, Object = Instance.
    - Class does not hold data directly → Objects hold data.
    - One class can create many objects.
    - Class = Idea, Object = Reality.
--------------------------------------------------------------------------------
📌 Analogy:
    - Class = Pizza Recipe 🍕
    - Object = Actual Pizza you eat.

"""


###########################################################################
#            📚 TYPES OF VARIABLES AND METHODS IN PYTHON 🐍
###########################################################################
'''
🔹Attributes (Variables inside a Class)
    - Attributes = data/variables that belong to a class or object.
    - There are two types:
        (a) Instance Attributes:
            - Belong to each object individually.
            - Defined inside __init__ using self.
            - Every object has its own separate copy.
            
        (b) Class Attributes
            - Shared by all objects.
            - Defined outside __init__, directly inside class.
            
🔹Methods (Functions inside a Class)
    - Methods define behavior (actions) of objects.
    - There are 3 types of methods in Python:            
        (a) Instance Methods
            - Work with instance attributes.
            - Take self as the first parameter.
            - Can access & modify object’s attributes.
            
        (b) Class Methods
            - Work with class attributes.
            - Use a special decorator @classmethod.
            - Take cls (class) as the first parameter instead of self.
            
        (c) Static Methods
            - General utility methods, don’t use self or cls.
            - Use @staticmethod decorator.
            - Behaves like a normal function but kept inside a class for organization.
'''

# Example to illustrate different types of variables and methods in a class
class Student:
    school_name = "ABC School"  # class variable

    def __init__(self, name, roll):  # constructor / instance method
        # if we don't use self then error will come like name is not defined
        self.name = name  # instance variable
        self.roll = roll  # instance variable

    # if we don't use self then error will come like display_info() takes 0 positional arguments but 1 was given
    def display_info(self):  # instance method
        print(f"student name = {self.name}")
        print(f"student roll = {self.roll}")

    @classmethod
    def change_school_name(cls, new_name):  # class method
        cls.school_name = new_name

    @staticmethod
    def info(): # static method
        print("This is Student class")


s1 = Student("Ansh", 13)
s2 = Student("Priyansh", 8)

Student.info() # recommended way to call static method
# s1.info() # it will also work but not recommended
s1.display_info()
s2.display_info()
print(f"s1 object can access class variable = {s1.school_name}") # it will also work but not recommended
# class variable can be accessed by class name also
print(f"school name = {Student.school_name}") # recommended way to access class variable

Student.change_school_name("XYZ School") # recommended way to change class variable
# s1.change_school_name("PQR School") # it will also work but not recommended
print(f"after changing class variable")
print(f"s1 object can access class variable = {s1.school_name}")
print(f"class can access class variable = {Student.school_name}")




