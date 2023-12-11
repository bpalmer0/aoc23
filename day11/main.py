from itertools import combinations
from typing import List


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
    grid = []
    for line in lines:
        grid.append([c for c in line])

    empty_cols: List[int] = []
    for col in range(len(grid[0])):
        column = [row[col] for row in grid]
        if "#" not in column:
            empty_cols.append(col)
    empty_cols = sorted(empty_cols, reverse=True)
    print(f"empty cols: {empty_cols}")
    for col in empty_cols:
        for row in grid:
            row.insert(col, ".")
    grid_width = len(grid[0])

    empty_rows = []
    for r, row in enumerate(grid):
        if "#" not in row:
            empty_rows.append(r)
    empty_rows = sorted(empty_rows, reverse=True)
    print(f"empty rows: {empty_rows}")
    for empty_row in empty_rows:
        grid.insert(empty_row, grid_width * ["."])

    for row in grid:
        print(row)

    galaxies = []
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "#":
                galaxies.append((c, r))
    print(f"Found {len(galaxies)} galaxies")

    sum = 0
    print(len(list(combinations(galaxies, 2))))
    for g1, g2 in combinations(galaxies, 2):
        sum += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    print(f"Sum of all shortest paths between all pairs of galaxies: {sum}")


if __name__ == "__main__":
    main()
