try:
    from src.cantor_int import Int
except:
    from cantor_int import Int

from collections import namedtuple
from typing import List


class RawInstruction:
    def __init__(self, num_instr, register, n=None, is_macro=False, next=None):
        self.is_macro = is_macro
        self.numInstr = num_instr
        self.register = register
        self.n = n
        self.next = next

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def clone(self, new_reg=None):
        return Instruction(self.numInstr, self.register if new_reg is None else new_reg, self.n)

    def execute(self, dico):
        return self.clone().execute(dico)

    def encode_instr(self):
        return self.clone().encode_instr()

    def __str__(self):
        dico = {"istr_nb": self.numInstr, "reg": self.register}
        if self.n != None:
            dico['n'] = self.n
        return str(dico)

    def __repr__(self) -> str:
        return self.__str__()


class Instruction(RawInstruction):
    def __init__(self, num_instr: int, register: int, n=None, next=None):
        super().__init__(Int(num_instr), Int(register),
                         n=Int(n) if n is not None else None, next=next)
        self.instr = [self.add_instr,
                      self.sub_instr,
                      self.jumpb_instr,
                      self.jumpf_instr,
                      self.push_instr,
                      self.pop_instr][num_instr]

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

    def execute(self, dico):
        self.register = Int(self.register)
        self.instr(dico)

    def push_instr(self, dico):
        dico['Monster'] = dico[self.register]

    def pop_instr(self, dico):
        dico[self.register] = dico['Monster']

    def encode_instr(self):
        if self.numInstr == 0:
            return self.register * 3
        elif self.numInstr == 1:
            return self.register * 3 + 1
        elif self.numInstr == 2:
            return 3 * Int.couple_to_int((self.register, (1, self.n))) + 2
        else:
            return 3 * Int.couple_to_int((self.register, (0, self.n))) + 2


class Macro:
    def __init__(self, nom, params, instr_list: List[RawInstruction]) -> None:
        self.nom = nom
        if len(params) != len(set(params)):
            raise Exception(f'Duplicate params in macro {nom}')
        self.params = params
        self.instr_list = instr_list

    def set_macro_dict(self, dico):
        self.macro_dict = dico

    def remove_macro(self, params, interp):
        if len(self.params) != len(set(params)):
            raise Exception(f'Invalid call to macro {self.nom}')
        dico = {macro_var: real_var for macro_var,
                real_var in zip(self.params, params)}
        res = []
        for instr in self.instr_list:
            if instr.register in dico:
                res.append(instr.clone(new_reg=dico[instr.register]))
            else:
                res.append(instr)
        interp.instr_list[interp.current_instr:interp.current_instr] = res
