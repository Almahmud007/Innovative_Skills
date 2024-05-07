class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self):
        radius = float(input("Enter the radius of the circle: "))
        return 3.14 * radius ** 2

class Rectangle(Shape):
    def calculate_area(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return length * width

class Triangle(Shape):
    def calculate_area(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return 0.5 * base * height

def main():
    shape_types = { "circle": Circle(), "rectangle": Rectangle(), "triangle": Triangle()}

    shape_type = input("Enter shape type (circle, rectangle, triangle): ").lower()

    shape = shape_types[shape_type]
    if shape:
        print(f"Area of {shape_type} is {shape.calculate_area()}")
    else:
        print("Invalid shape")

if __name__ == "__main__":
    main()