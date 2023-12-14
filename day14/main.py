from typing import List


def process_column(column: List[str]) -> int:
    height = len(column)
    next_space = 0
    sum = 0
    for i, c in enumerate(column):
        if c == "#":
            next_space = i + 1
        elif c == "O":
            next_space += 1
            sum += height - next_space + 1
    return sum


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
    grid_width = len(lines[0])

    sum = 0
    for c in range(grid_width):
        column = []
        for r in lines:
            column.append(r[c])
        print(f"{column=}")
        column_sum = process_column(column)
        print(f"{column_sum=}")
        sum += column_sum
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
