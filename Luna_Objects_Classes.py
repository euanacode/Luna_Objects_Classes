# Circle

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius ** 2)
        print(f"Area of the circle with radius {self.radius} is {area:.2f}")

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle with radius {self.radius} is  {perimeter:.2f}")


if __name__ == "__main__":
    circle = Circle(2)
    circle.area()
    circle.perimeter()
