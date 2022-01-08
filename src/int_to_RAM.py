from typing import List
from cantor_int import Int


def int_to_RAM(n: int):
    """
        Gödelisation :
        - ADD = Rk = Rk + 1 (n = 3 * k)
        - SUB = Rk = Rk - 1 (n = 3 * k + 1)
        - IFF = IF Rk != 0 THEN GOTOF n (n = 3 <k, <1, <n, 0>>> + 2)
        - IFB = IF Rk != 0 THEN GOTOB n (n = 3 <k, <0, <n, 0>>> + 2)
    """
    n = Int(n)
    res: List[str] = []
    cantor_couple = n.int_to_couple()
    while cantor_couple[1] != 0:
        current = Int(cantor_couple[0])
        if current % 3 < 2:
            current = current / 3
            res.append(
                'R{} = R{} {} 1'.format(current.left(), current.left(), ['+', '-'][current % 3 == 1]))
        else:
            current = current / 3
            k = current.left()
            op = current.right().left()
            saut = current.right().right()
            inst = ('F', 'B')
            res.append(f'if R{k}!=0 THEN GOTO{inst[op%2==0]} {saut}')
        cantor_couple = cantor_couple[1]
    return '\n'.join(res)


if __name__ == '__main__':
    # for i in range(1, 42):
    #     print(i)
    #     print(int_to_RAM(i))
    #     print()
    print(int_to_RAM(100254825))
