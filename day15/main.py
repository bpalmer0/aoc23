from typing import Tuple, Optional


def get_hash(s: str) -> int:
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    print(f"Hashing {s}: {val}")
    return val


def get_focal_length(s: str) -> Optional[int]:
    split = s.split("=")
    if len(split) == 1:
        return None
    else:
        _, focal_length = split
        focal_length = int(focal_length)
        return focal_length


def main():
    with open("input") as f:
        text = f.read().strip().replace("\n", "")

    print(f"Part 1")
    strings = text.split(",")
    sum = 0
    for string in strings:
        sum += get_hash(string)
    print(f"Sum: {sum}")

    print(f"\nPart 2")
    boxes = [[] for _ in range(256)]
    for string in strings:
        print(f"\nAfter {string}")
        focal_length = get_focal_length(string)
        if focal_length is not None:
            label, _ = string.split("=")
            box = boxes[get_hash(label) % 256]
            same_label = -1
            for i, lens in enumerate(box):
                if label == lens[0]:
                    same_label = i
            if same_label != -1:
                box[same_label] = (label, focal_length)
            else:
                box.append((label, focal_length))
        else:
            label = string.removesuffix("-")
            box = boxes[get_hash(label) % 256]
            for i, lens in enumerate(box):
                if label == lens[0]:
                    box.remove(lens)
                    break
        # print(f"{label=}, {focal_length=}")
        for i, box in enumerate(boxes):
            if len(box) > 0:
                print(f"Box {i}: {box}")

    sum = 0
    for box_num, box in enumerate(boxes):
        for i, lens in enumerate(box):
            print(f"{box_num=}, {i=}, {lens[1]=}")
            sum += (box_num + 1) * (i + 1) * lens[1]
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
