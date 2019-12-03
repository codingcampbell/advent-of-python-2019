import sys
from .part_01 import parse_input


def main(input_file):
    lines, crossings = parse_input(input_file)
    keys = (c for c in crossings if lines[0][c] > 0 and lines[1][c] > 0)
    min_steps = min((lines[0][k] + lines[1][k] for k in keys))
    print(min_steps)


if __name__ == '__main__':
    main(sys.stdin)
