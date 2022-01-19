try:
    from src.parser.instruction.instructionParser import Instruction
except:
    from src.parser.instruction.instructionParser import Instruction


class Macro(Instruction):
    def __init__(self, num_instr, register, instruction=None, next=None):
        super().__init__(num_instr, register, None, next, True)
        self.instruction = instruction
        self.next = next

    def verification_of_use_register(self):
        listInstruction = self.instruction.list_instruction()
        listRegister = self.register.list_register_str()

        for instruction in listInstruction:
            tmpRegister = instruction.register.list_register()
            for r in tmpRegister:
                if isinstance(r, str):
                    if r not in listRegister:
                        return False
        return True

    def __str__(self) -> str:
        return "Macro " + super().__str__()
