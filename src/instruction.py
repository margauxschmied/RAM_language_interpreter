class Instruction:
    def __init__(self, num_instr: int, register: int, n=None, next=None):
        self.numInstr = num_instr
        self.register = register
        self.n = n
        self.next = next

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    
    def toString(self):
        return {"number of instruction": self.numInstr, "register": self.register, "n": self.n}
