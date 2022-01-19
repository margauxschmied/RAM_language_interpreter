from ply import lex
from ply import yacc

try:
    from src.interpreter.instruction import *
    from src.interpreter.interpreter import *
    from src.parser.parser import lex
except:
    from interpreter.instruction import *
    from interpreter.interpreter import *
    from parser.parser import lex


def list_intruction(list_instr):
    list = []
    dic = {}
    c_instr = list_instr
    while c_instr != None:
        if c_instr.is_macro:
            dic[c_instr.num_instr] = Macro(c_instr.num_instr,
                                           c_instr.register.list_register(),
                                           list_intruction(c_instr.instruction)[0])
        elif isinstance(c_instr.num_instr, str):
            list.append(RawInstruction(
                c_instr.num_instr,
                c_instr.register.list_register(),
                c_instr.n))
        else:
            list.append(
                RawInstruction(
                    c_instr.num_instr,
                    c_instr.register.register,
                    c_instr.n))
        c_instr = c_instr.next
    return list, dic


def make_interpreter(listr_instr):
    return Interpreter(*list_intruction(listr_instr))


if __name__ == '__main__':
    data = """begin MACRO a(Rx, Ry)
    Ry = Ry + 1
    R1 = R1 + 1
    Rx = Rx - 1
    IF Rx != 0 THEN GOTOB 2
    Rx = Rx - 1
    END MACRO;
    a(R1, R1)
"""

    lexer = lex.lex()
    lexer.input(data)

    parser = yacc.yacc()

    result = parser.parse(data)
