import sys

OPCODE_ADD = 1
OPCODE_MULT = 2
OPCODE_HALT = 99


def intcode(stack, state):
    """
    99 means that the program is finished and should immediately halt

    >>> intcode([99], [])
    False

    Encountering an unknown opcode means something went wrong.

    >>> intcode([-1], [])
    Traceback (most recent call last):
    ValueError: Unexpected opcode: -1
    """

    if stack[0] == OPCODE_HALT:
        return False

    if stack[0] == OPCODE_ADD:
        state[stack[3]] = state[stack[1]] + state[stack[2]]
        return True

    if stack[0] == OPCODE_MULT:
        state[stack[3]] = state[stack[1]] * state[stack[2]]
        return True

    raise ValueError("Unexpected opcode: {}".format(stack[0]))


def intcode_program(state):
    pointer = 0
    state_length = len(state)
    stack_size = 4

    while pointer < state_length - stack_size:
        if not intcode(state[pointer:pointer + 4], state):
            return state

        pointer += stack_size

    return state


def test_intcode_opcode_add():
    """
    For example, if your Intcode computer encounters 1,10,20,30, it should read
    the values at positions 10 and 20, add those values, and then overwrite the
    value at position 30 with their sum.
    """

    state = [x for x in range(0, 31)]
    state[10] = 5
    state[20] = 7
    state_target = [x for x in state]
    state_target[30] = state_target[10] + state_target[20]

    intcode([OPCODE_ADD, 10, 20, 30], state)

    assert state[30] == state_target[30]


def test_intcode_opcode_mult():
    """
    Opcode 2 works exactly like opcode 1, except it multiplies the two inputs
    instead of adding them. Again, the three integers after the opcode indicate
    where the inputs and outputs are, not their values.
    """

    state = [x for x in range(0, 21)]
    state_target = [x for x in state]
    state_target[20] = state_target[5] * state_target[10]

    intcode([OPCODE_MULT, 5, 10, 20], state)

    assert state[20] == state_target[20]


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
    intcode_program(state)

    print(state[0])


if __name__ == '__main__':
    main(sys.stdin)
