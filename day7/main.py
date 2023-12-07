from dataclasses import dataclass
from enum import IntEnum, auto
from typing import List
from functools import total_ordering


class Card(IntEnum):
    cJ = auto()
    c2 = auto()
    c3 = auto()
    c4 = auto()
    c5 = auto()
    c6 = auto()
    c7 = auto()
    c8 = auto()
    c9 = auto()
    cT = auto()
    cQ = auto()
    cK = auto()
    cA = auto()

    @classmethod
    def from_str(cls, card_str: str) -> "Card":
        attr = f"c{card_str}"
        return cls(getattr(cls, attr).value)

    def __repr__(self) -> str:
        return self._name_.removeprefix("c")


class HandType(IntEnum):
    HighCard = auto()
    OnePair = auto()
    TwoPair = auto()
    ThreeKind = auto()
    FullHouse = auto()
    FourKind = auto()
    FiveKind = auto()


@total_ordering
@dataclass
class Hand:
    cards: List[Card]
    bid: int

    @classmethod
    def from_str(cls, hand_str: str) -> "Hand":
        cards, bid = hand_str.split(" ")
        cards = [Card.from_str(card) for card in cards]
        bid = int(bid)
        return cls(cards, bid)

    def get_type(self) -> HandType:
        card_counts = {card: 0 for card in Card}
        for card in self.cards:
            card_counts[card] += 1

        # try making jokers each type of card and take the strongest type made
        # it's never worth it to make jokers different cards
        num_jokers = card_counts[Card.cJ]
        card_counts[Card.cJ] = 0
        best_type = HandType.HighCard
        for card in Card:
            card_counts[card] += num_jokers

            if 5 in card_counts.values():
                type = HandType.FiveKind
            elif 4 in card_counts.values():
                type = HandType.FourKind
            elif 3 in card_counts.values() and 2 in card_counts.values():
                type = HandType.FullHouse
            elif 3 in card_counts.values():
                type = HandType.ThreeKind
            elif list(card_counts.values()).count(2) == 2:
                type = HandType.TwoPair
            elif 2 in card_counts.values():
                type = HandType.OnePair
            else:
                type = HandType.HighCard

            if type > best_type:
                best_type = type

            card_counts[card] -= num_jokers

        return best_type

    def __eq__(self, other: "Hand") -> bool:
        return self.cards == other.cards

    def __lt__(self, other: "Hand") -> bool:
        this_type = self.get_type()
        other_type = other.get_type()
        if this_type < other_type:
            return True
        elif this_type > other_type:
            return False

        for this_card, other_card in zip(self.cards, other.cards):
            if this_card < other_card:
                return True
            elif this_card > other_card:
                return False
        return False


def main() -> None:
    with open("input") as f:
        lines = f.read().split("\n")
    hands = [Hand.from_str(hand_str) for hand_str in lines if hand_str != ""]
    sorted_hands = sorted(hands)
    total = 0
    for i, hand in enumerate(sorted_hands):
        rank = i + 1
        winnings = rank * hand.bid
        total += winnings
        print(f"Winnings for hand {hand}: {winnings}")
    print(f"Total winnings: {total}")


if __name__ == "__main__":
    main()
