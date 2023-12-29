#!/usr/bin/env python3

import dataclasses

import util


@dataclasses.dataclass(frozen=True)
class Race:
    time: int
    distance: int


def numbers_from_str_list(
    numbers: str,
) -> list[int]:
    return [int(number) for number in numbers.split(' ') if number.isdigit()]


def main(part: int):
    times = []
    distances = []

    for line in util.iter_input():
        if line.startswith('Time'):
            times = numbers_from_str_list(numbers=line.split(':')[1])
            if part == 2:
                times = [int(''.join([str(time) for time in times]))]
        elif line.startswith('Distance'):
            distances = numbers_from_str_list(numbers=line.split(':')[1])
            if part == 2:
                distances = [int(''.join([str(distance) for distance in distances]))]

    races: list[Race] = []
    for idx, _ in enumerate(times):
        races.append(Race(
            time=times[idx],
            distance=distances[idx],
        ))

    product = 1
    for race in races:
        number_wins = 0
        for speed in range(1, race.time):
            distance = speed * (race.time - speed)
            if distance > race.distance:
                number_wins += 1
        product *= number_wins

    print(f'{part}) the product of numbers of ways to win is {product}')


if __name__ == '__main__':
    main(part=1)
    main(part=2)
