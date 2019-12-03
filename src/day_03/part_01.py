import sys


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_line_points(move_commands):
    point = {'x': 0, 'y': 0}
    points = {}
    steps = 0

    for cmd in move_commands:
        direction = cmd[0]
        axis = 'x' if direction in ('L', 'R') else 'y'

        num = int(cmd[1:])
        step = -1 if direction in ('L', 'U') else 1

        target = point[axis] + num * step

        # Step through all integer values between current position and target
        while point[axis] != target:
            # Only record steps taken to reach point the first time
            pt = (point['x'], point['y'])
            if pt not in points:
                points[pt] = steps

            point[axis] += step
            steps += 1

    return points


def parse_input(input_file):
    lines = [get_line_points(line.split(',')) for line in input_file]
    crossings = set(lines[0].keys()).intersection(set(lines[1].keys()))
    return lines, crossings
    

def main(input_file):
    lines, crossings = parse_input(input_file)
    distances = (manhattan_distance(c, (0, 0)) for c in crossings)
    min_dist = min(d for d in distances if d > 0)
    print(min_dist)


if __name__ == '__main__':
    main(sys.stdin)
