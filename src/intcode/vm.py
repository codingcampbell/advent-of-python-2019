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
        instruction = Instruction.from_instruction_int(instruction_int)
        if not instruction:
            raise ValueError('Unknown instruction type: {}'
                             .format(instruction_int))

        stack_size = instruction.num_parameters
        pointer += 1  # Move pointer to beginning of arguments
        stack = state[pointer:pointer + stack_size]

        # Instructions can return False to halt execution
        if not instruction.exec(stack, state, input):
            break

        pointer += stack_size

    return program['output']
