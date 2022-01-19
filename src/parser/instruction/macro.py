try:
    from src.parser.instruction.instructionParser import Instruction
    from src.parser.instruction.register import Register
except:
    from src.parser.instruction.instructionParser import Instruction
    from parser.register import Register


class Macro(Instruction):
    def __init__(self, num_instr, register, instruction=None, next=None):
        super().__init__(num_instr, register, None, next, True)
        self.instruction = instruction
        self.next=next


    def verification_of_use_register(self):
        listInstruction = self.instruction.list_instruction()
        listRegister=self.register.list_register_str()

        for instruction in listInstruction:
            tmpRegister = instruction.register.list_register()
            for r in tmpRegister:
                if isinstance(r, str):
                    if r not in listRegister:
                        return False

        return True



