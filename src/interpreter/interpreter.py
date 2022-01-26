from typing import Dict, List

try:
    from src.interpreter.instruction import *
    from src.interpreter.cantor_int import *
    from src.interpreter.interpreter import *
    from src.interpreter.existing_macros import *
except:
    from src.interpreter.instruction import *
    from interpreter.cantor_int import *
    from interpreter.interpreter import *
    from interpreter.existing_macros import *


class Interpreter:
    """
        A class taking a List of Instruction and interpreting them

        You can `treat one instr` or `treat_all_instr`

        The RC is stored in current_instr
    """

    def __init__(self, instr_list: List[RawInstruction], macro: Dict[str, Macro], memory=RAM()) -> None:
        self.instr_list = instr_list
        self.current_instr = Int(1)
        self.end = False
        self.memory = memory
        self.macros = {'push': macros['push'], 'pop': macros['pop']}
        for key, value in macro.items():
            self.macros[key] = value
        self.remove_macros()

    def update_current_instr(self, n: int):
        self.current_instr = int(Int(self.current_instr) + n)

    def translate_macro(self, instr):
        return self.macros[instr.num_instr].clone_instr(instr.register)

    def treat_one_instr(self):
        il, ci = self.instr_list, self.current_instr
        if ci == 0 or ci - 1 >= len(il):
            self.end = True
        else:
            il[ci-1].execute(self.memory, self)
        return self.memory

    def treat_all_instr(self):
        while not self.end:
            self.treat_one_instr()
        return self.memory

    def get_output(self):
        return self.memory[1]

    def init_zero(self, value):
        self[0] = value

    def encode_list_instr(self):
        t = self.instr_list[::-1]
        pos = 0
        while pos < len(t):
            current = t[pos]
            if current.is_macro:
                instrs = self.translate_macro(t.pop(pos))
                t[pos:pos] = instrs
            else:
                pos += 1
        res = t.pop(0).encode_instr(), 0
        while len(t) != 0:
            current = t.pop(0)
            if current.is_macro:
                instrs = self.translate_macro(current)
                t = instrs + t
            else:
                res = current.encode_instr(), res
        return Int.couple_to_int(res)

    def __str__(self) -> str:
        res = []
        for instr in self.instr_list:
            res.append(str(instr))
        return "\n".join(res)

    def remove_macros(self):
        def count_macro(a, b):
            return Int(sum([self.macros[self.instr_list[i].numInstr].len(self.macros)
                            for i in range(a, b) if self.instr_list[i].is_macro])) - 1

        def aux():
            res = []
            for pos, i in enumerate(self.instr_list):
                if i.numInstr == 2:
                    i.n = Int(i.n) + count_macro(Int(pos) - Int(i.n), Int(pos))
                if i.numInstr == 3:
                    i.n = Int(i.n) + count_macro(Int(pos), min(
                        Int(pos) + Int(i.n), len(self.instr_list)))
            for i in self.instr_list:
                if i.is_macro:
                    sub_interp = Interpreter(
                        self.macros[i.numInstr].clone_instr(i.register), self.macros, self.memory)
                    res.append(sub_interp.remove_macros())
                else:
                    res.append(i)
            return res

        def flatten_list(L, res):
            if not isinstance(L, list):
                res.append(L)
            else:
                for i in L:
                    if isinstance(L, list):
                        flatten_list(i, res)
                    else:
                        res.append(i)
            return res
        self.instr_list = flatten_list(aux(), [])
        return self.instr_list

    def reset(self, new_entry=0):
        self.current_instr = 1
        self.memory = RAM(new_entry)
        self.end = False


if __name__ == '__main__':

    ID_MACRO = Macro(
        'id', ['x', 'y'],
        [RawInstruction(0, 'x'),
         RawInstruction(1, 'x'),
         RawInstruction(0, 1000),
         RawInstruction(2, 'x', 2),
         RawInstruction(1, 1000),
         RawInstruction(0, 'x'),
         RawInstruction(0, 'y'),
         RawInstruction(2, 1000, 3),
         RawInstruction(1, 'x'),
         RawInstruction(1, 'y')])

    ADD_MACRO = Macro(
        'add', ['x', 'y'],
        [RawInstruction('id', ['x', 500], is_macro=True),
         RawInstruction(0, 500),
         RawInstruction(0, 'y'),
         RawInstruction(1, 500),
         RawInstruction(2, 500, 2),
         RawInstruction(1, 'y')])

    ADD_IN_Z_MACRO = Macro(
        'add', ['x', 'y', 'z'],
        [RawInstruction('id', ['x', 500], is_macro=True),
         RawInstruction('id', ['y', 'z'], is_macro=True),
         RawInstruction(0, 500),
         RawInstruction(1, 500),
         RawInstruction(0, 'z'),
         RawInstruction(2, 500, 2),
         RawInstruction(1, 'z')])

    CLEAR = Macro(
        'clear', ['x'],
        [RawInstruction(1, 'x'),
         RawInstruction(2, 'x', 1)])

    SUM_0_TO_N = Macro(
        'sum_0_to_n', ['x'],
        [RawInstruction(0, 'x'),
         RawInstruction(1, 'x'),
         RawInstruction('add', ['x', 1], is_macro=True),
         RawInstruction(2, 'x', 2)])

    macros = {
        'id': ID_MACRO,
        'add': ADD_MACRO,
        'add_in_z': ADD_IN_Z_MACRO,
        'clear': CLEAR,
        'sum_0_to_n': SUM_0_TO_N
    }

    interp: Interpreter = Interpreter([
        RawInstruction('sum_0_to_n', [0], is_macro=True)
    ], macros, RAM(20))

    print("\n".join(map(str, interp.instr_list)))

    for i in range(150):
        interp.reset(i)
        interp.treat_all_instr()
        print(f"The sum from 0 to {i} is {interp.get_output()}")

    print(str(interp))
