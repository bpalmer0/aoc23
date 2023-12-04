from dataclasses import dataclass
from typing import List


@dataclass
class Card:
    id: int
    winnning_numbers: List[int]
    numbers: List[int]

    @classmethod
    def from_str(cls, card_str: str) -> "Card":
        split = card_str.split(":")
        before_colon = split[0]
        after_colon = split[1]

        id_split = before_colon.split(" ")
        id = int(id_split[-1])

        numbers_split = after_colon.split("|")
        winning_str = numbers_split[0]
        numbers_str = numbers_split[1]

        winning_numbers = [int(num) for num in winning_str.split(" ") if num != ""]
        numbers = [int(num) for num in numbers_str.split(" ") if num != ""]

        return Card(id, winning_numbers, numbers)

    def points(self) -> int:
        correct_numbers = [num for num in self.numbers if num in self.winnning_numbers]
        num_correct = len(correct_numbers)
        if num_correct == 0:
            return 0
        else:
            return 2 ** (num_correct - 1)


def main() -> None:
    with open("input") as f:
        lines = f.readlines()

    cards = [Card.from_str(card_str.strip()) for card_str in lines]
    points = [card.points() for card in cards]
    for card, value in zip(cards, points):
        print(f"Card {card.id}: {str(value)}")
    total = sum(list(points))
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
