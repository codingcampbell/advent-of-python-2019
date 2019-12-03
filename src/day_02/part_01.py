import sys
from ..intcode import vm


def parse_input(input_file):
    return [int(x) for x in input_file.read().split(',')]


def main(input_file):
    """
    To do this, before running the program, replace position 1 with the value
    12 and replace position 2 with the value 2. What value is left at position
    0 after the program halts?
    """

    state = parse_input(input_file)
    state[1] = 12
    state[2] = 2
    vm.run_program(state)

    print(state[0])


if __name__ == '__main__':
    main(sys.stdin)
