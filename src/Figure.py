class Figure:

    def __init__(self, name):
        self.area = 0
        self.perimeter = 0
        self.name = name

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.get_area() + figure.get_area()
        else:
            raise ValueError("Wrong class passed")
