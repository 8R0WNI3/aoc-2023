#!/usr/bin/env python3

import dataclasses

import util


@dataclasses.dataclass(frozen=True)
class Seed:
    starts_from: int
    range: int


def numbers_from_str_list(
    numbers: str,
) -> list[int]:
    return [int(number) for number in numbers.split(' ') if number.isdigit()]


def main(part: int):
    seeds = []
    maps = []

    for line in util.iter_input():
        if line.startswith('seeds'):
            _, seeds = line.split(':')
            seeds = numbers_from_str_list(numbers=seeds)
            if part == 2:
                seeds_iterator = iter(seeds)
                seeds = []
                for seed in seeds_iterator:
                    seed_len = next(seeds_iterator)
                    seeds.append(Seed(starts_from=seed, range=seed_len))
        elif not line:
            continue
        elif line.endswith('map:'):
            maps.append([])
        else:
            maps[len(maps) - 1].append(numbers_from_str_list(numbers=line))

    if part == 1:
        current = seeds
        for map in maps:
            last = current
            current = []

            for last_number in last:
                for mapping in map:
                    dest_start, src_start, range_len = mapping
                    if last_number in range(src_start, src_start + range_len):
                        current.append(last_number + (dest_start - src_start))
                        break
                else:
                    current.append(last_number)
        location = min(current)
    elif part == 2:
        maps.reverse()
        location = min([mapping[0] for mapping in maps[0]])
        while True:
            current = location
            for map in maps:
                for mapping in map:
                    dest_start, src_start, range_len = mapping
                    if current in range(dest_start, dest_start + range_len):
                        current -= dest_start - src_start
                        break

            found = False
            for seed in seeds:
                if current in range(seed.starts_from, seed.starts_from + seed.range):
                    found = True
                    break

            if found:
                break

            location += 1

    print(f'{part}) the lowest location is {location}')


if __name__ == '__main__':
    main(part=1)
    main(part=2)
