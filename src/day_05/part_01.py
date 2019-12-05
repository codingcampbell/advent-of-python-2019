import sys
from ..intcode import vm


def parse_input(input_file):
    return [int(x) for x in input_file.read().split(',')]


def main(input_file):
    """
    After providing 1 to the only input instruction and passing all the tests,
    what diagnostic code does the program produce?
    """

    state = parse_input(input_file)
    print(vm.run_program(state, 1))


if __name__ == '__main__':
    main(sys.stdin)
