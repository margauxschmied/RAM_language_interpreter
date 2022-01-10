class Instruction:
    def __init__(self, num_instr: int, register: int, n=None, next=None):
        self.numInstr = num_instr
        self.register = register
        self.n = n
        self.next = next
        self.instr = [self.add_instr,
                      self.sub_instr,
                      self.jump_instr][num_instr]

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

    def jump_instr(self, dico):
        dico.update_current_instr(self.n if dico[self.register] != 0 else 1)

    def calc_instr(self, dico):
        self.instr(dico)

    def toString(self):
        return {"number of instruction": self.numInstr, "register": self.register, "n": self.n}
