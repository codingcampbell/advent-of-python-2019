from enum import IntEnum


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99

    @staticmethod
    def from_instruction_int(n):
        """
        Returns raw opcode and parameter mode ints from instruction int

        >>> OpCode.from_instruction_int(1012)
        (12, [0, 1])

        >>> OpCode.from_instruction_int(1101012)
        (12, [0, 1, 0, 1, 1])

        >>> OpCode.from_instruction_int(99)
        (99, [])

        >>> OpCode.from_instruction_int(103)
        (3, [1])
        """

        s = str(n)
        opcode = int(s[-2:])
        modes = [int(x) for x in s[:-2]]

        # Modes are actually right-to-left
        modes.reverse()

        return (opcode, modes)


class ParameterMode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1


class Instruction:
    def __init__(self, param_modes):
        self.num_parameters = 0
        self.param_modes = param_modes

    @staticmethod
    def from_instruction_int(instruction_int):
        opcode, param_modes = OpCode.from_instruction_int(instruction_int)
        instruction = _instructions.get(opcode, None)
        if not instruction:
            return None

        return instruction(param_modes)

    def validate(self, stack, state):
        n = self.num_parameters
        if len(stack) != n:
            raise ValueError('Expected {} parameters in `stack`'.format(n))

    def exec(self, stack, state):
        self.validate()
        return True


class InstructionAdd(Instruction):
    def __init__(self, param_modes):
        super().__init__(param_modes)
        self.num_parameters = 3

    def exec(self, stack, state, program):
        super().validate(stack, state)
        state[stack[2]] = state[stack[0]] + state[stack[1]]
        return True


class InstructionMultiply(Instruction):
    def __init__(self, param_modes):
        super().__init__(param_modes)
        self.num_parameters = 3

    def exec(self, stack, state, program):
        super().validate(stack, state)
        state[stack[2]] = state[stack[0]] * state[stack[1]]
        return True


class InstructionHalt(Instruction):
    def exec(self, stack, state, program):
        super().validate(stack, state)
        return False


_instructions = {
    OpCode.ADD: InstructionAdd,
    OpCode.MULTIPLY: InstructionMultiply,
    OpCode.HALT: InstructionHalt,
}
