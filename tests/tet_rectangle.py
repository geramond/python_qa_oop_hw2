def test_rectangle_create(default_figure):
    assert default_figure["rectangle"].name == "Rectangle"
    assert default_figure["rectangle"].a == 10
    assert default_figure["rectangle"].b == 5


def test_rectangle_get_area(default_figure):
    assert default_figure["rectangle"].get_area() == 50


def test_rectangle_get_perimeter(default_figure):
    assert default_figure["rectangle"].get_perimeter() == 30
