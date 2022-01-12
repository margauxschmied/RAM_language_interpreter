from typing import Dict, List

try:
    from src.instruction import RAM
    from src.cantor_int import Int
    from src.decode_int import decode_int_instr, decode_int_program
    from src.instruction import RawInstruction, Macro
except:
    from instruction import RAM
    from cantor_int import Int
    from decode_int import decode_int_instr, decode_int_program
    from instruction import RawInstruction, Macro


class Interpreter:
    """
        A class taking a List of Instruction and interpreting them

        You can `treat one instr` or `treat_all_instr`

        The RC is stored in current_instr
    """

    def __init__(self, instr_list: List[RawInstruction], macros: Dict[str, Macro] = dict(), memory=RAM()) -> None:
        self.instr_list = instr_list
        self.current_instr = Int(1)
        self.end = False
        self.memory = memory
        self.macros = macros

    def update_current_instr(self, n: int):
        self.current_instr += n

    def translate_macro(self, instr):
        return self.macros[instr.numInstr].clone_instr(instr.register)

    def treat_one_instr(self):
        il, ci = self.instr_list, self.current_instr
        if ci == 0 or ci - 1 >= len(il):
            self.end = True
        elif il[ci-1].is_macro:
            instrs = self.translate_macro(il[ci - 1])
            sub_int = Interpreter(instrs, self.macros, self.memory)
            sub_int.treat_all_instr()
            sub_int_inst = sub_int.current_instr
            if sub_int_inst == 0:
                self.current_instr += 1
            elif sub_int_inst < 0:
                self.current_instr -= sub_int_inst
            else:
                self.current_instr += (sub_int_inst - len(instrs))
        else:
            il[ci-1].execute(self.memory, self)

    def treat_all_instr(self):
        while not self.end:
            self.treat_one_instr()

    def get_otput(self):
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
        return repr((self.current_instr, self.memory))


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
        [RawInstruction('id', ['x', 100], is_macro=True),
         RawInstruction(0, 100),
         RawInstruction(0, 'y'),
         RawInstruction(1, 100),
         RawInstruction(2, 100, 2),
         RawInstruction(1, 'y')])

    ADD_IN_Z_MACRO = Macro(
        'add', ['x', 'y', 'z'],
        [RawInstruction('id', ['x', 100], is_macro=True),
         RawInstruction('id', ['y', 'z'], is_macro=True),
         RawInstruction(0, 100),
         RawInstruction(1, 100),
         RawInstruction(0, 'z'),
         RawInstruction(2, 100, 2),
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

    for i in range(20):
        interp = Interpreter([
            RawInstruction('sum_0_to_n', [0], is_macro=True)
        ], macros, RAM(i))
        interp.treat_all_instr()
        print(f"The sum from 0 to {i} is {interp.get_otput()}")
        interp.encode_list_instr()
