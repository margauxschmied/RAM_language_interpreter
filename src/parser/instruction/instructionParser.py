try:
    from src.parser.instruction.register import Register
except:
    from register import Register


class Instruction:
    def __init__(self, num_instr: int, register: Register, n=None, next=None, is_macro=False):
        self.num_instr = num_instr
        self.register = register
        self.n = n
        self.next = next
        self.is_macro = is_macro

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def list_instruction(self):
        list = []
        currentInstruction = self
        while currentInstruction != None:
            list.append(currentInstruction)
            if currentInstruction.is_macro:
                list.append(currentInstruction.instruction.list_instruction())
            currentInstruction = currentInstruction.next

        return list

    def __str__(self) -> str:
        return f"{self.num_instr} {self.register} {self.n}"

    def __repr__(self) -> str:
        return self.__str__()
