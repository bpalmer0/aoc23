from dataclasses import dataclass, field
from typing import List

INF = 1000000


@dataclass
class Pos:
    x: int
    y: int

    def __add__(self, other: "Pos"):
        return Pos(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Pos"):
        return Pos(self.x - other.x, self.y - other.y)

    def __eq__(self, other: "Pos"):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def is_valid(directions: List[Pos]) -> bool:
    if len(directions) < 2:
        return True
    positions = []
    x_consecutive = 1
    y_consecutive = 1
    prev_x = directions[0].x
    prev_y = directions[0].y
    current_position = Pos(0, 0)
    for dir in directions[1:]:
        new_position = current_position + dir
        if new_position in positions:
            return False
        current_position = new_position

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


@dataclass
class Node:
    pos: Pos
    cost: int
    neighbors: List["Node"] = field(default_factory=list)
    updated_path: List[Pos] = field(default_factory=list)
    updated_cost: int = INF

    def get_neighbors(self, grid: List[List["Node"]]) -> List["Node"]:
        neighbors = []
        for dir in [Pos(1, 0), Pos(0, 1), Pos(-1, 0), Pos(0, -1)]:
            neighbor_pos = self.pos + dir
            if (
                neighbor_pos.x > len(grid[0]) - 1
                or neighbor_pos.y > len(grid) - 1
                or neighbor_pos.x < 0
                or neighbor_pos.y < 0
            ):
                continue
            neighbors.append(grid[neighbor_pos.y][neighbor_pos.x])
        return neighbors


def main():
    with open("mini-input") as f:
        lines = f.read().strip().split("\n")
    grid = []
    for r, line in enumerate(lines):
        row = []
        for c, char in enumerate(line):
            row.append(Node(Pos(c, r), int(char)))
        grid.append(row)

    start = grid[0][0]
    start.updated_cost = start.cost
    end = grid[-1][-1]
    curr = start
    while curr.pos != end.pos:
        # update estimates for neighbors
        neighbors = curr.get_neighbors(grid)
        for neighbor in neighbors:
            new_path = curr.updated_path.copy()
            new_path.append(neighbor.pos - curr.pos)
            if not is_valid(new_path):
                continue
            new_cost = curr.updated_cost + curr.cost
            if new_cost < neighbor.updated_cost:
                neighbor.updated_path = new_path
                neighbor.updated_cost = new_cost

        # select neighbor with lowest updated cost
        best_neighbor = sorted(neighbors, key=updated_cost)

    print(start.get_neighbors(grid))


if __name__ == "__main__":
    main()
