from typing import List
from cantor_int import Int


def decode_int_instr(n: int):
    """
        Gödelisation :
        - ADD = Rk = Rk + 1 (n = 3 * k)
        - SUB = Rk = Rk - 1 (n = 3 * k + 1)
        - IFF = IF Rk != 0 THEN GOTOF n (n = 3 <k, <0, <n, 0>>> + 2)
        - IFB = IF Rk != 0 THEN GOTOB n (n = 3 <k, <1, <n, 0>>> + 2)
    """
    res: List[str] = []
    n = Int(n)
    if n % 3 < 2:
        current = n / 3
        res.append(
            'R{} = R{} {} 1'.format(current, current, ['+', '-'][n % 3 == 1]))
    else:
        current = Int(n // 3)
        # By default we 'think we have a `minimal jump`
        # current.right = 0 since 0 is not decodable
        k = 0
        type_saut = 0
        saut = 0
        rpart = Int(0)
        if current != 0 and current.right() != 0:
            k = current.left()
            rpart = current.right()
            type_saut = rpart.left()
            saut = rpart.right()
        inst = ('F', 'B')
        res.append(f'if R{k}!=0 THEN GOTO{inst[type_saut!=1]} {saut}')
    return '\n'.join(res)


def decode_int_program(inp):
    """
        If n is an int it is converted to the Cantor's couple
        Else n is on the form <a1, ... <an, 0>>>
        The program transform every instr to a RAM instr 
        thanks to decode_int_instr function
    """
    n = Int(inp).int_to_couple() if type(inp) == int else inp
    program = []
    while True:
        try:
            program.append(decode_int_instr(n[0]))
            n = n[1]
            if n == 0:
                break
        except Exception as e:
            raise
    return "\n".join(program)


if __name__ == '__main__':
    decode_int_program(83)
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
