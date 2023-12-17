from dataclasses import dataclass
from typing import List, Tuple

grid = []


@dataclass
class Pos:
    x: int
    y: int

    def __add__(self, other: "Pos"):
        return Pos(self.x + other.x, self.y + other.y)


@dataclass
class Path:
    end: Pos
    directions: List[Pos]
    cost: int

    def add(self, direction: Pos):
        pass


def main():
    with open("mini-input") as f:
        lines = f.read().strip().split("\n")
    for line in lines:
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    sanity_check = Path(Pos(0, 0), [], 0)
