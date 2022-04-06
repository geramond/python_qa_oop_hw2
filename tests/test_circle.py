def test_circle_create(default_figure):
    assert default_figure["circle"].name == "Circle"
    assert default_figure["circle"].r == 10


def test_circle_get_area(default_figure):
    assert default_figure["circle"].get_area() == 314.1592653589793


def test_circle_get_perimeter(default_figure):
    assert default_figure["circle"].get_perimeter() == 62.83185307179586
