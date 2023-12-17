from dataclasses import dataclass
from typing import List, Tuple
from itertools import permutations

grid = []
INF = 1000000


@dataclass
class Pos:
    x: int
    y: int

    def __add__(self, other: "Pos"):
        return Pos(self.x + other.x, self.y + other.y)

    def __eq__(self, other: "Pos"):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Path:
    positions: List[Pos]
    directions: List[Pos]
    cost: int

    def add(self, direction: Pos) -> "Path":
        new_end = self.positions[-1] + direction
        try:
            end_cost = grid[new_end.y][new_end.x]
        except IndexError:
            end_cost = INF
        new_directions = self.directions.copy()
        new_positions = self.positions.copy()
        new_directions.append(direction)
        new_positions.append(new_end)
        return Path(new_positions, new_directions, self.cost + end_cost)

    def is_complete(self) -> bool:
        return (
            self.positions[-1].x == len(grid[0]) - 1
            and self.positions[-1].y == len(grid) - 1
        )

    def is_valid(self) -> bool:
        # cannot cross over itself
        for pos in self.positions:
            if self.positions.count(pos) > 1:
                return False

        x_consecutive = 1
        y_consecutive = 1
        prev_x = self.directions[0].x
        prev_y = self.directions[0].y
        for dir in self.directions[1:]:
            if dir.x == prev_x:
                x_consecutive += 1
            else:
                x_consecutive = 1

            if dir.y == prev_y:
                y_consecutive += 1
            else:
                y_consecutive = 1

            if x_consecutive == 3 or y_consecutive == 3:
                return False
            prev_x = dir.x
            prev_y = dir.y
        return True


def main():
    with open("mini-input") as f:
        lines = f.read().strip().split("\n")
    for line in lines:
        row = []
        for c in line:
            row.append(int(c))
        grid.append(row)

    min_x_dir = len(grid[0]) - 1
    min_y_dir = len(grid) - 1
    print(min_x_dir + min_y_dir)
    min_cost = INF

    def get_bitstring(n) -> str:
        return "{0:b}".format(n)

    def is_valid(b) -> bool:
        return (
            "111" not in b
            and "000" not in b
            and b.count("1") == min_x_dir
            and b.count("0") == min_y_dir
        )

    for i, bitstring in enumerate(
        filter(is_valid, map(get_bitstring, range(2 ** (min_x_dir + min_y_dir))))
    ):
        print(i)
        path = Path([Pos(0, 0)], [], grid[0][0])
        for b in bitstring:
            if b == "1":
                path = path.add(Pos(1, 0))
            else:
                path = path.add(Pos(0, 1))
            if path.cost > min_cost:
                continue
        if path.cost < min_cost:
            min_cost = path.cost
            # print(path)
    print(min_cost)


if __name__ == "__main__":
    main()
