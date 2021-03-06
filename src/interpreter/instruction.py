try:
    from src.parser.instruction.register import *
    from src.interpreter.cantor_int import *
except:
    from interpreter.cantor_int import *

from typing import List


class RawInstruction:
    def __init__(self, num_instr, register, n=None, is_macro=False, next=None):
        self.is_macro = is_macro or type(num_instr) == str
        self.numInstr = num_instr
        self.register = register
        self.n = n

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def clone_in_instr(self, new_reg=None):
        return Instruction(self.numInstr, self.register if new_reg is None else new_reg, self.n)

    def clone(self):
        return RawInstruction(self.numInstr, self.register, self.n, self.is_macro)

    def execute(self, dico, interp):
        return self.clone_in_instr().execute(dico, interp)

    def encode_instr(self):
        if self.numInstr == 0:
            return self.register * 3
        elif self.numInstr == 1:
            return self.register * 3 + 1
        elif self.numInstr == 2:
            return 3 * Int.couple_to_int((self.register, (1, self.n))) + 2
        else:
            return 3 * Int.couple_to_int((self.register, (0, self.n))) + 2

    def __str__(self) -> str:
        if self.numInstr == 0:
            return f"R{self.register} = R{self.register} + 1"
        elif self.numInstr == 1:
            return f"R{self.register} = R{self.register} - 1"
        elif self.numInstr == 2:
            return f"IF R{self.register} != 0 then gotob {self.n}"
        elif self.numInstr == 3:
            return f"IF R{self.register} != 0 then gotof {self.n}"
        elif self.numInstr == 4:
            return f"rp(R{self.register}, R{self.n})"
        elif self.numInstr == 5:
            return f"rl(R{self.register}, R{self.n})"
        else:
            return "{}({})".format(self.numInstr, ",".join(map(lambda x: f"R{x}", self.register)))

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
                      self.right_part,
                      self.left_part][num_instr]

    def add_instr(self, dico, interp):
        dico[self.register] += 1
        interp.update_current_instr(1)

    def sub_instr(self, dico, interp):
        dico[self.register] -= 1
        interp.update_current_instr(1)

    def jumpb_instr(self, dico, interp):
        interp.update_current_instr(-self.n if dico[self.register] != 0 else 1)

    def jumpf_instr(self, dico, interp):
        interp.update_current_instr(self.n if dico[self.register] != 0 else 1)

    def right_part(self, dico, interp):
        dico[self.n] = Int(dico[self.register]).right()
        interp.update_current_instr(1)

    def left_part(self, dico, interp):
        dico[self.n] = Int(dico[self.register]).left()
        interp.update_current_instr(1)

    def execute(self, dico, interp):
        self.instr(dico, interp)


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
        res = self.clone_instr(params)
        interp.instr_list[interp.current_instr:interp.current_instr] = res

    def clone_instr(self, params) -> List[Instruction]:
        dico = {macro_var: real_var for macro_var,
                real_var in zip(self.params, params)}
        res: List[Instruction] = []
        clone = [i.clone() for i in self.instr_list]
        for instr in clone:
            if not instr.is_macro and instr.register in dico:
                instr.register = dico[instr.register]
            elif instr.is_macro:
                instr.register = [dico[var] if var in dico else var
                                  for var in instr.register]
            res.append(instr)
        return res

    def len(self, dico):
        acc = 0
        for i in self.instr_list:
            if i.is_macro:
                acc += dico[i.numInstr].len(dico)
            else:
                acc += 1
        return acc

    def __str__(self) -> str:
        return f"{self.nom} ({self.params}) {self.instr_list};"

    def __repr__(self) -> str:
        return str(self)


class RAM(dict):
    def __init__(self, start_value=0):
        self[0] = Int(start_value)

    def __getitem__(self, k) -> Int:
        if k not in dict(self):
            self.__setitem__(k, Int(0))
        return dict(self)[k]

    def __setitem__(self, key: int, value: Int) -> None:
        return super().__setitem__(key, Int(value))
