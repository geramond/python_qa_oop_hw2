from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)
