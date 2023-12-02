import pytest
from main import Record, Game


@pytest.mark.parametrize(
    "record_str,expected_record",
    [
        ("1 red, 2 green, 3 blue", Record(red=1, green=2, blue=3)),
        ("2 green, 3 blue", Record(red=0, green=2, blue=3)),
        ("3 red, 3 blue", Record(red=3, green=0, blue=3)),
        ("15 blue", Record(red=0, green=0, blue=15)),
        ("7 green, 5 red, 7 blue", Record(red=5, green=7, blue=7)),
    ],
)
def test_record_parsing(record_str: str, expected_record: Record) -> None:
    assert Record.from_str(record_str) == expected_record


@pytest.mark.parametrize(
    "record,result",
    [
        (Record(red=1, green=2, blue=3), True),
        (Record(red=90, green=0, blue=3), False),
        (Record(red=12, green=13, blue=14), True),
    ],
)
def test_record_is_possible(record: Record, result: bool) -> None:
    x = record.is_possible(12, 13, 14)
    assert x == result


@pytest.mark.parametrize(
    "game_str,expected_game",
    [
        (
            "Game 1: 1 red, 2 green, 3 blue; 9 green",
            Game(
                id=1,
                records=[
                    Record(red=1, green=2, blue=3),
                    Record(red=0, green=9, blue=0),
                ],
            ),
        ),
        (
            "Game 2: 10 blue, 12 red; 8 red; 7 green, 5 red, 7 blue",
            Game(
                id=2,
                records=[
                    Record(red=12, green=0, blue=10),
                    Record(red=8, green=0, blue=0),
                    Record(red=5, green=7, blue=7),
                ],
            ),
        ),
    ],
)
def test_game_parsing(game_str: str, expected_game: Game) -> None:
    assert Game.from_str(game_str) == expected_game


@pytest.mark.parametrize(
    "game,result",
    [
        (
            Game(
                id=1,
                records=[
                    Record(red=1, green=2, blue=3),
                    Record(red=0, green=9, blue=0),
                ],
            ),
            True,
        ),
        (
            Game(
                id=1,
                records=[
                    Record(red=40, green=2, blue=3),
                    Record(red=0, green=9, blue=0),
                ],
            ),
            False,
        ),
    ],
)
def test_game_is_possible(game: Game, result: bool) -> None:
    x = game.is_possible(red=12, green=13, blue=14)
    assert x == result
