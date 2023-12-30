#!/usr/bin/env python3

import util


def numbers_from_str_list(
    numbers: str,
) -> list[int]:
    return [int(number) for number in numbers.split(' ') if number.lstrip('-').isdigit()]


def main(part: int):
    extrapolated_values_sum = 0

    for line in util.iter_input():
        histories = [numbers_from_str_list(numbers=line)]

        while [value for value in histories[len(histories) - 1] if value != 0]:
            history = histories[len(histories) - 1]
            next_history = []
            for idx in range(1, len(history)):
                next_history.append(history[idx] - history[idx - 1])
            histories.append(next_history)

        extrapolated_value = 0
        for history in reversed(histories):
            if part == 1:
                extrapolated_value += history[len(history) - 1]
            elif part == 2:
                extrapolated_value = history[0] - extrapolated_value
        extrapolated_values_sum += extrapolated_value

    print(f'{part}) the sum of all extrapolated values is {extrapolated_values_sum}')


if __name__ == '__main__':
    main(part=1)
    main(part=2)
