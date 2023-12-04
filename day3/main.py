from typing import List
from dataclasses import dataclass
from copy import deepcopy
from math import prod


@dataclass
class Pixel:
    value: str
    alive: bool
    row: int
    col: int
    # 0 means not part of a gear
    gear_id: int

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
            [Pixel(grid[row][col], False, row, col, 0) for col in range(grid_width)]
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
        gear_id = 1
        for row in self.grid:
            for pixel in row:
                if pixel.value != "." and not pixel.value.isdigit():
                    pixel.alive = True
                    if pixel.value == "*":
                        pixel.gear_id = gear_id
                        gear_id += 1

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
            for neighbor in self.get_neighbors(alive_pixel, horizontal):
                if neighbor.value.isdigit():
                    neighbor.alive = True
                    neighbor.gear_id = alive_pixel.gear_id

    def __str__(self) -> str:
        output = ""
        for row in self.grid:
            for pixel in row:
                output += str(pixel)
        return output


def part1(grid: Grid) -> None:
    numbers = []
    for row in grid.grid:
        number_stream = [str(pixel) for pixel in row]
        for idx, char in enumerate(number_stream):
            if not char.isdigit():
                number_stream[idx] = "."
        number_stream = "".join(number_stream)
        print("Number stream:")
        print(number_stream)

        numbers += [int(number) for number in number_stream.split(".") if number != ""]
    print(f"Part Numbers: {numbers}")

    print(f"Sum of part numbers: {sum(numbers)}")


def part2(grid: Grid) -> None:
    # keys are gear ids, values are gear numbers
    gear_numbers = {}
    wip_number = ""
    last_gear_id = 0

    def complete_number(gear_id: int, wip_number: str):
        number = int(wip_number)
        if gear_numbers.get(gear_id) is None:
            gear_numbers[gear_id] = [number]
        else:
            gear_numbers[gear_id].append(number)

    for row in grid.grid:
        for pixel in row:
            if pixel.gear_id > 0 and pixel.value != "*":
                wip_number += pixel.value
            if (not pixel.alive or pixel.value == "*") and wip_number != "":
                complete_number(last_gear_id, wip_number)
                wip_number = ""
            last_gear_id = pixel.gear_id
        if wip_number != "":
            complete_number(last_gear_id, wip_number)
            wip_number = ""

    print(f"Gear Number Candidates: {gear_numbers}")

    real_gear_numbers = [gn for gn in gear_numbers.values() if len(gn) == 2]
    print(f"Real gear numbers: {real_gear_numbers}")
    gear_ratios = [prod(gn) for gn in real_gear_numbers]
    print(f"Gear ratios: {gear_ratios}")
    gear_ratio_sum = sum(gear_ratios)
    print(f"Sum of gear ratios: {gear_ratio_sum}")


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

    part1(new_grid)
    part2(new_grid)


if __name__ == "__main__":
    main()
