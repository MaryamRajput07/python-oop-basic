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
# ---------------------------------------
# Assigment : getter method / setter methood in encapsulation
# ---------------------------------------
class Student:
    def __init__(self):
        self.__grade = None  

    # Getter method
    def get_grade(self):
        return self.__grade

    # Setter method 
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade")

    # Method to check 
    def is_passed(self):
        if self.__grade is not None:
            return "Passed" if self.__grade >= 50 else "Failed"
        return "No grade set"

# --- object ---
student1 = Student()


student1.set_grade(120)


student1.set_grade(85)

# Print results
print(f"Grade: {student1.get_grade()}")
print(f"Status: {student1.is_passed()}")
# ---------------------------------
# question no 2:
# ---------------------------------
class Product:
    def __init__(self):
        # Private attribute: shuru mein price 0 hogi
        self.__price = 0

    # Getter method: is se hum price check kar sakte hain
    def get_price(self):
        return self.__price

    # Setter method: price update karne ke liye, magar sirf positive value
    def set_price(self, amount):
        if amount > 0:
            self.__price = amount
        else:
            # Agar value 0 ya us se kam ho to error message
            print("Invalid price")

    # Discount lagane ka method
    def apply_discount(self, percent):
        # Discount sirf 0 se 100 percent ke darmiyan hona chahiye
        if 0 < percent < 100:
            discount_value = (self.__price * percent) / 100
            self.__price -= discount_value
        else:
            print("Invalid discount percentage")

# --- Test Script ---

# 1. Product ka object banaya
my_product = Product()

# 2. Galat price set karne ki koshish (Check validation)
my_product.set_price(-50)

# 3. Sahi price set ki
my_product.set_price(1000)
print(f"Price after setting: {my_product.get_price()}")

# 4. 20% discount apply kiya
my_product.apply_discount(20)

# 5. Final price print ki
print(f"Price after discount: {my_product.get_price()}")
# -------------------------------
# question no 3:
# -------------------------------
class Employee:
    def __init__(self):
        # Private attribute: shuru mein salary 0 hogi
        self.__salary = 0

    # Getter method: Is ke zariye hum salary ki value mangwa sakte hain
    def get_salary(self):
        return self.__salary

    # Setter method: Salary update karne ke liye, magar validation ke saath
    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
        else:
            # Agar salary negative ho to ye message print hoga
            print("Invalid salary")

    # Salary barhane ka method (Percentage ke hisab se)
    def increase_salary(self, percent):
        if percent > 0:
            increment = (self.__salary * percent) / 100
            self.__salary += increment
        else:
            print("Invalid percentage")

# --- Script to Test ---

# 1. Employee ka object banaya
emp = Employee()

# 2. Galat salary set karne ki koshish (Validation check)
emp.set_salary(-1000)

# 3. Sahi salary set ki
emp.set_salary(5000)
print(f"Salary after setting: {emp.get_salary()}")

# 4. Salary mein 10% izafa (increment) kiya
emp.increase_salary(10)

# 5. Final salary print ki
print(f"Salary after increment: {emp.get_salary()}")
# --------------------------------------------
# question 4:
# ------------------------------------------------
class Car:
    def __init__(self):
        # Private attribute: shuru mein speed 0 hogi
        self.__speed = 0

    # Getter method: Is ke zariye hum current speed pata kar sakte hain
    def get_speed(self):
        return self.__speed

    # Setter method: Speed update karne ke liye, magar validation ke saath
    def set_speed(self, value):
        if value >= 0:
            self.__speed = value
        else:
            # Agar speed negative ho to ye message print hoga
            print("Invalid speed")

    # Accelerate method: Speed barhane ke liye
    def accelerate(self, amount):
        self.__speed += amount

    # Brake method: Speed kam karne ke liye, magar 0 se niche nahi jayegi
    def brake(self, amount):
        self.__speed -= amount
        if self.__speed < 0:
            self.__speed = 0

# --- Script to Test ---

# 1. Car ka object banaya
my_car = Car()

# 2. Galat speed set karne ki koshish (Validation check)
my_car.set_speed(-20)

# 3. Sahi speed set ki (50)
my_car.set_speed(50)
print(f"Speed after setting: {my_car.get_speed()}")

# 4. 30 se accelerate kiya (50 + 30 = 80)
my_car.accelerate(30)
print(f"Speed after acceleration: {my_car.get_speed()}")


my_car.brake(100)

print(f"Speed after braking: {my_car.get_speed()}")

# 6. Final speed
print(f"Final speed: {my_car.get_speed()}")
# -----------------------------
# question no 5:
# -----------------------------

class BankAccount:
    def __init__(self):
        # Private attribute: shuru mein balance 0 hoga
        # __ lagane se ye variable class ke bahar se direct change nahi ho sakta
        self.__balance = 0

    # Getter method: Current balance check karne ke liye
    def get_balance(self):
        return self.__balance

    # Setter method: Balance set karne ke liye validation ke saath
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount")

    # Deposit method: Sirf positive amount jama karne ke liye
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    # Withdraw method: Balance nikalne ke liye (check balance logic ke saath)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

# --- Script to Test ---

# 1. BankAccount ka object banaya
account = BankAccount()

# 2. Negative number set karne ki koshish (Validation test)
account.set_balance(-100)

# 3. Money deposit ki (Set balance ke zariye 500 kiya)
account.set_balance(500)
print(f"Balance after deposit: {account.get_balance()}")

# 4. Money withdraw ki (300 nikale taake 200 bachein)
account.withdraw(300)
print(f"Balance after withdrawal: {account.get_balance()}")

# 5. Final balance getter use karte hue print kiya
print(f"Final balance: {account.get_balance()}")
# -------------------------completed.................










