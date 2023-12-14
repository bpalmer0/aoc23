from typing import List


def process_pattern(pattern: List[str]) -> int:
    print(f"{pattern=}")
    row_values = []
    for row in pattern:
        value = 0
        for i, char in enumerate(reversed(row)):
            if char == "#":
                value += 2**i
        row_values.append(value)
    max_row = len(row_values) - 1
    mirror_ind = []
    for i in range(max_row):
        mirror = True
        smudge_fixed = False
        for d in range(len(row_values)):
            j1 = i + d + 1
            j2 = i - d
            if j1 > max_row or j2 < 0:
                break
            v1 = row_values[j1]
            v2 = row_values[j2]
            if v1 != v2:
                # smudge if numbers differ by a power of two - bitwise 'xor' results in exactly one 1 in the bitstring
                print(f"{v1=}, {v2=}, {(v1 ^ v2)=}")
                if not smudge_fixed and "{0:b}".format(v1 ^ v2).count("1") == 1:
                    print(f"Smudge used on index {j1} or {j2} ({v1} vs {v2})")
                    smudge_fixed = True
                    continue
                # even fixing a smudge won't make these rows equal
                else:
                    mirror = False
                    break
        # only count the mirror where smudge was fixed
        if mirror and smudge_fixed:
            mirror_ind.append(i)
    print(f"{mirror_ind=}")
    print(f"{row_values=}")
    rows_above_mirror = 0
    for i in mirror_ind:
        rows_above_mirror += i + 1
    return rows_above_mirror


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
        lines.append("")

    pattern_rows = []
    sum = 0
    num_pattern = 0
    for line in lines:
        if line == "":
            print(f"\n\n{num_pattern=}")
            pattern_columns = []
            for c in range(len(pattern_rows[0])):
                column = ""
                for row in pattern_rows:
                    column += row[c]
                pattern_columns.append(column)
            print(f"Rows")
            row_summary = process_pattern(pattern_rows)
            print(f"Columns")
            column_summary = process_pattern(pattern_columns)
            print(f"Pattern {num_pattern}: {row_summary}, {column_summary}")
            sum += column_summary + 100 * row_summary
            pattern_rows = []
            num_pattern += 1
        else:
            pattern_rows.append(line)
    print(f"Summary total: {sum}")


if __name__ == "__main__":
    main()
