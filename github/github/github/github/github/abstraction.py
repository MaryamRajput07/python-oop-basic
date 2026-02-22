from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width  

    def area(self):
        return self.length * self.width

# Inputs
side = float(input("Enter the side of the square: "))
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

# Objects
sq = Square(side)
rect = Rectangle(length, width)

print("Area of square:", sq.area())
print("Area of rectangle:", rect.area())
# completed-----------------------------abstract class...
