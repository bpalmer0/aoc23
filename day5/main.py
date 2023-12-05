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

    def unmap(self, destination: int) -> int:
        source = -1
        for r in self.ranges:
            if destination in range(r.destination, r.destination + r.length):
                source = destination - r.destination + r.source
        if source == -1:
            return destination
        else:
            return source

    def interesting_numbers(self, later_map: "Map", destination_numbers: List[int]):
        interesting_numbers = []
        for r in self.ranges:
            interesting_numbers += [r.source, r.source + r.length]
        for r in later_map.ranges:
            interesting_numbers += [
                self.unmap(r.source),
                self.unmap(r.source + r.length),
            ]
        for number in destination_numbers:
            interesting_numbers.append(self.unmap(number))
        return interesting_numbers


if __name__ == "__main__":
    # part 1
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

    def func(s):
        source = s
        for map in maps:
            source = map.map(source)
        return source

    # part 2
    print("\n\nPart 2")
    locations_map = maps[-1]
    interesting_numbers = []
    for i in range(len(maps) - 2, -1, -1):
        print(f"Converting map {i + 1} to map {i}")
        print(f"{interesting_numbers=}")
        interesting_numbers = maps[i].interesting_numbers(
            maps[i + 1], interesting_numbers
        )
        interesting_numbers = sorted(list(set(interesting_numbers)))
    print(f"Interesting numbers {interesting_numbers}")
    part2_seeds = []
    part2_locations = []

    for i in range(0, len(seeds), 2):
        a = seeds[i]
        b = seeds[i] + seeds[i + 1]
        print(f"({a}, {b})")
        for num in interesting_numbers:
            if num in range(a, b):
                print(f"Interesting seed {num}")
                source = num
                for map in maps:
                    source = map.map(source)
                part2_locations.append(source)
    print(f"Locations: {part2_locations}")
    print(f"Minimum location: {min(part2_locations)}")
