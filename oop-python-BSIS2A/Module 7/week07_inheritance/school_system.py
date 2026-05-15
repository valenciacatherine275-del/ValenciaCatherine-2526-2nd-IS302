class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_info(self):
        super().display_info()
        print("Course:", self.course)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print("Subject:", self.subject)


student1 = Student("Alexa", 20, "BSIS")
teacher1 = Teacher("Mr. Tiongco", 30, "Programming")

print("Student Info:")
student1.display_info()

print("\nTeacher Info:")
teacher1.display_info()

# Name: Bostero, Alexa C.