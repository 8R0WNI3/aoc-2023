#!/usr/bin/env python3

import util


def get_row(
    space: dict[(int, int), str],
    row: int,
) -> dict[(int, int), str]:
    return dict([
        space_tile for space_tile in space.items()
        if space_tile[0][1] == row
    ])


def get_column(
    space: dict[(int, int), str],
    column: int,
) -> dict[(int, int), str]:
    return dict([
        space_tile for space_tile in space.items()
        if space_tile[0][0] == column
    ])


def main(part: int):
    space: dict[(int, int), str] = dict()
    galaxies: dict[(int, int), str] = dict()

    for y_pos, line in enumerate(util.iter_input()):
        for x_pos, space_tile in enumerate(line):
            space[(x_pos, y_pos)] = space_tile
            if space_tile == '#':
                galaxies[(x_pos, y_pos)] = space_tile


    seen_galaxies = set()
    row_weight: dict[int, int] = dict()
    column_weight: dict[int, int] = dict()
    lengths_sum = 0

    for galaxy_from in galaxies:
        seen_galaxies.add(galaxy_from)
        for galaxy_to in galaxies:
            if galaxy_to in seen_galaxies:
                continue

            if part == 1:
                expansion = 1
            elif part == 2:
                expansion = 999999

            extra_steps = 0
            for row in range(
                min(galaxy_from[1], galaxy_to[1]),
                max(galaxy_from[1], galaxy_to[1]),
            ):
                if row not in row_weight:
                    if '#' in get_row(space=space, row=row).values():
                        row_weight[row] = 0
                    else:
                        row_weight[row] = expansion
                extra_steps += row_weight[row]
            for column in range(
                min(galaxy_from[0], galaxy_to[0]),
                max(galaxy_from[0], galaxy_to[0]),
            ):
                if column not in column_weight:
                    if '#' in get_column(space=space, column=column).values():
                        column_weight[column] = 0
                    else:
                        column_weight[column] = expansion
                extra_steps += column_weight[column]

            lengths_sum += abs(galaxy_from[0] - galaxy_to[0])
            lengths_sum += abs(galaxy_from[1] - galaxy_to[1])
            lengths_sum += extra_steps

    print(f'{part}) the sum of all lengths {lengths_sum}')


if __name__ == '__main__':
    main(part=1)
    main(part=2)
