from .instructions import Instruction


def run_program(state):
    pointer = 0
    state_length = len(state)

    while pointer < state_length:
        opcode = state[pointer]
        instruction = Instruction.from_opcode(opcode)
        if not instruction:
            raise ValueError('Unknown opcode: {}'.format(opcode))

        stack_size = instruction.num_parameters
        pointer += 1  # Move pointer to beginning of arguments

        # Instructions can return False to halt execution
        if not instruction.exec(state[pointer:pointer + stack_size], state):
            break

        pointer += stack_size

    return state
