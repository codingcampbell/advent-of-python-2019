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
    num_parameters = 0

    @staticmethod
    def from_instruction_int(instruction_int):
        opcode, param_modes = OpCode.from_instruction_int(instruction_int)
        return _instructions.get(opcode, None), param_modes

    def __init__(self, param_modes, stack, state, program):
        self.param_modes = param_modes
        self.stack = stack
        self.state = state
        self.program = program
        self.validate()

    def validate(self):
        n = type(self).num_parameters
        if len(self.stack) != n:
            raise ValueError('Expected {} parameters in `stack`'.format(n))

        while len(self.param_modes) != n:
            # Assume POSITION mode for missing modes
            self.param_modes.append(ParameterMode.POSITION)

    def exec(self):
        return True

    def get_param(self, index):
        if self.param_modes[index] == ParameterMode.IMMEDIATE:
            return self.stack[index]

        # Default ParameterMode.POSITION
        return self.state[self.stack[index]]


class InstructionAdd(Instruction):
    num_parameters = 3

    def exec(self):
        self.state[self.stack[2]] = self.get_param(0) + self.get_param(1)
        return True


class InstructionMultiply(Instruction):
    num_parameters = 3

    def exec(self):
        self.state[self.stack[2]] = self.get_param(0) * self.get_param(1)
        return True


class InstructionHalt(Instruction):
    def exec(self):
        return False


_instructions = {
    OpCode.ADD: InstructionAdd,
    OpCode.MULTIPLY: InstructionMultiply,
    OpCode.HALT: InstructionHalt,
}
