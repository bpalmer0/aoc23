from typing import List

def get_calibration_value(line: str) -> int:
    digits = list(filter(lambda c: c.isdigit(), line))
    first = digits[0]
    last = digits[~0]
    return int(first + last)

def sum_calibration_values(document: List[str]):
    return sum(list(map(get_calibration_value, document)))

if __name__ == "__main__":
    with open("./input") as f:
        lines = f.readlines()
    sum = sum_calibration_values(lines)
    print(sum)
