#!/usr/bin/env python3

import dataclasses
import math

import util


@dataclasses.dataclass
class Tile:
    tile: str
    x_pos: int
    y_pos: int
    north: str=None
    east: str=None
    south: str=None
    west: str=None

    def has_connection_to_north(self) -> bool:
        return self.tile in ('|', 'L', 'J') or self.tile == 'S'

    def has_connection_to_east(self) -> bool:
        return self.tile in ('-', 'L', 'F') or self.tile == 'S'

    def has_connection_to_south(self) -> bool:
        return self.tile in ('|', '7', 'F') or self.tile == 'S'

    def has_connection_to_west(self) -> bool:
        return self.tile in ('-', 'J', '7') or self.tile == 'S'

    def next_tile(self, coming_from: 'Tile') -> 'Tile':
        if (
            self.north and
            coming_from != self.north and
            self.has_connection_to_north() and
            self.north.has_connection_to_south()
        ):
            return self.north
        if (
            self.east and
            coming_from != self.east and
            self.has_connection_to_east() and
            self.east.has_connection_to_west()
        ):
            return self.east
        if (
            self.south and
            coming_from != self.south and
            self.has_connection_to_south() and
            self.south.has_connection_to_north()
        ):
            return self.south
        if (
            self.west and
            coming_from != self.west and
            self.has_connection_to_west() and
            self.west.has_connection_to_east()
        ):
            return self.west


def main():
    lines = tuple(util.iter_input())

    tiles: dict[(int, int), Tile] = dict()
    for x_pos, line in enumerate(lines):
        for y_pos, tile in enumerate(line):
            tiles[(x_pos, y_pos)] = Tile(
                tile=tile,
                x_pos=x_pos,
                y_pos=y_pos,
            )

    start_tile = None
    for pos, tile in tiles.items():
        tile.north = tiles.get((pos[0] - 1, pos[1]))
        tile.east = tiles.get((pos[0], pos[1] + 1))
        tile.south = tiles.get((pos[0] + 1, pos[1]))
        tile.west = tiles.get((pos[0], pos[1] - 1))

        if tile.tile == 'S':
            start_tile = tile

    pipe: dict[Tile, int] = {
        (start_tile.x_pos, start_tile.y_pos): 0,
    }
    current = start_tile
    previous = None

    while (next := current.next_tile(coming_from=previous)) != start_tile:
        previous = current
        current = next
        pipe[(current.x_pos, current.y_pos)] = pipe[(previous.x_pos, previous.y_pos)] + 1

    steps = math.ceil(max(pipe.values()) / 2)

    print(f'1) {steps} steps are required')

    # Shoelace Formula
    # formula requires counterclockwise order
    vertices = sorted(pipe.keys(), key=pipe.get, reverse=True)

    area = 0
    for idx, vertice in enumerate(vertices[:-1]):
        area += vertice[0] * vertices[idx + 1][1] - vertices[idx + 1][0] * vertice[1]
    area += vertices[-1][0] * vertices[0][1] - vertices[0][0] * vertices[-1][1]
    area *= 0.5

    # Pick's Theorem
    enclosed_tiles = area - len(vertices) / 2 + 1

    print(f'2) {int(enclosed_tiles)} tiles are enclosed by the loop')


if __name__ == '__main__':
    main()
