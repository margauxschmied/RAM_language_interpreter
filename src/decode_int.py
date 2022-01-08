from typing import List, cast
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
    n = Int(n)
    if n % 3 < 2:
        current = n / 3
        res.append(
            'R{} = R{} {} 1'.format(current, current, ['+', '-'][n % 3 == 1]))
    else:
        try:
            current = n / 3
            k = current.left()
            type_saut = current.right().left()
            saut = current.right().right()
            inst = ('F', 'B')
            res.append(f'if R{k}!=0 THEN GOTO{inst[type_saut==1]} {saut}')
        except Exception as e:
            raise Exception(f'Cannot decode {n}')
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
    for i in range(21):
        try:
            print(f"Decoding program {i} :")
            print(decode_int_instr(i))
        except:
            print(f"Can't decode {i}")
