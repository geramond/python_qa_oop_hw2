def test_square_create(default_figure):
    assert default_figure["square"].name == "Square"
    assert default_figure["square"].a == 10


def test_square_get_area(default_figure):
    assert default_figure["square"].get_area() == 100


def test_square_get_perimeter(default_figure):
    assert default_figure["square"].get_perimeter() == 40
