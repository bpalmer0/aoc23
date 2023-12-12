from typing import List
from itertools import combinations


def is_valid(record: str, groups: List[int]) -> bool:
    spring_groups = [group for group in record.split(".") if group != ""]
    if len(spring_groups) != len(groups):
        return False
    for spring_group, group in zip(spring_groups, groups):
        if len(spring_group) != group:
            return False
    return True


def get_num_valid(record: str, groups: List[int]) -> int:
    print(f"{record=}, {groups=}")
    num_valid = 0
    unknown_ind = [i for i, char in enumerate(record) if char == "?"]
    combos = []
    for i in range(len(unknown_ind) + 1):
        combos += list(combinations(unknown_ind, i))
    for combo in combos:
        test_record = record
        for broken_index in combo:
            test_record = (
                test_record[:broken_index] + "#" + test_record[broken_index + 1 :]
            )
        test_record = test_record.replace("?", ".")
        if is_valid(test_record, groups):
            num_valid += 1
            # print(f"Test record {test_record} is valid")
        else:
            pass
            # print(f"Test record {test_record} is not valid")
    print(f"{num_valid=}")
    return num_valid


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")

    sum = 0
    for line in lines:
        record, groups = line.split(" ")
        groups = [int(g) for g in groups.split(",")]
        num_valid = get_num_valid(record, groups)
        sum += num_valid
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
