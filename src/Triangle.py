from src.Figure import Figure
import math


class Triangle(Figure):

    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c
