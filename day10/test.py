import pytest
from main import Pipe, NORTH, SOUTH, EAST, WEST


@pytest.mark.parametrize(
    "p1,p2,expected",
    [
        (Pipe((1, 1), "L", (NORTH, EAST)), Pipe((2, 1), "7", (SOUTH, WEST)), True),
        (Pipe((1, 1), "L", (NORTH, EAST)), Pipe((1, 0), "7", (SOUTH, WEST)), True),
        (Pipe((1, 1), "L", (NORTH, EAST)), Pipe((1, 2), "7", (SOUTH, WEST)), False),
        (Pipe((1, 1), "-", (WEST, EAST)), Pipe((1, 2), "|", (NORTH, SOUTH)), False),
    ],
)
def test_pipe_connects(p1: Pipe, p2: Pipe, expected: bool) -> None:
    assert p1.connects(p2) == expected
