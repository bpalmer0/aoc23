import pytest
from main import Grid, Pixel

@pytest.fixture
def test_grid() -> Grid:
    with open("mini-input") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return Grid(lines)


def test_get_neighbors(test_grid) -> None:
    pixel = Pixel("%", False, 1, 0)
    neighbors = test_grid.get_neighbors(pixel)

    assert Pixel("4", False, 0, 0) in neighbors
    assert Pixel("6", False, 0, 1) in neighbors
    assert Pixel(".", False, 1, 1) in neighbors
    assert Pixel(".", False, 2, 0) in neighbors
    assert Pixel(".", False, 2, 1) in neighbors
