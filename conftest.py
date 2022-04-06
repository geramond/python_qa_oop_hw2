import pytest

from src.Figure import Figure
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture()
def default_figure():
    circle = Circle("Circle", 10)
    rectangle = Rectangle("Rectangle", 10, 5)
    square = Square("Square", 10)
    triangle = Triangle("Triangle", 13, 14, 15)
    figures = {
        "circle": circle,
        "rectangle": rectangle,
        "square": square,
        "triangle": triangle
    }
    yield figures
    del figures, circle, rectangle, square, triangle
