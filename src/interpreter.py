from typing import List
try:
    from src.cantor_int import Int
    from src.decode_int import decode_int_instr, decode_int_program
    from src.instruction.instruction import Instruction
except:
    from cantor_int import Int
    from decode_int import decode_int_instr, decode_int_program
    from instruction.instruction import Instruction


class Interpreter(dict):
    """ 
        A class taking a List of Instruction and interpreting them

        You can `treat one instr` or `treat_all_instr`

        The RC is stored in current_instr
    """

    def __init__(self, instr_list: List[Instruction], start_value=0) -> None:
        self.instr_list = instr_list
        self.current_instr = Int(1)
        self.end = False
        self[0] = Int(start_value)

    def update_current_instr(self, n: int):
        self.current_instr += n

    def treat_one_instr(self):
        il, ci = self.instr_list, self.current_instr
        if ci == 0 or ci - 1 >= len(il):
            self.end = True
        else:
            il[ci-1].calc_instr(self)

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
        [Instruction(1, 0),
         Instruction(0, 1),
         Instruction(2, 0, 2)], N)

    i.treat_all_instr()
    print(i.get_otput())

    print(decode_int_program(i.encode_list_instr()))

    """
        Ram program returing sigma(N)
    """
    N = 1
    i = Interpreter(
        [Instruction(0, 0),
         Instruction(1, 0),
         Instruction(0, 1),
         Instruction(2, 0, 2)], N)
    i.treat_all_instr()
    print(i.get_otput())

    print(decode_int_program(i.encode_list_instr()))

    """
        Ram program returning N * 2
    """
    N = 50
    i = Interpreter(
        [Instruction(0, 0),

         Instruction(0, 2),
         Instruction(0, 2),
         Instruction(1, 0),
         Instruction(2, 0, 3),
         Instruction(1, 2),

         Instruction(1, 2),
         Instruction(0, 1),
         Instruction(2, 2, 2),
         Instruction(1, 1)], N
    )
    i.treat_all_instr()
    print(i.get_otput())
