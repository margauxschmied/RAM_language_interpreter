# Generated from MyGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#program.
    def enterProgram(self, ctx:MyGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#program.
    def exitProgram(self, ctx:MyGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#code.
    def enterCode(self, ctx:MyGrammarParser.CodeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#code.
    def exitCode(self, ctx:MyGrammarParser.CodeContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#ZeroUn.
    def enterZeroUn(self, ctx:MyGrammarParser.ZeroUnContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#ZeroUn.
    def exitZeroUn(self, ctx:MyGrammarParser.ZeroUnContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#DeuxTrois.
    def enterDeuxTrois(self, ctx:MyGrammarParser.DeuxTroisContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#DeuxTrois.
    def exitDeuxTrois(self, ctx:MyGrammarParser.DeuxTroisContext):
        pass



del MyGrammarParser