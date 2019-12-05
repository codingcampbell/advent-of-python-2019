import sys
from .part_01 import parse_input
from ..intcode import vm


def main(input_file):
    """
    This time, when the TEST diagnostic program runs its input instruction to
    get the ID of the system to test, provide it 5, the ID for the ship's
    thermal radiator controller. This diagnostic test suite only outputs one
    number, the diagnostic code.

    What is the diagnostic code for system ID 5?
    """

    state = parse_input(input_file)
    print(vm.run_program(state, 5))


if __name__ == '__main__':
    main(sys.stdin)
