import sys
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor

# https://faun.pub/introduction-to-antlr-python-af8a3c603d23


def get_username():
    from pwd import getpwuid
    from os import getuid

    return getpwuid(getuid())[0]


class MyVisitor(MyGrammarVisitor):
    def visitCoucou(self, ctx):
        print(ctx.r1.text)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())


if __name__ == "__main__":
    # while 1:
    data = InputStream(
        """R2 = R2 + 1
R2 = R2 - 1
if R2!=2 THEN GOTOB 0
R0 = R0 - 1"""
    )
    print(data)
    # lexer
    lexer = MyGrammarLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = MyGrammarParser(stream)
    tree = parser.program()
    # evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)
    print(output)
