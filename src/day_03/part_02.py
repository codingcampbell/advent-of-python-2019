import sys
from .part_01 import parse_input


def count_intersection_steps(line1, line2, central=(0, 0)):
    result = {}
    steps = 0
    for point in line1:
        if point != central and point not in result and point in line2:
            result[point] = steps

        steps += 1

    return result


def main(input_file):
    lines = parse_input(input_file)

    steps = [
        count_intersection_steps(lines[0], lines[1]),
        count_intersection_steps(lines[1], lines[0]),
    ]

    min_steps = min(steps[0][k] + steps[1][k] for k in steps[0])
    print(min_steps)


if __name__ == '__main__':
    main(sys.stdin)
