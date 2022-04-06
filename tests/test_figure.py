from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_figure_isinstance(default_figure):
    assert isinstance(default_figure["circle"], Circle)
    assert isinstance(default_figure["rectangle"], Rectangle)
    assert isinstance(default_figure["square"], Square)
    assert isinstance(default_figure["triangle"], Triangle)


def test_figure_add_area(default_figure):
    assert default_figure["circle"].add_area(default_figure["rectangle"]) == 364.1592653589793
    assert default_figure["circle"].add_area(default_figure["square"]) == 414.1592653589793
    assert default_figure["circle"].add_area(default_figure["triangle"]) == 398.1592653589793
    assert default_figure["rectangle"].add_area(default_figure["square"]) == 150
    assert default_figure["rectangle"].add_area(default_figure["triangle"]) == 134.0
    assert default_figure["square"].add_area(default_figure["triangle"]) == 184.0
