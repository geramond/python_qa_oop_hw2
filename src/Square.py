from src.Figure import Figure
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle


class Square(Figure):

    def __init__(self, name, a):
        super().__init__(name)
        self.a = a

    def get_area(self):
        return self.a ** 2

    def get_perimeter(self):
        return self.a * 4


circle = Circle("Circle", 10)
rectangle = Rectangle("Rectangle", 10, 5)
square = Square("Square", 10)
triangle = Triangle("Triangle", 13, 14, 15)

print(circle.add_area(rectangle))
print(circle.add_area(square))
print(circle.add_area(triangle))

print(rectangle.add_area(square))
print(rectangle.add_area(triangle))

print(square.add_area(triangle))

print("-----------")
print(circle.get_area())
print(rectangle.get_area())
print(square.get_area())
print(triangle.get_area())

print("-----------")
print(circle.get_perimeter())
print(rectangle.get_perimeter())
print(square.get_perimeter())
print(triangle.get_perimeter())
