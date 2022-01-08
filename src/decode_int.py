from typing import List
from cantor_int import Int


def decode_int_instr(n: int):
    """
        Gödelisation :
        - ADD = Rk = Rk + 1 (n = 3 * k)
        - SUB = Rk = Rk - 1 (n = 3 * k + 1)
        - IFF = IF Rk != 0 THEN GOTOF n (n = 3 <0, <k, <n, 0>>> + 2)
        - IFB = IF Rk != 0 THEN GOTOB n (n = 3 <1, <k, <n, 0>>> + 2)
    """
    res: List[str] = []
    current = Int(n)
    if current % 3 < 2:
        current = current / 3
        res.append(
            'R{} = R{} {} 1'.format(current.left(), current.left(), ['+', '-'][current % 3 == 1]))
    else:
        current = current / 3
        type_saut = current.left()
        k = current.right().left()
        saut = current.right().right()
        inst = ('F', 'B')
        res.append(f'if R{k}!=0 THEN GOTO{inst[type_saut==1]} {saut}')
    return '\n'.join(res)


def decode_int_program(n):
    if type(n) == int:
        n = Int(n).int_to_couple()
    program = []
    while n[1] != 0:
        program.append(decode_int_instr(n[0]))
        n = n[1]
    return "\n".join(program)


if __name__ == '__main__':
    L = [1002500825, 2, 5, 8, 11]
    for elt in L:
        print(f"Decoding instruction {elt}:")
        try:
            print(decode_int_instr(elt))
        except Exception as e:
            print(e)
    N = 1002500826

    print(f"Decoding program {N} :")
    print(decode_int_program(1002500826))
