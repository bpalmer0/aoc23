from dataclasses import dataclass
from typing import List, Dict


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

    def num_correct(self) -> int:
        correct_numbers = [num for num in self.numbers if num in self.winnning_numbers]
        return len(correct_numbers)

    def points(self) -> int:
        num_correct = self.num_correct()
        if num_correct == 0:
            return 0
        else:
            return 2 ** (num_correct - 1)


def play_game(cards: List[Card]) -> int:
    num_cards: Dict[int, int] = {card.id: 1 for card in cards}
    for card in cards:
        num_copies = num_cards[card.id]
        print(f"{num_copies} of card {card.id}")
        new_card_ids = range(card.id + 1, card.id + card.num_correct() + 1)
        print(f"Got new cards: {list(new_card_ids)}")
        for new_card_id in new_card_ids:
            num_cards[new_card_id] += num_copies
    total_cards = sum(num_cards.values())
    return total_cards


def main() -> None:
    with open("input") as f:
        lines = f.readlines()

    # part 1
    cards = [Card.from_str(card_str.strip()) for card_str in lines]
    points = [card.points() for card in cards]
    for card, value in zip(cards, points):
        print(f"Card {card.id}: {str(value)}")
    total = sum(list(points))
    print(f"Total: {total}")

    # part 2
    print("Playing game")
    total_cards = play_game(cards)
    print(f"Game resulted in a final total of {total_cards} scratchcards")


if __name__ == "__main__":
    main()
