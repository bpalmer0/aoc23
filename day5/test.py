import pytest
from main import Range, Map
from typing import List


@pytest.mark.parametrize(
    "range_str,expected",
    [
        ("50 98 2", Range(50, 98, 2)),
        ("45 77 23", Range(45, 77, 23)),
    ],
)
def test_range_from_str(range_str: str, expected: Range) -> None:
    assert Range.from_str(range_str) == expected


@pytest.mark.parametrize(
    "map_str,expected",
    [
        (
            ["seed-to-soil map:", "50 98 2", "45 77 23"],
            Map([Range(50, 98, 2), Range(45, 77, 23)]),
        ),
    ],
)
def test_map_from_str(map_str: List[str], expected: Map) -> None:
    assert Map.from_str(map_str) == expected


@pytest.mark.parametrize(
    "map,source,destination",
    [
        (
            Map(
                ranges=[
                    Range(destination=50, source=98, length=2),
                    Range(destination=52, source=50, length=48),
                ]
            ),
            10,
            10,
        ),
        (
            Map(
                ranges=[
                    Range(destination=50, source=98, length=2),
                    Range(destination=52, source=50, length=48),
                ]
            ),
            98,
            50,
        ),
        (
            Map(
                ranges=[
                    Range(destination=50, source=98, length=2),
                    Range(destination=52, source=50, length=48),
                ]
            ),
            99,
            51,
        ),
        (
            Map(
                ranges=[
                    Range(destination=50, source=98, length=2),
                    Range(destination=52, source=50, length=48),
                ]
            ),
            53,
            55,
        ),
    ],
)
def test_map(map: Map, source: int, destination: int) -> None:
    assert map.map(source) == destination
