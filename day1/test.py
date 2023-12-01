from main import *
import pytest

@pytest.mark.parametrize(
    "line,expected_value",
    [
        ("12345", 15),
        ("ab3lda0", 30),
        ("a1b2c3d4e5f", 15),
    ]
)
def test_get_calibration_value(line: str, expected_value: int) -> None:
    assert get_calibration_value(line) == expected_value


def test_sum_calibration_values() -> None:
    document = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
        ]

    assert sum_calibration_values(document) == 142
