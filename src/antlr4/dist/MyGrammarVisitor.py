# Generated from MyGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

from src.instruction import Instruction


# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#MakeList.
    def visitMakeList(self, ctx:MyGrammarParser.MakeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#code.
    def visitCode(self, ctx:MyGrammarParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#expr.
    def visitExpr(self, ctx:MyGrammarParser.ExprContext):
        return self.visitChildren(ctx)



del MyGrammarParser