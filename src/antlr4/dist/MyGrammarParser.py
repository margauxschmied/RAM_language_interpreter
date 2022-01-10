# Generated from MyGrammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n\4\3\4\2")
        buf.write("\2\5\2\4\6\2\5\3\2\5\6\3\2\7\b\3\2\f\r\2&\2\b\3\2\2\2")
        buf.write("\4\23\3\2\2\2\6%\3\2\2\2\b\t\5\4\3\2\t\n\7\2\2\3\n\3\3")
        buf.write("\2\2\2\13\f\5\6\4\2\f\r\7\16\2\2\r\16\5\2\2\2\16\17\b")
        buf.write("\3\1\2\17\24\3\2\2\2\20\21\5\6\4\2\21\22\b\3\1\2\22\24")
        buf.write("\3\2\2\2\23\13\3\2\2\2\23\20\3\2\2\2\24\5\3\2\2\2\25\26")
        buf.write("\7\3\2\2\26\27\7\n\2\2\27\30\7\4\2\2\30\31\7\3\2\2\31")
        buf.write("\32\7\n\2\2\32\33\t\2\2\2\33\34\7\n\2\2\34&\b\4\1\2\35")
        buf.write("\36\t\3\2\2\36\37\7\3\2\2\37 \7\n\2\2 !\7\t\2\2!\"\7\n")
        buf.write("\2\2\"#\7\13\2\2#$\t\4\2\2$&\7\n\2\2%\25\3\2\2\2%\35\3")
        buf.write("\2\2\2&\7\3\2\2\2\4\23%")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'R'", "'='", "'+'", "'-'", "'IF'", "'if'", 
                     "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "THEN", "GOTOB", "GOTOF", "NEWLINE", "WHITESPACE" ]

    RULE_program = 0
    RULE_code = 1
    RULE_expr = 2

    ruleNames =  [ "program", "code", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INT=8
    THEN=9
    GOTOB=10
    GOTOF=11
    NEWLINE=12
    WHITESPACE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code(self):
            return self.getTypedRuleContext(MyGrammarParser.CodeContext,0)


        def EOF(self):
            return self.getToken(MyGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.code()
            self.state = 7
            self.match(MyGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(MyGrammarParser.NEWLINE, 0)

        def program(self):
            return self.getTypedRuleContext(MyGrammarParser.ProgramContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode" ):
                listener.enterCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode" ):
                listener.exitCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = MyGrammarParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_code)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self.expr()
                self.state = 10
                self.match(MyGrammarParser.NEWLINE)
                self.state = 11
                self.program()

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.expr()

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CoucouContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.r1 = None # Token
            self.r2 = None # Token
            self.op = None # Token
            self.un = None # Token
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.INT)
            else:
                return self.getToken(MyGrammarParser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoucou" ):
                listener.enterCoucou(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoucou" ):
                listener.exitCoucou(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoucou" ):
                return visitor.visitCoucou(self)
            else:
                return visitor.visitChildren(self)


    class PommeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.r1 = None # Token
            self.zero = None # Token
            self.goto = None # Token
            self.n = None # Token
            self.copyFrom(ctx)

        def THEN(self):
            return self.getToken(MyGrammarParser.THEN, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.INT)
            else:
                return self.getToken(MyGrammarParser.INT, i)
        def GOTOB(self):
            return self.getToken(MyGrammarParser.GOTOB, 0)
        def GOTOF(self):
            return self.getToken(MyGrammarParser.GOTOF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPomme" ):
                listener.enterPomme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPomme" ):
                listener.exitPomme(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPomme" ):
                return visitor.visitPomme(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = MyGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammarParser.T__0]:
                localctx = MyGrammarParser.CoucouContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(MyGrammarParser.T__0)
                self.state = 20
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 21
                self.match(MyGrammarParser.T__1)
                self.state = 22
                self.match(MyGrammarParser.T__0)
                self.state = 23
                localctx.r2 = self.match(MyGrammarParser.INT)
                self.state = 24
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.T__2 or _la==MyGrammarParser.T__3):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 25
                localctx.un = self.match(MyGrammarParser.INT)

                pass
            elif token in [MyGrammarParser.T__4, MyGrammarParser.T__5]:
                localctx = MyGrammarParser.PommeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.T__4 or _la==MyGrammarParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 28
                self.match(MyGrammarParser.T__0)
                self.state = 29
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 30
                self.match(MyGrammarParser.T__6)
                self.state = 31
                localctx.zero = self.match(MyGrammarParser.INT)
                self.state = 32
                self.match(MyGrammarParser.THEN)
                self.state = 33
                localctx.goto = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.GOTOB or _la==MyGrammarParser.GOTOF):
                    localctx.goto = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 34
                localctx.n = self.match(MyGrammarParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





