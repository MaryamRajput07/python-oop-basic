# Parent Class (Base Class)
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")

# Child Class (Inheritance)
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        # super() ka istemal parent class ke __init__ ko call karne ke liye
        super().__init__(brand, year)
        self.doors = doors

    def display_info(self):
        super().display_info() # Parent ki info dikhayega
        print(f"Doors: {self.doors}")

# Object create karna
my_car = Car("Toyota", 2024, 4)

print("--- Car Details ---")
my_car.display_info()