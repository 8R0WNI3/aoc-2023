import collections.abc
import os


own_dir = os.path.abspath(os.path.dirname(__file__))
input_file = os.path.join(own_dir, 'input.txt')


def iter_input() -> collections.abc.Generator[str, None, None]:
    with open(input_file) as f:
        while (line := f.readline()):
            yield line.rstrip()
