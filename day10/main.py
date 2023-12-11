from typing import Tuple, List, Optional
from dataclasses import dataclass

# (x, y) x is horizontal, y is vertical
NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)

symbol_to_directions = {
    "|": (NORTH, SOUTH),
    "-": (WEST, EAST),
    "L": (NORTH, EAST),
    "J": (NORTH, WEST),
    "7": (WEST, SOUTH),
    "F": (SOUTH, EAST),
    ".": None,
    "S": (SOUTH, EAST),
}


def opposite_direction(direction: Tuple[int, int]) -> Tuple[int, int]:
    return (-1 * direction[0], -1 * direction[1])


@dataclass
class Pipe:
    position: Tuple[int, int]
    symbol: str
    directions: Optional[Tuple[Tuple[int, int], Tuple[int, int]]] = None
    steps: Optional[int] = None

    def get_steps(self) -> str:
        if self.steps is None:
            return "."
        else:
            return str(self.steps)

    def get_symbol(self) -> str:
        if self.steps is None:
            return "."
        else:
            return self.symbol

    def connects(self, other: "Pipe") -> bool:
        if self.directions is None or other.directions is None:
            return False
        for direction in self.directions:
            expected_position = (
                self.position[0] + direction[0],
                self.position[1] + direction[1],
            )
            if (
                expected_position == other.position
                and opposite_direction(direction) in other.directions
            ):
                return True
        return False


def display_number_grid(grid: List[List[Pipe]]) -> None:
    for row in grid:
        row_str = "".join([pipe.get_steps() for pipe in row])
        print(f"{row_str}\n")


def display_symbol_grid(grid: List[List[Pipe]]) -> None:
    for row in grid:
        row_str = "".join([pipe.get_symbol() for pipe in row])
        print(f"{row_str}\n")


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
    for line in lines:
        print(line)
    # parse into grid
    pipe_grid = []
    s_pos = (0, 0)
    for y, row in enumerate(lines):
        pipe_row = []
        for x, c in enumerate(row):
            print(f"{x=}, {y=}, {c=}")
            if c == "S":
                steps = 0
                s_pos = (x, y)
            else:
                steps = None
            pipe = Pipe((x, y), c, symbol_to_directions[c], steps)
            pipe_row.append(pipe)
        pipe_grid.append(pipe_row)
    grid_height = len(pipe_grid)
    grid_width = len(pipe_grid[0])
    # determine starting directions
    s_directions = []
    s_pipe = pipe_grid[s_pos[1]][s_pos[0]]
    print(f"starting pipe at {s_pos}")
    for direction in [NORTH, SOUTH, EAST, WEST]:
        check_pos = (s_pos[0] + direction[0], s_pos[1] + direction[1])
        print(f"{check_pos=}")
        if (
            check_pos[0] < 0
            or check_pos[0] >= grid_width
            or check_pos[1] < 0
            or check_pos[1] >= grid_height
        ):
            continue
        check_pipe = pipe_grid[check_pos[1]][check_pos[0]]
        s_pipe.directions = (direction,)
        print(f"Checking if starting pipe has {direction}")
        print(f"Check pipe: {check_pipe}")
        if s_pipe.connects(check_pipe):
            s_directions.append(direction)
    s_pipe.directions = s_directions
    print(f"S directions are: {s_directions}")

    changed = True
    generation = 0
    while changed:
        changed = False
        print(f"Generation {generation}")
        # print("Symbols:")
        # display_symbol_grid(pipe_grid)
        # print("Numbers:")
        # display_number_grid(pipe_grid)

        for y, row in enumerate(pipe_grid):
            for x, pipe in enumerate(row):
                for direction in [NORTH, SOUTH, EAST, WEST]:
                    new_pos = (x + direction[0], y + direction[1])
                    if (
                        new_pos[0] < 0
                        or new_pos[0] >= grid_width
                        or new_pos[1] < 0
                        or new_pos[1] >= grid_height
                    ):
                        continue
                    new_pipe = pipe_grid[new_pos[1]][new_pos[0]]
                    if pipe.steps is None or new_pipe.steps is not None:
                        continue
                    if pipe.connects(new_pipe):
                        # print(f"Updating steps for {new_pos}")
                        changed = True
                        new_pipe.steps = pipe.steps + 1
        generation += 1
    print("Symbols:")
    display_symbol_grid(pipe_grid)
    max_steps = 0
    for row in pipe_grid:
        for pipe in row:
            if pipe.steps is not None and pipe.steps > max_steps:
                max_steps = pipe.steps
    print(f"Maximum distance away from start: {max_steps}")

    # part 2
    print("\n\nPart 2\n\n")
    for symbol, directions in symbol_to_directions.items():
        if directions is None or symbol == "S":
            continue
        if directions[0] in s_pipe.directions and directions[1] in s_pipe.directions:
            s_pipe.symbol = symbol

    num_enclosed = 0
    for row in pipe_grid:
        symbols = [pipe.get_symbol() for pipe in row]
        line = "".join(symbols)
        line = line.replace("-", "")
        line = line.replace("L7", "|")
        line = line.replace("FJ", "|")
        line = line.replace("LJ", "")
        line = line.replace("F7", "")
        print(line)
        enclosed = False
        for c in line:
            if c == "|":
                enclosed = not enclosed
            elif c == "." and enclosed:
                num_enclosed += 1
    print(f"Number of tiles enclosed: {num_enclosed}")


if __name__ == "__main__":
    main()
