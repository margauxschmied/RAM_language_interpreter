import sys


import antlr4
from antlr4 import *


# https://faun.pub/introduction-to-antlr-python-af8a3c603d23
from src.antlr4.dist.MyGrammarLexer import MyGrammarLexer
from src.antlr4.dist.MyGrammarParser import MyGrammarParser
from src.antlr4.dist.MyGrammarVisitor import MyGrammarVisitor


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
    data = InputStream(
         """R2 = R2 + 1
R2 = R2 - 1
if R2!=0 THEN GOTOB 0
R0 = R0 - 1"""
    )
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

