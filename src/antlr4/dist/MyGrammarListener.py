# Generated from MyGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

from src.instruction import Instruction


# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#MakeList.
    def enterMakeList(self, ctx:MyGrammarParser.MakeListContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#MakeList.
    def exitMakeList(self, ctx:MyGrammarParser.MakeListContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#code.
    def enterCode(self, ctx:MyGrammarParser.CodeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#code.
    def exitCode(self, ctx:MyGrammarParser.CodeContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#expr.
    def enterExpr(self, ctx:MyGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#expr.
    def exitExpr(self, ctx:MyGrammarParser.ExprContext):
        pass



del MyGrammarParser