def test_triangle_create(default_figure):
    assert default_figure["triangle"].name == "Triangle"
    assert default_figure["triangle"].a == 13
    assert default_figure["triangle"].b == 14
    assert default_figure["triangle"].c == 15


def test_triangle_get_area(default_figure):
    assert default_figure["triangle"].get_area() == 84.0


def test_triangle_get_perimeter(default_figure):
    assert default_figure["triangle"].get_perimeter() == 42
