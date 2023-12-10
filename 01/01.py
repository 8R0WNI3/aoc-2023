#!/usr/bin/env python3

import util


name_to_digit = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def digit_from_name(s: str) -> int | None:
    for name, digit in name_to_digit.items():
        if s.lower().startswith(name):
            return digit


def main(part: int):
    calibration_value_sum = 0
    for line in util.iter_input():
        digits = []
        for idx, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            elif part == 2:
                if digit := digit_from_name(line[idx:]):
                    digits.append(digit)

        calibration_value_sum += int(f'{digits[0]}{digits[-1]}')

    print(f'{part}) the sum of all calibration values is {calibration_value_sum}')


if __name__ == '__main__':
    main(part=1)
    main(part=2)
