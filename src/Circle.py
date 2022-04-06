from src.Figure import Figure
import math


class Circle(Figure):

    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def get_area(self):
        return math.pi * (self.r ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.r


# c = Circle("Circle", 1)
# print(c.get_area())
# print(c.get_perimeter())
