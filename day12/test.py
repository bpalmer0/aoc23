import pytest
from typing import List
from main import is_valid


@pytest.mark.parametrize(
    "record,groups,expected",
    [
        ("#.#.###", [1, 1, 3], True),
        ("#....######..#####.", [1, 6, 5], True),
        (".#.###.#.######", [1, 3, 1, 6], True),
        ("#....######..#####.", [1, 6], False),
        ("#..######..###.", [1, 6, 5], False),
        ("#..######..###.", [1, 6, 5], False),
    ],
)
def test_is_valid(record: str, groups: List[int], expected: bool) -> None:
    assert is_valid(record, groups) == expected
