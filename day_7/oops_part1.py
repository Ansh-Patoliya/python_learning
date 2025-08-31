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
class Student:
    def __init__(self, name, roll):
        # if we don't use self then error will come like name is not defined
        self.name = name
        self.roll = roll

    # if we don't use self then error will come like display_info() takes 0 positional arguments but 1 was given
    def display_info(self):
        print(f"student name = {self.name}")
        print(f"student roll = {self.roll}")


s1 = Student("Ansh", 13)
s2 = Student("Priyansh", 8)

s1.display_info()
s2.display_info()
