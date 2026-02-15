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
class student:
    # class attribute(agar classs atrr our obj atrr same hoti hain tu..)
    college_name="ABCD COLLEGE"
    # do terha ke constructor hoty hain 1st defult, 2nd parameterized
    def __init__(self,name,marks,age,section):
    # properties < obj atrribut(ko prefrence diya jata hai )
        self.name=name
        self.marks=marks
        self.age=age
        self.section=section
# functions ko hi hum method bhe boltye hain 
    def welcome(self):
        print(f"welcome {self.name} to new classs section")
        # s1.self.name()
    def get_marks(self):
        return self.marks
# call karne ki liye direct method ka naam obj ke bad lagatye hain (s1.welcome())
# instance > object
# s1=student("aiman", 65, "20", "A")
class Student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
# yahan humne loop lagaya hain number ko add karke usko 3 se divide kya hai
    def get_marks(self):
        sum=0
        for val in self.marks:
            sum += val
        print(f"hi {self.name} your total marks is {sum/3}")
# staticmethod mai humy self prefrence ki zarrorat nahe hoti hain yah humy simple print provide karta hain
    @staticmethod
    def hello():
        print("hey buddy")

obj=Student("rayan",[20,30,40])
obj.get_marks()
# es se hum apne variables ke  value ka naam change kar sakhtye hain 
obj.name='shayan'
obj.get_marks()



    
    

        


    
        
