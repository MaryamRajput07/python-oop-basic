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

# multi-level ihneritance staticmethod function
class car:
    colour='black'
    @staticmethod
    def start():
        print('car started...')
    @staticmethod
    def stop():
        print('car stopped...')
    
class toyota(car):
    def __init__(self, brand):
        self.brand = brand

class fortuner(toyota):
    def __init__(self, type):
        self.type = type

car1 = fortuner('diesel')
car1.start()



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

# polymorphism {megic methods}(__add__),(__str__):
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # object ko add kerne ke liye banaya hain 
    def __add__ (self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return point (new_x, new_y)
    # object ko thik se dikhane ke liye bnaya hai 
    def __str__(self):
        return f"({self.x},{self.y})"
# oject banaya hai class ka naam use ker ke our unko parameter bhe diye hain 
p1=point(1, 2)
p2=point(3, 4)
#  yahan aik variable banaya hai jahan se hum dono aik variable mai store karke valus laye sakhtye hai
p3 = p1 + p2
# yahan f string use ker ke print kia hai 
print (f"p1, p2 ka result hain:,{p3}")

# polymorphism with {__sub__} magic function:
class shop:
    def __init__(self,product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
    def __sub__(self,other):
        new_quantity = self.quantity - other.quantity
        return shop (self.quantity, other.quantity)
    def __str__(self):
        return f"{self.product_name} ka bacha hua stock: {self.quantity}"
product_name = shop('medicated cream:', 100)
total_sell = shop("total sell: " , 50)

remain_stock = product_name - total_sell
print(remain_stock)

# making private attribute in class 
class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

    def reset_pass(self):
        print(self.acc_pass)

account1 = account('1234', "abcd")
print(account1.acc_no)
print(account1.reset_pass())

        