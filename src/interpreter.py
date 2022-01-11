from typing import Dict, List

try:
    from src.cantor_int import Int
    from src.decode_int import decode_int_instr, decode_int_program
    from src.instruction import RawInstruction, Macro
except:
    from cantor_int import Int
    from decode_int import decode_int_instr, decode_int_program
    from instruction import RawInstruction, Macro


class Interpreter(dict):
    """
        A class taking a List of Instruction and interpreting them

        You can `treat one instr` or `treat_all_instr`

        The RC is stored in current_instr
    """

    def __init__(self, instr_list: List[RawInstruction], start_value=0, macros: Dict[str, Macro] = dict()) -> None:
        self.instr_list = instr_list
        self.current_instr = Int(1)
        self.end = False
        self[0] = Int(start_value)
        self.macros = macros
        self.remove_macros()

    def remove_macros(self):
        while self.current_instr - 1 < len(self.instr_list):
            current_instr = self.instr_list[self.current_instr - 1]
            if current_instr.is_macro:
                self.instr_list.pop(self.current_instr-1)
                self.current_instr -= 1
                macro = self.macros[current_instr.numInstr]
                macro.remove_macro(current_instr.register, self)
            self.current_instr += 1
        self.current_instr = Int(1)

    def update_current_instr(self, n: int):
        self.current_instr += n

    def treat_one_instr(self):
        il, ci = self.instr_list, self.current_instr
        if ci == 0 or ci - 1 >= len(il):
            self.end = True
        else:
            il[ci-1].execute(self)

    def treat_all_instr(self):
        while not self.end:
            self.treat_one_instr()

    def get_otput(self):
        return self[1]

    def init_zero(self, value):
        self[0] = value

    def encode_list_instr(self):
        t = self.instr_list[::-1]
        res = (t.pop(0).encode_instr(), 0)
        while len(t) != 0:
            res = (t.pop(0).encode_instr(), res)
        print(res)
        return Int.couple_to_int(res)

    def __getitem__(self, k) -> Int:
        if k not in dict(self):
            self.__setitem__(k, Int(0))
        return dict(self)[k]

    def __setitem__(self, key: int, value: Int) -> None:
        return super().__setitem__(key, Int(value))

    def __str__(self) -> str:
        return repr((self.current_instr, self))


if __name__ == '__main__':
    """
        Ram program returing N
    """
    N = 5
    i = Interpreter(
        [RawInstruction(1, 0),
         RawInstruction(0, 1),
         RawInstruction(2, 0, 2)], N)

    # i.treat_all_instr()
    # print(i.get_otput())

    # print(decode_int_program(i.encode_list_instr()))

    """
        Ram program returing sigma(N)
    """
    N = 1
    i = Interpreter(
        [RawInstruction(0, 0),
         RawInstruction(1, 0),
         RawInstruction(0, 1),
         RawInstruction(2, 0, 2)], N)
    # i.treat_all_instr()
    # print(i.get_otput())

    # print(decode_int_program(i.encode_list_instr()))

    """
        Ram program returning N * 2
    """
    N = 50
    i = Interpreter(
        [RawInstruction(0, 0),

         RawInstruction(0, 2),
         RawInstruction(0, 2),
         RawInstruction(1, 0),
         RawInstruction(2, 0, 3),
         RawInstruction(1, 2),

         RawInstruction(1, 2),
         RawInstruction(0, 1),
         RawInstruction(2, 2, 2),
         RawInstruction(1, 1)], N
    )
    # i.treat_all_instr()
    # print(i.get_otput())

    # sum(range(N))

    ID_MACRO = Macro(
        'id', ['x', 'y'],
        [RawInstruction(0, 0),
         RawInstruction(1, 0),
         RawInstruction(0, 5),
         RawInstruction(2, 0, 2),
         RawInstruction(1, 5)],
    )

    macros = {
        'id': ID_MACRO,
    }

    N = 20
    i = Interpreter(
        [
            # identity
            RawInstruction('id', [0, 5], is_macro=True),
            # sum
            RawInstruction(0, 5),
            RawInstruction(0, 1),
            RawInstruction(1, 5),
            RawInstruction(0, 0),
            RawInstruction(2, 5, 3),
            # # decrease i
            RawInstruction(1, 1),
            RawInstruction(1, 0),
            RawInstruction(1, 0),
            RawInstruction(2, 0, 13)
        ], N, macros
    )

    i.treat_all_instr()
    print(i.get_otput())
    # print(decode_int_program(i.encode_list_instr()))
    print(i)
