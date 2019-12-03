from enum import IntEnum


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


class Instruction:
    def __init__(self):
        self.num_parameters = 0

    @staticmethod
    def from_opcode(opcode):
        return _instructions.get(opcode, None)

    def validate(self, stack, state):
        n = self.num_parameters
        if len(stack) != n:
            raise ValueError('Expected {} parameters in `stack`'.format(n))

    def exec(self, stack, state):
        self.validate()
        return True


class InstructionAdd(Instruction):
    def __init__(self):
        super().__init__()
        self.num_parameters = 3

    def exec(self, stack, state):
        super().validate(stack, state)
        state[stack[2]] = state[stack[0]] + state[stack[1]]
        return True


class InstructionMultiply(Instruction):
    def __init__(self):
        super().__init__()
        self.num_parameters = 3

    def exec(self, stack, state):
        super().validate(stack, state)
        state[stack[2]] = state[stack[0]] * state[stack[1]]
        return True


class InstructionHalt(Instruction):
    def exec(self, stack, state):
        super().validate(stack, state)
        return False


_instructions = {
    OpCode.ADD: InstructionAdd(),
    OpCode.MULTIPLY: InstructionMultiply(),
    OpCode.HALT: InstructionHalt(),
}
