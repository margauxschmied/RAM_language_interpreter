
try:
    from src.instruction.register import Register
    from src.cantor_int import Int
except:
    from register import Register
    from cantor_int import Int


class Instruction:
    def __init__(self, num_instr: int, register: Register, n=None, next=None):
        self.numInstr = num_instr
        self.register = register
        self.n = n
        self.next = next
        # self.instr = [self.add_instr,
        #               self.sub_instr,
        #               self.jumpb_instr,
        #               self.jumpf_instr, None, None, None, None][num_instr]

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def add_instr(self, dico):
        dico[self.register] += 1
        dico.update_current_instr(1)

    def sub_instr(self, dico):
        dico[self.register] -= 1
        dico.update_current_instr(1)

    def jumpb_instr(self, dico):
        dico.update_current_instr(-self.n if dico[self.register] != 0 else 1)

    def jumpf_instr(self, dico):
        dico.update_current_instr(self.n if dico[self.register] != 0 else 1)

    def calc_instr(self, dico):
        self.instr(dico)

    def __str__(self):
        dico = {"istr_nb": self.numInstr, "reg": self.register}
        if self.n != None:
            dico['n'] = self.n
        return str(dico)

    def __repr__(self) -> str:
        return self.__str__()

    def encode_instr(self):
        if self.numInstr == 0:
            return self.register * 3
        elif self.numInstr == 1:
            return self.register * 3 + 1
        elif self.numInstr == 2:
            return 3 * Int.couple_to_int((self.register, (1, self.n))) + 2
        else:
            return 3 * Int.couple_to_int((self.register, (0, self.n))) + 2

    def transform_to_interpreter(self):
