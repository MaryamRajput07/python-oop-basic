from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Square class implementing Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# User input
side = float(input("Enter the side of the square: "))

# Object creation
square = Square(side)

# Display area
print("Area of the square:", square.area())
