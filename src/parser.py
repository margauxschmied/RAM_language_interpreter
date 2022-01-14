# https://faun.pub/introduction-to-antlr-python-af8a3c603d23
from antlr4 import *

# try:
#     from src.antlr4.dist.MyGrammarLexer import MyGrammarLexer
#     from src.antlr4.dist.MyGrammarParser import MyGrammarParser
#     from src.antlr4.dist.MyGrammarVisitor import MyGrammarVisitor
# except:
#     from antlr4.dist.MyGrammarLexer import MyGrammarLexer
#     from antlr4.dist.MyGrammarParser import MyGrammarParser
#     from antlr4.dist.MyGrammarVisitor import MyGrammarVisitor
from src.Antlr4.dist.MyGrammarLexer import MyGrammarLexer
from src.Antlr4.dist.MyGrammarParser import MyGrammarParser
from src.Antlr4.dist.MyGrammarVisitor import MyGrammarVisitor


class MyVisitor(MyGrammarVisitor):

    def visitMakeList(self, ctx):
        current_instruction = ctx.instruction
        instructions = [current_instruction]

        while current_instruction is not None and current_instruction.getNext() is not None:
            current_instruction = current_instruction.getNext()
            instructions.append(current_instruction)

        return instructions


def listInstruction(expr):
    instructions = []
    current_instruction = None
    for child in expr.getChildren():
        if not isinstance(child, TerminalNode):
            current_instruction = child.instruction
            instructions.append(current_instruction)

    while current_instruction is not None and current_instruction.getNext() is not None:
        current_instruction = current_instruction.getNext()
        instructions.append(current_instruction)

    return instructions


if __name__ == "__main__":
#     data = InputStream(
#         """R2 = R2 + 1
# R2 = R2 - 1
# if R2!=0 THEN GOTOB 0
# R0 = R0 - 1"""
#     )

    data = InputStream("""BEGIN MACRO name(Rx, Ry)
    R1 = R1 + 1
    R1 = R1 + 1
    R1 = R1 - 1
    IF R1 != 0 THEN GOTOB 2
    R1 = R1 - 1
    END MACRO;""")

    # print(data)
    # lexer
    lexer = MyGrammarLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = MyGrammarParser(stream)
    tree = parser.program()
    # evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)
    # listInstruction(tree)
    print(output)
