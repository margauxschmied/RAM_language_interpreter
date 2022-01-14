# Generated from MyGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

from src.instruction.instruction import Instruction
from src.instruction.register import Register



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


    # Visit a parse tree produced by MyGrammarParser#list_register.
    def visitList_register(self, ctx:MyGrammarParser.List_registerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#macro.
    def visitMacro(self, ctx:MyGrammarParser.MacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#macro_list_register.
    def visitMacro_list_register(self, ctx:MyGrammarParser.Macro_list_registerContext):
        return self.visitChildren(ctx)



del MyGrammarParser