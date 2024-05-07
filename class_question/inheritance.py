# Question Answer of Inheritance

import math

class AreaCalculatorAll:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

    def calculate_triangle_area(self, base, height):
        return 0.5 * base * height

class Circle(AreaCalculatorAll):
    def __init__(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def calculate_area(self):
        return self.calculate_circle_area(self.radius)

class Rectangle(AreaCalculatorAll):
    def __init__(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))

    def calculate_area(self):
        return self.calculate_rectangle_area(self.length, self.width)

class Triangle(AreaCalculatorAll):
    def __init__(self):
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    def calculate_area(self):
        return self.calculate_triangle_area(self.base, self.height)

def main():
    choice = input("Enter shape type (circle, rectangle, triangle): ").lower()

    if choice == "circle":
        circle = Circle()
        area = circle.calculate_area()
        print(f"Area of the circle is {area:.2f}")

    elif choice == 'rectangle':
        rectangle = Rectangle()
        area = rectangle.calculate_area()
        print(f"Area of the rectangle is {area:.2f}")

    elif choice == 'triangle':
        triangle = Triangle()
        area = triangle.calculate_area()
        print(f"Area of the triangle is {area:.2f}")
    else:
        print("Invalid shape choice!")

if __name__ == "__main__":
    main()