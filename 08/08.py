#!/usr/bin/env python3

import dataclasses
import math
import re

import util


@dataclasses.dataclass
class Node:
    name: str
    left: str
    right: str


def main(part: int):
    lines = tuple(util.iter_input())

    instructions = lines[0]
    nodes: dict[str, Node] = dict()
    for line in lines[2:]:
        name = line.split(' = ')[0]
        nodes[name] = Node(
            name=name,
            left=line.split(' = ')[1].split(', ')[0].split('(')[1],
            right=line.split(' = ')[1].split(', ')[1].split(')')[0],
        )

    if part == 1:
        start_nodes_regex = 'AAA'
        destination_nodes_regex = 'ZZZ'
    elif part == 2:
        start_nodes_regex = r'.*A'
        destination_nodes_regex = r'.*Z'

    for node in nodes.values():
        node.left = nodes[node.left]
        node.right = nodes[node.right]


    start_nodes: list[Node] = [
        node for node in nodes.values()
        if re.match(start_nodes_regex, node.name)
    ]

    distances = []
    for node in start_nodes:
        distance = 0
        current_instruction_idx = 0

        while True:
            current_instruction_idx %= len(instructions)
            instruction = instructions[current_instruction_idx]
            current_instruction_idx += 1
            distance += 1

            node = node.left if instruction == 'L' else node.right

            if re.match(destination_nodes_regex, node.name):
                break
        distances.append(distance)

    steps = math.lcm(*distances)

    print(f'{part}) {steps} steps are required to reach {destination_nodes_regex}')


if __name__ == '__main__':
    main(part=1)
    main(part=2)
