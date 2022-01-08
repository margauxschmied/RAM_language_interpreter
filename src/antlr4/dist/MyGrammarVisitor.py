# Generated from MyGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#program.
    def visitProgram(self, ctx:MyGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#code.
    def visitCode(self, ctx:MyGrammarParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#ZeroUn.
    def visitZeroUn(self, ctx:MyGrammarParser.ZeroUnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#DeuxTrois.
    def visitDeuxTrois(self, ctx:MyGrammarParser.DeuxTroisContext):
        return self.visitChildren(ctx)



del MyGrammarParser