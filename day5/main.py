from typing import List
from dataclasses import dataclass


@dataclass
class Range:
    destination: int
    source: int
    length: int

    @classmethod
    def from_str(cls, range_str: str) -> "Range":
        num_strs = [
            int(num.strip()) for num in range_str.split(" ") if num.strip() != ""
        ]
        destination, source, length = tuple(num_strs)
        return cls(destination, source, length)


@dataclass
class Map:
    ranges: List[Range]

    @classmethod
    def from_str(cls, lines: List[str]) -> "Map":
        range_strs = lines[1:]
        ranges = [
            Range.from_str(range_str) for range_str in range_strs if range_str != ""
        ]
        return cls(ranges)

    def map(self, source: int) -> int:
        destination = -1
        for r in self.ranges:
            if source in range(r.source, r.source + r.length):
                destination = source - r.source + r.destination
        if destination == -1:
            return source
        else:
            return destination


if __name__ == "__main__":
    with open("input") as f:
        input = f.read()
    split = input.split("\n\n")
    seed_str = split[0]
    map_strs = split[1:]
    maps = [Map.from_str(map_str.split("\n")) for map_str in map_strs]

    seeds = [int(seed) for seed in seed_str.split(": ")[1].split(" ")]
    locations = []
    for seed in seeds:
        source = seed
        for map in maps:
            source = map.map(source)
        locations.append(source)
    print(f"Seeds: {seeds}")
    print(f"Locations: {locations}")
    print(f"Minimum location: {min(locations)}")
