from main import *
from typing import List
import pytest


@pytest.mark.parametrize(
    "line,expected_value",
    [
        ("12345", 15),
        ("ab3lda0", 30),
        ("a1b2c3d4e5f", 15),
        ("two1nine", 29),
        ("zoneight234", 14),
        ("q35bvblmmqhmnine5zeightwoj", 32),
        ("twone3943sevenine", 29),
        ("nineight", 98),
        ("fiveight", 58),
        ("oneight", 18),
    ],
)
def test_get_calibration_value(line: str, expected_value: int) -> None:
    assert get_calibration_value(line) == expected_value


@pytest.mark.parametrize(
    "document,expected_sum",
    [
        (
            [
                "1abc2",
                "pqr3stu8vwx",
                "a1b2c3d4e5f",
                "treb7uchet",
            ],
            142,
        ),
        (
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ],
            281,
        )
    ],
)
def test_sum_calibration_values(document: List[str], expected_sum: int) -> None:
    assert sum_calibration_values(document) == expected_sum
