from enum import IntEnum


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    STORE = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
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
        return None

    def get_param(self, index):
        if self.param_modes[index] == ParameterMode.IMMEDIATE:
            return self.stack[index]

        # Default ParameterMode.POSITION
        return self.state[self.stack[index]]


class InstructionAdd(Instruction):
    num_parameters = 3

    def exec(self):
        self.state[self.stack[2]] = self.get_param(0) + self.get_param(1)


class InstructionMultiply(Instruction):
    num_parameters = 3

    def exec(self):
        self.state[self.stack[2]] = self.get_param(0) * self.get_param(1)


class InstructionStore(Instruction):
    num_parameters = 1

    def exec(self):
        self.state[self.stack[0]] = self.program['input']


class InstructionOutput(Instruction):
    num_parameters = 1

    def exec(self):
        self.program['output'] = self.get_param(0)


class InstructionHalt(Instruction):
    def exec(self):
        return -1


class InstructionJumpIfTrue(Instruction):
    """
    Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the
    instruction pointer to the value from the second parameter. Otherwise, it
    does nothing.
    """

    num_parameters = 2

    def exec(self):
        return self.get_param(1) if self.get_param(0) != 0 else None


class InstructionJumpIfFalse(Instruction):
    """
    Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
    instruction pointer to the value from the second parameter. Otherwise, it
    does nothing.
    """

    num_parameters = 2

    def exec(self):
        return self.get_param(1) if self.get_param(0) == 0 else None


class InstructionLessThan(Instruction):
    """
    Opcode 7 is less than: if the first parameter is less than the second
    parameter, it stores 1 in the position given by the third parameter.
    Otherwise, it stores 0.
    """

    num_parameters = 3

    def exec(self):
        result = 1 if self.get_param(0) < self.get_param(1) else 0
        self.state[self.stack[2]] = result


class InstructionEquals(Instruction):
    """
    Opcode 8 is equals: if the first parameter is equal to the second
    parameter, it stores 1 in the position given by the third parameter.
    Otherwise, it stores 0.
    """
    num_parameters = 3

    def exec(self):
        result = 1 if self.get_param(0) == self.get_param(1) else 0
        self.state[self.stack[2]] = result


_instructions = {
    OpCode.ADD: InstructionAdd,
    OpCode.MULTIPLY: InstructionMultiply,
    OpCode.STORE: InstructionStore,
    OpCode.OUTPUT: InstructionOutput,
    OpCode.JUMP_IF_TRUE: InstructionJumpIfTrue,
    OpCode.JUMP_IF_FALSE: InstructionJumpIfFalse,
    OpCode.LESS_THAN: InstructionLessThan,
    OpCode.EQUALS: InstructionEquals,
    OpCode.HALT: InstructionHalt,
}
