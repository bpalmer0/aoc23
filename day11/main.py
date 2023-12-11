from itertools import combinations
from typing import List


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
    galaxies = []
    grid_height = len(lines)
    grid_width = len(lines[0])
    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if char == "#":
                galaxies.append((c, r))
    print(galaxies)

    galaxy_rows = [galaxy[1] for galaxy in galaxies]
    empty_rows = [r for r in range(grid_height) if r not in galaxy_rows]
    empty_rows.sort(reverse=True)

    empty_space_distance = 1000000

    for empty_row in empty_rows:
        new_galaxies = []
        for c, r in galaxies:
            if r > empty_row:
                new_galaxies.append((c, r + empty_space_distance - 1))
            else:
                new_galaxies.append((c, r))
        galaxies = new_galaxies

    galaxy_columns = [galaxy[0] for galaxy in galaxies]
    empty_columns = [c for c in range(grid_height) if c not in galaxy_columns]
    empty_columns.sort(reverse=True)

    for empty_column in empty_columns:
        new_galaxies = []
        for c, r in galaxies:
            if c > empty_column:
                new_galaxies.append((c + empty_space_distance - 1, r))
            else:
                new_galaxies.append((c, r))
        galaxies = new_galaxies

    print(len(list(combinations(galaxies, 2))))
    sum = 0
    for g1, g2 in combinations(galaxies, 2):
        x_diff = abs(g1[0] - g2[0])
        y_diff = abs(g1[1] - g2[1])
        sum += x_diff + y_diff
    print(f"Sum of all shortest paths between all pairs of galaxies: {sum}")


if __name__ == "__main__":
    main()
