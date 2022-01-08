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


if __name__ == '__main__':
    # for i in range(1, 42):
    #     print(i)
    #     print(int_to_RAM(i))
    #     print()
    L = [1002500825, 2, 5, 8, 11]
    for elt in L:
        print(f"Decoding {elt}:")
        try:
            print(int_to_RAM(elt))
        except Exception as e:
            print(e)
