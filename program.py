# inheritance 
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


# Child Class
class Dog(Animal):
    def sound(self):
        print(self.name, "barks")


# Object
dog = Dog("Buddy")
dog.sound()

# abstraction 
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass


# Child Class
class Car(Vehicle):
    def start(self):
        print(self.name, "is starting")


# Object
car = Car("Toyota")
car.start()

