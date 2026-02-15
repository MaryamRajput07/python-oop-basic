# (Parent) class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


# (Child) class
class Student(User):
    def __init__(self, name, email, course):
        super().__init__(name, email)
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")


# Object creation
student1 = Student(
    name="Maryam",
    email="maryam@example.com",
    course="Python Programming"
)

student1.display_info()
# completed----------------------------------
