from main import Card, HandType, Hand
import pytest


@pytest.mark.parametrize(
    "hand_str,hand",
    [
        ("32T3K 765", Hand([Card.c3, Card.c2, Card.cT, Card.c3, Card.cK], 765)),
        ("KTJJT 220", Hand([Card.cK, Card.cT, Card.cJ, Card.cJ, Card.cT], 220)),
    ],
)
def test_hand_from_str(hand_str: str, hand: Hand) -> None:
    assert Hand.from_str(hand_str) == hand


@pytest.mark.parametrize(
    "hand,hand_type",
    [
        (Hand([Card.c3, Card.c2, Card.cT, Card.c3, Card.cK], 765), HandType.OnePair),
        (Hand([Card.cT, Card.c5, Card.c5, Card.cJ, Card.c5], 684), HandType.FourKind),
        (Hand([Card.cK, Card.cK, Card.c6, Card.c7, Card.c7], 28), HandType.TwoPair),
        (Hand([Card.cK, Card.cT, Card.cJ, Card.cJ, Card.cT], 220), HandType.FourKind),
        (Hand([Card.cQ, Card.cQ, Card.cQ, Card.cJ, Card.cA], 483), HandType.FourKind),
        (Hand([Card.cQ, Card.cQ, Card.cQ, Card.cA, Card.cA], 899), HandType.FullHouse),
        (Hand([Card.c4, Card.c4, Card.c4, Card.c4, Card.c4], 473), HandType.FiveKind),
        (Hand([Card.c2, Card.c3, Card.c4, Card.c5, Card.c6], 58), HandType.HighCard),
    ],
)
def test_hand_type(hand: Hand, hand_type: HandType) -> None:
    assert hand.get_type() == hand_type


@pytest.mark.parametrize(
    "hand1,hand2,expected",
    [
        (Hand([Card.cA] * 5, 25), Hand([Card.cA] * 5, 36), 0),
        (
            Hand([Card.cK, Card.cK, Card.c6, Card.c7, Card.c7], 28),
            Hand([Card.cK, Card.cT, Card.cJ, Card.cJ, Card.cT], 220),
            -1,
        ),
        (
            Hand([Card.cQ, Card.cQ, Card.cQ, Card.cJ, Card.cA], 483),
            Hand([Card.cQ, Card.cQ, Card.cQ, Card.cA, Card.cA], 292),
            1,
        ),
        (
            Hand([Card.cT, Card.c5, Card.c5, Card.cJ, Card.c5], 1),
            Hand([Card.cK, Card.cK, Card.c6, Card.c7, Card.c7], 28),
            1,
        ),
        (
            Hand([Card.cT, Card.c5, Card.c5, Card.cJ, Card.c5], 8),
            Hand([Card.c3, Card.c2, Card.cT, Card.c3, Card.cK], 9),
            1,
        ),
    ],
)
def test_hand_cmp(hand1: Hand, hand2: Hand, expected: int) -> None:
    if expected < 0:
        assert hand1 < hand2
    if expected == 0:
        assert hand1 == hand2
    if expected > 0:
        assert hand1 > hand2
