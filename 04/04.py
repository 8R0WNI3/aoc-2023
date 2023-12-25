#!/usr/bin/env python3

import util


def numbers_from_str_list(
    numbers: str,
) -> list[int]:
    return [int(number) for number in numbers.split(' ') if number.isdigit()]


def part_1():
    points_sum = 0

    for line in util.iter_input():
        points_card = 0
        _, numbers = line.split(':')
        winning_numbers, own_numbers = numbers.split('|')

        winning_numbers = numbers_from_str_list(numbers=winning_numbers)
        own_numbers = numbers_from_str_list(numbers=own_numbers)

        for own_number in own_numbers:
            if own_number in winning_numbers:
                if points_card == 0:
                    points_card = 1
                else:
                    points_card *= 2

        points_sum += points_card

    print(f'1) the cards are {points_sum} worth in total')


def part_2():
    numbers_cards = dict()

    for idx, line in enumerate(util.iter_input()):
        if idx not in numbers_cards:
            numbers_cards[idx] = 1
        else:
            numbers_cards[idx] += 1

        _, numbers = line.split(':')
        winning_numbers, own_numbers = numbers.split('|')

        winning_numbers = numbers_from_str_list(numbers=winning_numbers)
        own_numbers = numbers_from_str_list(numbers=own_numbers)

        numbers_matches = 0
        for own_number in own_numbers:
            if own_number in winning_numbers:
                numbers_matches += 1

        for copy_idx in range(idx + 1, idx + numbers_matches + 1):
            if copy_idx not in numbers_cards:
                numbers_cards[copy_idx] = numbers_cards[idx]
            else:
                numbers_cards[copy_idx] += numbers_cards[idx]

    number_cards = 0
    for numbers_card in numbers_cards.values():
        number_cards += numbers_card

    print(f'2) there are {number_cards} scratchcards in the end')


if __name__ == '__main__':
    part_1()
    part_2()
