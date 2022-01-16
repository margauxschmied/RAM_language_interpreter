try:
    from src.parser.instructionParser import Instruction
    from src.parser.register import Register
except:
    from instructionParser import Instruction
    from register import Register


class Macro(Instruction):
    def __init__(self, num_instr, register, instruction=None, next=None):
        super().__init__(num_instr, register, None, next, True)
        self.instruction = instruction
