###################################################################
#                        POLYMORPHISM
###################################################################
"""
✅ Definition
    - Polymorphism means “one name, many forms”.
    - In Python OOPs, it allows the same function/method/operator to behave differently depending on the object or data type.

    - Types of Polymorphism

        (1) Function Polymorphism (Built-in functions working with different types)
        Example:
            print(len("Hello"))   # Works on string → output: 5
            print(len([1, 2, 3])) # Works on list → output: 3

        (2) Operator Overloading (Polymorphism with operators)
        Example:
            print(5 + 10)       # Addition → 15
            print("Hi" + "Bye") # Concatenation → "HiBye"
            print([1, 2] + [3]) # List merge → [1,2,3]

        (3) Method Overriding (Runtime Polymorphism)
            - A child class redefines a parent’s method with the same name.
        Example:

            class Animal:
                def sound(self):
                    print("Some generic sound")

            class Dog(Animal):
                def sound(self):
                    print("Bark")

            obj = Dog()
            obj.sound()  # Output: Bark

        (4) Method Overloading (Compile-time Polymorphism, but Python doesn’t support directly)
            - Python doesn’t support true method overloading.
            - But we can simulate using default arguments or *args / **kwargs.
        Example:
            class Calculator:
                def add(self, a=0, b=0, c=0):
                    return a + b + c

            obj = Calculator()
            print(obj.add(2, 3))      # 5
            print(obj.add(2, 3, 4))   # 9
"""

###################################################################
#                    ABSTRACTION
###################################################################
"""
1. What is Abstraction?
    - Abstraction means hiding the implementation details and showing only the essential features to the user.
    - Example:
        - When you drive a car, you just use the steering wheel, brakes, and accelerator.
        - You don’t need to know how the engine works internally.
        
    👉 In Python, abstraction is implemented using the abc module (Abstract Base Class).
    
2. Why Abstraction?
    - To reduce complexity.
    - To increase reusability.
    - To enforce a blueprint (rules) for child classes.
    
3. How to Implement Abstraction in Python?
    - Import ABC (Abstract Base Class) and abstractmethod from abc module.
    - Create an abstract class with abstract methods (methods without implementation).
    - Any child class must override these abstract methods, otherwise it cannot be instantiated.
    
4. Key Rules of Abstraction in Python
    - You cannot create objects of abstract classes.
    - v = Vehicle()  # ❌ Error
    - Abstract class may contain both abstract and normal methods.
    - All child classes must implement all abstract methods.
    - Abstract methods provide a blueprint for child classes.
"""
# Example of Abstraction in Python
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass   # Only declaration, no body

    @abstractmethod
    def stop(self):
        pass

# Child Class
class Car(Vehicle):
    def start(self):
        print("Car started 🚗")

    def stop(self):
        print("Car stopped 🛑")

class Bike(Vehicle):
    def start(self):
        print("Bike started 🏍️")

    def stop(self):
        print("Bike stopped 🛑")


# Testing
v1 = Car()
v1.start()
v1.stop()

v2 = Bike()
v2.start()
v2.stop()
