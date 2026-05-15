# Name: Bostero, Alexa C.

import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Rectangle(10, 5),
    Circle(5),
    Triangle(8, 6)
]

print("Rectangle Area:", shapes[0].area())
print("Circle Area:", round(shapes[1].area(), 1))
print("Triangle Area:", shapes[2].area())