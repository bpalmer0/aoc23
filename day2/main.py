from dataclasses import dataclass
from typing import List


@dataclass
class Record:
    red: int
    green: int
    blue: int

    @classmethod
    def from_str(cls, record_str: str) -> "Record":
        """
        Parses a record from a string of comma separated values listing the number of cubes.
        Example: "1 red, 2 green, 3 blue"
        """
        cube_counts = record_str.split(", ")
        # we should not have more than 3 types of cube, if we do something has gone wrong
        if len(cube_counts) > 3:
            raise ValueError(
                f"Received a record with more than 3 cube types: {record_str}"
            )

        red = 0
        green = 0
        blue = 0

        while len(cube_counts) > 0:
            if cube_counts[0].endswith("red"):
                red = int(cube_counts[0].split(" ")[0])
                cube_counts = cube_counts[1:]

            elif cube_counts[0].endswith("green"):
                green = int(cube_counts[0].split(" ")[0])
                cube_counts = cube_counts[1:]

            elif cube_counts[0].endswith("blue"):
                blue = int(cube_counts[0].split(" ")[0])
                cube_counts = cube_counts[1:]
            else:
                raise ValueError(f'Unknown cube color in record "{record_str}"')

        return Record(red=red, green=green, blue=blue)

    def is_possible(self, red: int, green: int, blue: int) -> bool:
        """
        Determines if this record could possibly have occurred with the given numbers of cubes
        """
        return self.red <= red and self.green <= green and self.blue <= blue


@dataclass
class Game:
    id: int
    records: List[Record]

    @classmethod
    def from_str(cls, game_str: str) -> "Game":
        """
        Parses a game from a string starting with "Game <n>:" where n is the game id, followed by a list of
        record strings separated by colons.
        """
        split = game_str.split(": ")
        game_id = int(split[0].removeprefix("Game "))
        record_strs = split[1].split("; ")
        records = list(map(Record.from_str, record_strs))
        return Game(id=game_id, records=records)

    def is_possible(self, red: int, green: int, blue: int) -> bool:
        """
        Determines if this game is possible with the specified number of cubes
        """
        records_possible = list(
            map(lambda rec: rec.is_possible(red, green, blue), self.records)
        )
        game_is_possible = all(records_possible)
        return game_is_possible


def main() -> None:
    with open("input") as f:
        game_strs = f.readlines()
    game_strs = list(map(lambda s: s.strip(), game_strs))
    games = list(map(Game.from_str, game_strs))
    possible_games = list(filter(lambda game: game.is_possible(12, 13, 14), games))
    possible_game_ids = list(map(lambda game: game.id, possible_games))
    print(f"Valid game IDs: {possible_game_ids}")
    id_sum = sum(possible_game_ids)
    print(f"Sum of IDs: {id_sum}")


if __name__ == "__main__":
    main()
