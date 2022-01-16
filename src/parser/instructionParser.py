try:
    from src.parser.register import Register
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
