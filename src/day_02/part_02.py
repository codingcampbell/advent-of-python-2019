import sys
from .part_01 import parse_input
from ..intcode import vm


def find_noun_and_verb(base_state, needle):
    for noun in range(0, 100):
        for verb in range(0, 100):
            state = base_state[:]  # Copy so base_state is not mutated
            state[1] = noun
            state[2] = verb
            vm.run_program(state)

            if state[0] == needle:
                return noun, verb

    return None, None


def main(input_file):
    base_state = parse_input(input_file)
    needle = 19690720

    noun, verb = find_noun_and_verb(base_state, needle)

    if None in (noun, verb):
        print('Could not find noun/verb that would produce {}'.format(needle))
        return

    print(100 * noun + verb)


if __name__ == '__main__':
    main(sys.stdin)
