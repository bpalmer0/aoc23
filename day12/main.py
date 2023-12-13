from typing import Tuple
from itertools import combinations
from functools import cache
from math import comb


def partitions(n, k):
    for c in combinations(range(n + k - 1), k - 1):
        yield [b - a - 1 for a, b in zip((-1,) + c, c + (n + k - 1,))]


@cache
def is_valid(record: str, groups: Tuple[int, ...]) -> bool:
    spring_groups = [group for group in record.split(".") if group != ""]
    if len(spring_groups) != len(groups):
        return False
    for spring_group, group in zip(spring_groups, groups):
        if len(spring_group) != group:
            return False
    return True


@cache
def get_num_valid_combo(record: str, groups: Tuple[int, ...]) -> int:
    unknown_ind = [i for i, char in enumerate(record) if char == "?"]
    combos = []
    num_valid = 0
    for i in range(len(unknown_ind) + 1):
        combos = combinations(unknown_ind, i)
        for combo in combos:
            test_record = record
            for broken_index in combo:
                test_record = (
                    test_record[:broken_index] + "#" + test_record[broken_index + 1 :]
                )
            test_record = test_record.replace("?", ".")
            if is_valid(test_record, groups):
                num_valid += 1
            else:
                pass
    return num_valid


@cache
def get_num_valid_old(record: str, groups: Tuple[int, ...]) -> int:
    if len(groups) != 0:
        # sanity checks
        if len(record) < max(groups) or len(record) < sum(groups) + len(groups) - 1:
            return 0
        if record.find((max(groups) + 1) * "#") != -1:
            return 0
    if "#" not in record and "." not in record and len(groups) != 0:
        n = sum(groups) + len(groups) - 1
        bars = len(groups)
        stars = len(record) - n + 1
        if stars == 0:
            return 1
        ans = comb(bars + stars - 1, stars - 1)
        return ans

    num_valid = 0
    boundaries = []
    if len(record) > 4:
        for i in range(0, len(record) - 1):
            if record[i : i + 2] == "?#":
                boundaries.append(i)
            elif record[i : i + 2] == "#?":
                boundaries.append(i + 1)
    if len(record) > 4 and len(boundaries) > 0:
        if len(boundaries) > 0:
            q = boundaries[len(boundaries) // 2]
            test_record = record
            broken_record = test_record[:q] + "#" + test_record[q + 1 :]
            fixed_record = test_record[:q] + "." + test_record[q + 1 :]
            broken_record = [r for r in broken_record.split(".") if r != ""]
            fixed_record = [r for r in fixed_record.split(".") if r != ""]
            num_valid += get_num_valid(tuple(broken_record), groups) + get_num_valid(
                tuple(fixed_record), groups
            )
            return num_valid
    return get_num_valid_combo(record, groups)


@cache
def get_num_valid(record: Tuple[str, ...], groups: Tuple[int, ...]) -> int:
    if len(record) == 1:
        return get_num_valid_old(record[0], groups)
    num_valid = 0
    for num_groups in range(len(groups) + 1):
        matches = get_num_valid_old(record[0], groups[:num_groups])

        remaining_record = record[1:]
        remaining_groups = groups[num_groups:]
        remaining = get_num_valid(remaining_record, remaining_groups)
        num_valid += matches * remaining
    return num_valid


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")

    sum = 0
    for line in lines:
        record, groups = line.split(" ")
        groups = [int(g) for g in groups.split(",")]

        # part 2
        record = "?".join([record] * 5)
        record = [r for r in record.split(".") if r != ""]
        groups = groups * 5

        print(f"{record=}")
        num_valid = get_num_valid(tuple(record), tuple(groups))
        print(f"{num_valid=}")
        sum += num_valid
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
