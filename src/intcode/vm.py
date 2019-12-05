from .instructions import Instruction


def run_program(state, input=None):
    pointer = 0
    state_length = len(state)

    program = {
        'input': input,
        'output': None
    }

    while pointer < state_length:
        instruction_int = state[pointer]
        instruction_class, param_modes = Instruction.from_instruction_int(
            instruction_int
        )

        if not instruction_class:
            raise ValueError('Unknown instruction type: {}'
                             .format(instruction_int))

        stack_size = instruction_class.num_parameters
        pointer += 1  # Move pointer to beginning of arguments
        stack = state[pointer:pointer + stack_size]
        instruction = instruction_class(param_modes, stack, state, program)
        result = instruction.exec()

        # Instructions can return -1 to halt execution
        if result == -1:
            break

        # Instructions can return ints to change pointer (e.g. for jumps)
        if type(result) == int:
            pointer = result

        # Otherwise we move the pointer as usual
        else:
            pointer += stack_size

    return program['output']


def test_run_program():
    # It should handle positional + immediate param modes
    state = [1002, 4, 3, 4, 33, 99]
    run_program(state)
    assert state[4] == 99

    # It should handle negative values
    state = [1101, 100, -1, 4, 0]
    run_program(state)
    assert state[4] == 99

    # Test InstructionStore
    state = [3, 3, 99, 0]
    run_program(state, 10)
    assert state[3] == 10

    # run_program should return result of InstructionOutput
    state = [104, 52]
    assert run_program(state) == 52
