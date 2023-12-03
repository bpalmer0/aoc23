from typing import List
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Pixel:
    value: str
    alive: bool
    row: int
    col: int

    def __repr__(self) -> str:
        if self.alive:
            return self.value
        else:
            return "."

    def __str__(self) -> str:
        return self.__repr__()


class Grid:
    def __init__(self, grid: List[List[str]]):
        grid_height = len(grid)
        grid_width = len(grid[0])
        self.grid = [
            [Pixel(grid[row][col], False, row, col) for col in range(grid_width)]
            for row in range(grid_height)
        ]

    def display(self) -> None:
        for row in self.grid:
            print(row)

    def get_neighbors(self, pixel: Pixel, horizontal: bool = False) -> List[Pixel]:
        neighbors = []
        if horizontal:
            vectors = [(0, -1), (0, 1)]
        else:
            vectors = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
        for x, y in vectors:
            try:
                neighbors.append(self.grid[pixel.row + x][pixel.col + y])
            except IndexError:
                continue
        return neighbors

    def mark_symbols_alive(self) -> None:
        for row in self.grid:
            for pixel in row:
                if pixel.value != "." and not pixel.value.isdigit():
                    pixel.alive = True

    def get_alive_pixels(self) -> List[Pixel]:
        alive_pixels = []
        for row in self.grid:
            for pixel in row:
                if pixel.alive:
                    alive_pixels.append(pixel)
        return alive_pixels

    def grow(self, horizontal: bool = False) -> None:
        """
        Any Pixel that contains a digit and is adjacent to an alive Pixel will be made alive
        """
        all_neighbors = []
        for alive_pixel in self.get_alive_pixels():
            all_neighbors += self.get_neighbors(alive_pixel, horizontal)
        newly_alive = [pixel for pixel in all_neighbors if pixel.value.isdigit()]
        for pixel in newly_alive:
            pixel.alive = True

    def __str__(self) -> str:
        output = ""
        for row in self.grid:
            for pixel in row:
                output += str(pixel)
        return output


def main() -> None:
    with open("mini-input2") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    grid = Grid([[char for char in line] for line in lines])
    print("initial grid")
    grid.display()

    grid.mark_symbols_alive()
    old_grid = grid
    new_grid = deepcopy(old_grid)

    new_grid.grow()
    generation = 1
    print(f"generation {generation}")
    new_grid.display()
    while str(old_grid) != str(new_grid):
        old_grid = deepcopy(new_grid)
        print(f"generation {generation}")
        new_grid.grow(horizontal=True)
        new_grid.display()
        generation += 1

    number_stream = list(str(new_grid))
    for idx, char in enumerate(number_stream):
        if not char.isdigit():
            number_stream[idx] = "."
    number_stream = "".join(number_stream)
    print("Number stream:")
    print(number_stream)

    numbers = [int(number) for number in number_stream.split(".") if number != ""]
    print(f"Part Numbers: {numbers}")

    print(f"Sum of part numbers: {sum(numbers)}")


if __name__ == "__main__":
    main()
