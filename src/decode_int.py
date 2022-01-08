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
    """
        If n is an int it is converted to the Cantor's couple
        Else n is on the form <a1, ... <an, 0>>>
        The program transform every instr to a RAM instr 
        thanks to decode_int_instr function
    """
    if type(n) == int:
        n = Int(n).int_to_couple()
    program = []
    while True:
        program.append(decode_int_instr(n[0]))
        n = n[1]
        if n == 0:
            break
    return "\n".join(program)


if __name__ == '__main__':
    for i in range(21):
        try:
            print(f"Decoding instruction {i} :")
            print(decode_int_instr(i))
        except:
            print(f"Can't decode {i}")
    print("-"*40)
    for i in range(100):
        try:
            print(f"Decoding program {i} :")
            print(decode_int_program(i))
        except Exception as e:
            print(f"Can't decode {i} because there is {e}")
