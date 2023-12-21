#!/usr/bin/env python3

import util


def main():
    input = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    game_ids_sum = 0
    for line in util.iter_input():
        game_is_possible = True
        game, information = line.split(': ')
        subsets = information.split('; ')
        for subset in subsets:
            cubes = subset.split(', ')
            for cube in cubes:
                number, color = cube.split(' ')
                if int(number) > input[color]:
                    game_is_possible = False
        if game_is_possible:
            game_ids_sum += int(game.split(' ')[1])

    print(f'1) the sum of the IDs of valid games is {game_ids_sum}')

    power_of_sets_sum = 0
    for line in util.iter_input():
        minimal_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        game, information = line.split(': ')
        subsets = information.split('; ')
        for subset in subsets:
            cubes = subset.split(', ')
            for cube in cubes:
                number, color = cube.split(' ')
                if int(number) > minimal_cubes[color]:
                    minimal_cubes[color] = int(number)
        power_of_set = 1
        for number in minimal_cubes.values():
            power_of_set *= number
        power_of_sets_sum += power_of_set

    print(f'2) the sum of the power of the minimal sets is {power_of_sets_sum}')


if __name__ == '__main__':
    main()
