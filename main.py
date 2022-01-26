import src.GUI.interface as interface
from src.interpreter.cantor_int import *
from src.interpreter.instruction import *
from src.interpreter.decode_int import *
from src.interpreter.interpreter import *
from src.parser.parser import myLex, myYacc, macros
from src.pars_to_interp import *
from src.help_panel import *
from src.ram_instructions import *
from src.ram_instructions.ram_instr import open_ram_instr
from src.about.about import open_about


if __name__ == '__main__':
    interface.run_GUI()

    RAM_inst = (
        """begin macro id(Rx, Ry)
        Rx=Rx + 1
        Rx=Rx - 1
        R1000=R1000 + 1
        IF Rx != 0 then gotob 2
        R1000=R1000 - 1
        Rx=Rx + 1
        Ry=Ry + 1
        IF R1000 != 0 then gotob 3
        Rx=Rx - 1
        Ry=Ry - 1
        end macro;
        begin macro add(Rx, Ry)
        id(Rx, R100)
        R100=R100 + 1
        Ry=Ry + 1
        R100=R100 - 1
        IF R100 != 0 then gotob 2
        Ry=Ry - 1
        end macro;
        begin macro add_in_z(Rx, Ry, Rz)
        id(Rx, R100)
        id(Ry, Rz)
        R100=R100 + 1
        R100=R100 - 1
        Rz=Rz + 1
        IF R100 != 0 then gotob 2
        Rz=Rz - 1
        end macro;
        begin macro clear(Rx)
        Rx=Rx - 1
        IF Rx != 0 then gotob 1
        end macro;
        begin macro sum_0_to_n(Rx)
        Rx=Rx + 1
        Rx=Rx - 1
        add(Rx, R1)
        IF Rx != 0 then gotob 2
        end macro;
        sum_0_to_n(R0)"""
    )

    lexer = myLex()
    lexer.input(RAM_inst)

    parser = myYacc()

    result = parser.parse(RAM_inst)

    interp = make_interpreter(result)
    N = 50
    interp.reset(N)
    print(
        f"Mesdames et messieurs, la somme de 0 à {N} is {interp.treat_all_instr()[1]}")

#     data = InputStream("""R0 = R0 + 1
# R0 = R0 - 1
# R0 = R0 + 1
# R0 = R0 - 1
# R1000 = R1000 + 1
# IF R0 != 0 then gotob 2
# R1000 = R1000 - 1
# R0 = R0 + 1
# R100 = R100 + 1
# IF R1000 != 0 then gotob 3
# R0 = R0 - 1
# R100 = R100 - 1
# R100 = R100 + 1
# R1 = R1 + 1
# R100 = R100 - 1
# IF R100 != 0 then gotob 2
# R1 = R1 - 1
# IF R0 != 0 then gotob 16
# """)

# # lexer
# lexer = MyGrammarLexer(data)
# stream = CommonTokenStream(lexer)
#
# # parser
# parser = MyGrammarParser(stream)
# tree = parser.program()
#
# # evaluator
# visitor = MyVisitor()
# output = visitor.visit(tree)
#
# l_inst = listInstruction(tree)
#
# print(f"\n  List instr after parsing \n{l_inst}")
#
# print(f"\n  Program to int instr \n{decode_int_program(l_inst)}")
#
# # interpreter
# interp = Interpreter(l_inst, memory=RAM(N))
# interp.treat_all_instr()
# print("\n  Program output =", interp.get_output())
