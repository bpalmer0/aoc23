grid = []
number_grid = []
active_splitters = []


def display_grid() -> None:
    for number_row in number_grid:
        row = ""
        for num in number_row:
            if num > 0:
                row += "#"
            else:
                row += "."
        print(row)


def clear_grid() -> None:
    global active_splitters
    active_splitters = []
    for number_row in number_grid:
        for i in range(len(number_row)):
            number_row[i] = 0


def get_num_energized() -> int:
    num_energized = 0
    for number_row in number_grid:
        for num in number_row:
            if num > 0:
                num_energized += 1
    return num_energized


def beam(beam_x: int, beam_y: int, beam_vx: int, beam_vy: int) -> None:
    while True:
        beam_x += beam_vx
        beam_y += beam_vy
        if (
            beam_x > len(grid[0]) - 1
            or beam_x < 0
            or beam_y > len(grid) - 1
            or beam_y < 0
        ):
            break
        tile = grid[beam_y][beam_x]
        number_grid[beam_y][beam_x] += 1
        if tile == ".":
            continue
        elif tile == "\\":
            if beam_vx == 1 and beam_vy == 0:
                beam_vx = 0
                beam_vy = 1
            elif beam_vx == -1 and beam_vy == 0:
                beam_vx = 0
                beam_vy = -1
            elif beam_vx == 0 and beam_vy == 1:
                beam_vx = 1
                beam_vy = 0
            elif beam_vx == 0 and beam_vy == -1:
                beam_vx = -1
                beam_vy = 0
            else:
                raise ValueError(f"Invalid beam direction ({beam_vx}, {beam_vy})")
        elif tile == "/":
            if beam_vx == 1 and beam_vy == 0:
                beam_vx = 0
                beam_vy = -1
            elif beam_vx == -1 and beam_vy == 0:
                beam_vx = 0
                beam_vy = 1
            elif beam_vx == 0 and beam_vy == 1:
                beam_vx = -1
                beam_vy = 0
            elif beam_vx == 0 and beam_vy == -1:
                beam_vx = 1
                beam_vy = 0
            else:
                raise ValueError(f"Invalid beam direction ({beam_vx}, {beam_vy})")
        elif tile == "|":
            if beam_vy == 0:
                if (beam_x, beam_y) not in active_splitters:
                    active_splitters.append((beam_x, beam_y))
                    beam(beam_x, beam_y, 0, 1)
                    beam(beam_x, beam_y, 0, -1)
                break
        elif tile == "-":
            if beam_vx == 0:
                if (beam_x, beam_y) not in active_splitters:
                    active_splitters.append((beam_x, beam_y))
                    beam(beam_x, beam_y, -1, 0)
                    beam(beam_x, beam_y, 1, 0)
                break


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            row = []
            number_row = []
            for c in line:
                row.append(c)
                number_row.append(0)
            grid.append(row)
            number_grid.append(number_row)

        print("Part 1")
        beam(-1, 0, 1, 0)
        print(f"Number of energized tiles: {get_num_energized()}")
        clear_grid()
        beam(-1, 0, 1, 0)
        print(f"Number of energized tiles: {get_num_energized()}")

        print("Part 2")
        max_num_energized = 0
        for r in range(len(grid)):
            # enter from left
            clear_grid()
            beam(-1, r, 1, 0)
            energized = get_num_energized()
            print(f"{energized=}")
            max_num_energized = max(max_num_energized, get_num_energized())
            # enter from right
            clear_grid()
            beam(len(grid[0]), r, -1, 0)
            energized = get_num_energized()
            print(f"{energized=}")
            max_num_energized = max(max_num_energized, get_num_energized())
        for c in range(len(grid[0])):
            # enter from top
            clear_grid()
            beam(c, -1, 0, 1)
            energized = get_num_energized()
            print(f"{energized=}")
            max_num_energized = max(max_num_energized, get_num_energized())
            # enter from bottom
            clear_grid()
            beam(c, len(grid), 0, -1)
            energized = get_num_energized()
            print(f"{energized=}")
            max_num_energized = max(max_num_energized, get_num_energized())
        print(f"Max number of energized tiles: {max_num_energized}")


if __name__ == "__main__":
    main()
