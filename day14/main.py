from typing import List


def sum_column(column: List[str]) -> int:
    sum = 0
    for i, c in enumerate(column):
        if c == "O":
            sum += len(column) - i
    return sum


def sum_grid(grid: List[List[str]]) -> int:
    sum = 0
    for c in range(len(grid[0])):
        column = []
        for r in grid:
            column.append(r[c])
        column_sum = sum_column(column)
        sum += column_sum
    return sum


def process_column(column: List[str]) -> None:
    next_space = len(column) - 1
    for i in range(len(column) - 1, -1, -1):
        c = column[i]
        if c == "#":
            next_space = i - 1
        elif c == "O":
            column[next_space] = column[i]
            if i != next_space:
                column[i] = "."
            next_space -= 1


def display_grid(grid: List[List[str]]) -> None:
    for row in grid:
        print(row)


def rotate(grid: List[List[str]]) -> List[List[str]]:
    new_grid = []
    for col in range(len(grid[0])):
        new_row = []
        for row in range(len(grid) - 1, -1, -1):
            new_row.append(grid[row][col])
        new_grid.append(new_row)
    return new_grid


def do_cycle(grid: List[List[str]]) -> List[List[str]]:
    grid = rotate(grid)
    for direction in range(4):
        for row in grid:
            process_column(row)
        grid = rotate(grid)
    for _ in range(3):
        grid = rotate(grid)
    return grid


def sum_cycle(cycles: int, grid: List[List[str]]) -> None:
    for cycle in range(1, cycles + 1):
        grid = do_cycle(grid)
        sum = 0
        for c in range(len(grid[0])):
            column = []
            for r in grid:
                column.append(r[c])
            column_sum = sum_column(column)
            sum += column_sum
        print(f"{cycle=}, {sum=}")


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
    grid = [[c for c in line] for line in lines]

    grid_width = len(lines[0])

    sum = 0
    for c in range(grid_width):
        column = []
        for r in lines:
            column.append(r[c])
        print(f"{column=}")
        column_sum = sum_column(column)
        print(f"{column_sum=}")
        sum += column_sum
    print(f"Sum: {sum}")
    print(f"Sum2: {sum_grid(grid)}")

    display_grid(grid)

    states = {}

    for cycle in range(1, 1000 + 1):
        grid = do_cycle(grid)
        print(f"Cycle {cycle}")
        display_grid(grid)
        print(f"{sum_grid(grid)=}")
        grid_str = "".join(["".join([c for c in line]) for line in grid])
        if states.get(grid_str) is None:
            states[grid_str] = [cycle]
        else:
            states[grid_str].append(cycle)

    periods = set()
    for grid_str, occurrences in states.items():
        large_occurrences = [n for n in occurrences if n > 900]
        if len(large_occurrences) > 2:
            periods.add(large_occurrences[-1] - large_occurrences[-2])
    if len(periods) != 1:
        raise ValueError(f"{periods=}")
    period = periods.pop()

    congruent_cycle = 1000000000 % period
    while congruent_cycle < 1000:
        congruent_cycle += period
    print(f"{congruent_cycle=}")

    grid = [[c for c in line] for line in lines]
    for cycle in range(1, congruent_cycle + 1):
        grid = do_cycle(grid)
    sum = sum_grid(grid)

    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
