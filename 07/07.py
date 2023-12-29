#!/usr/bin/env python3

import dataclasses
import enum

import util


class Types(enum.IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


@dataclasses.dataclass(frozen=True)
class Hand:
    cards: str
    bid: int


def type_of_hand(hand: Hand, part: int) -> Types:
    label_counts = dict()

    for label in hand.cards:
        if label not in label_counts:
            label_counts[label] = 1
        else:
            label_counts[label] += 1

    joker_count = 0
    if part == 2 and 'J' in label_counts:
        joker_count = label_counts['J']
        del label_counts['J']
        if not label_counts:
            label_counts['A'] = 0

    label_counts_sorted = sorted(label_counts.values(), reverse=True)
    label_counts_sorted[0] += joker_count
    if label_counts_sorted[0] == 5:
        return Types.FIVE_OF_A_KIND
    if label_counts_sorted[0] == 4:
        return Types.FOUR_OF_A_KIND
    if label_counts_sorted[0] == 3 and label_counts_sorted[1] == 2:
        return Types.FULL_HOUSE
    if label_counts_sorted[0] == 3:
        return Types.THREE_OF_A_KIND
    if label_counts_sorted[1] == 2:
        return Types.TWO_PAIR
    if label_counts_sorted[0] == 2:
        return Types.ONE_PAIR
    return Types.HIGH_CARD


def strength_of_hand(hand: Hand, part: int) -> int:
    value = 0

    strength_of_pos = 1
    for label in hand.cards:
        strength_of_pos /= 100
        if label.isdigit():
            value += int(label) * strength_of_pos
        elif label == 'A':
            value += 14 * strength_of_pos
        elif label == 'K':
            value += 13 * strength_of_pos
        elif label == 'Q':
            value += 12 * strength_of_pos
        elif label == 'J':
            if part == 1:
                value += 11 * strength_of_pos
            elif part == 2:
                value += 1 * strength_of_pos
        elif label == 'T':
            value += 10 * strength_of_pos

    return value


def main(part: int):
    hands = [
        Hand(
            cards=hand.split(' ')[0],
            bid=int(hand.split(' ')[1]),
        )
        for hand in util.iter_input()
    ]

    sorted_hands = sorted(
        hands,
        key=lambda hand: (
            type_of_hand(hand=hand, part=part),
            strength_of_hand(hand=hand, part=part),
        ),
    )

    total_winnings = 0
    for idx, hand in enumerate(sorted_hands):
        total_winnings += hand.bid * (idx + 1)

    print(f'{part}) the total winnings are {total_winnings}')


if __name__ == '__main__':
    main(part=1)
    main(part=2)
