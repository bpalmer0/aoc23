from dataclasses import dataclass
from typing import List
from math import prod


@dataclass
class Race:
    time: int
    record: int

    def is_win(self, hold_time: int) -> bool:
        distance = (self.time - hold_time) * hold_time
        return distance > self.record

    def winning_hold_times(self) -> List[int]:
        return [h for h in range(self.time) if self.is_win(h)]


def main():
    with open("input") as f:
        lines = f.read().split("\n")
    times = [int(time) for time in lines[0].split(" ")[1:] if time != ""]
    distances = [
        int(distance) for distance in lines[1].split(" ")[1:] if distance != ""
    ]
    races = [Race(time, distance) for (time, distance) in zip(times, distances)]
    ways_to_win = [len(race.winning_hold_times()) for race in races]
    print(f"{ways_to_win=}")
    print(f"product: {prod(ways_to_win)}")


if __name__ == "__main__":
    main()
