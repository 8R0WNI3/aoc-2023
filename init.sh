#!/usr/bin/env bash

dir=$(pwd)
echo "current directory is $dir"

util_file=$(cat <<EOL
import collections.abc
import os


own_dir = os.path.abspath(os.path.dirname(__file__))
input_file = os.path.join(own_dir, 'input.txt')


def iter_input() -> collections.abc.Generator[str, None, None]:
    with open(input_file) as f:
        while (line := f.readline()):
            yield line.rstrip()

EOL
)

exec_file=$(cat <<EOL
#!/usr/bin/env python3

import util


def main():
    for line in util.iter_input():
        # continue HERE with your code


if __name__ == '__main__':
    main()

EOL
)

for i in {1..24}; do
    new_dir=$(printf "%02i" $i)

    if [ -d "$(readlink -f $dir/$new_dir)" ]; then
        echo "directory $new_dir already exists, skipping creation..."
        continue
    fi

    echo "creating directory $new_dir"
    mkdir $new_dir
    cd $new_dir

    echo "creating \`input.txt\` file"
    touch input.txt

    echo "creating \`util.py\` file"
    echo -e "$util_file" >> util.py

    echo "creation \`$new_dir\` file"
    echo -e "$exec_file" >> $new_dir.py
    chmod +x $new_dir.py

    cd $dir
done
