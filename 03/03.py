#!/usr/bin/env python3

import collections
import collections.abc
import dataclasses

import util


@dataclasses.dataclass(frozen=True)
class Adjacent:
    x: int
    y: int
    character: str


@dataclasses.dataclass(frozen=True)
class Number:
    value: int
    adjacents: tuple[Adjacent]


def get_adjacents_of_number(
    number: str,
    lines: tuple[str],
    line_idx: int,
    char_idx: int,
) -> collections.abc.Generator[Adjacent, None, None]:
    for current_line_idx in range(
        max(0, line_idx - 1),
        min(len(lines), line_idx + 2),
    ):
        line = lines[current_line_idx]
        for current_char_idx in range(
            max(0, char_idx - len(number) - 1),
            min(len(line), char_idx + 1),
        ):
            char = line[current_char_idx]
            if not char.isdigit() and char != '.':
                yield Adjacent(x=current_char_idx, y=current_line_idx, character=char)


def main():
    lines = tuple(util.iter_input())

    numbers: list[Number] = []
    part_numbers_sum = 0
    number = ''
    for line_idx, line in enumerate(lines):
        for char_idx, char in enumerate(line):
            if char.isdigit():
                number += char
            if number and (not char.isdigit() or char_idx == len(line) - 1):
                adjacents = tuple(get_adjacents_of_number(
                    number=number,
                    lines=lines,
                    line_idx=line_idx,
                    char_idx=char_idx,
                ))
                if adjacents:
                    number = Number(value=int(number), adjacents=adjacents)
                    numbers.append(number)
                    part_numbers_sum += number.value
                number = ''

    print(f'1) the sum of all part numbers is {part_numbers_sum}')

    relevant_adjacents_with_numbers = collections.defaultdict(list)
    for number in numbers:
        for adjacent in number.adjacents:
            if adjacent.character != '*':
                continue
            relevant_adjacents_with_numbers[adjacent].append(number)

    gear_ratios_sum = 0
    for numbers in relevant_adjacents_with_numbers.values():
        if len(numbers) == 2:
            gear_ratios_sum += numbers[0].value * numbers[1].value

    print(f'2) the sum of all gear ratios is {gear_ratios_sum}')


if __name__ == '__main__':
    main()
