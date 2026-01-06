# Write a Python program to create an abstract class Shape with an abstract method area().
# Then, create a child class Square that inherits from Shape and implements the area() method.
# The program should:
# -----------------------------------------------
# Take the side of the square as input from the user
# calculate the value of square
# display the area as output
# ----------------------------------------------
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class square(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side*self.side 

class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width  

    def area(self):
        return self.length*self.width
     


side=float(input('Enter the side of the square'))
length=int(input("Enter a length of rectangle:  "))
width=int(input("Enter a width of rectangle:  "))

Square = square(side)
rect=rectangle(length, width)

print("area of the square:   ",Square.area())
print("area of the rectangle:  ",rect.area())


# completed------------------------abstract class....


    
        
