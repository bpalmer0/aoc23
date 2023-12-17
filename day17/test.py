import pytest
from typing import List
from main import Pos, Path, INF


@pytest.mark.parametrize(
    "p,expected",
    [
        (
            Path(
                [Pos(0, 0), Pos(0, 1), Pos(0, 2), Pos(0, 3)],
                [Pos(0, 1), Pos(0, 1), Pos(0, 1)],
                10,
            ),
            False,
        ),
        (
            Path(
                [Pos(0, 0), Pos(0, 1)],
                [Pos(0, 1)],
                12,
            ),
            True,
        ),
        (
            Path(
                [Pos(0, 0), Pos(0, 1), Pos(1, 1), Pos(1, 0), Pos(0, 0)],
                [Pos(0, 1), Pos(1, 0), Pos(0, -1), Pos(-1, 0)],
                15,
            ),
            False,
        ),
        (
            Path(
                positions=[
                    Pos(x=0, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=1),
                    Pos(x=1, y=2),
                    Pos(x=1, y=3),
                    Pos(x=2, y=3),
                    Pos(x=2, y=4),
                    Pos(x=2, y=5),
                    Pos(x=2, y=6),
                    Pos(x=2, y=7),
                    Pos(x=2, y=8),
                    Pos(x=2, y=9),
                    Pos(x=2, y=10),
                    Pos(x=2, y=11),
                    Pos(x=2, y=12),
                    Pos(x=3, y=12),
                    Pos(x=4, y=12),
                    Pos(x=5, y=12),
                    Pos(x=6, y=12),
                    Pos(x=7, y=12),
                    Pos(x=8, y=12),
                    Pos(x=9, y=12),
                    Pos(x=10, y=12),
                    Pos(x=11, y=12),
                    Pos(x=12, y=12),
                ],
                directions=[
                    Pos(x=1, y=0),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=1, y=0),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=0, y=1),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                    Pos(x=1, y=0),
                ],
                cost=98,
            ),
            False,
        ),
    ],
)
def test_is_valid(p: Path, expected: bool) -> None:
    assert p.is_valid() == expected


@pytest.mark.parametrize(
    "p,dir,expected",
    [
        (
            Path(
                [Pos(0, 0)],
                [],
                2,
            ),
            Pos(0, 1),
            Path([Pos(0, 0), Pos(0, 1)], [Pos(0, 1)], 2 + INF),
        )
    ],
)
def test_add(p: Path, dir: Pos, expected: Path) -> None:
    assert p.add(dir) == expected
