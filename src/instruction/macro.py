from src.instruction.instruction import Instruction
from src.instruction.register import Register


class Macro(Instruction):
    def __init__(self, name, register, instruction=None, next=None):
        super().__init__(name, register, None, next)
        self.name=name
        self.instruction=instruction
