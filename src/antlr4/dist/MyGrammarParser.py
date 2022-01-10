# Generated from MyGrammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from src.instruction import Instruction


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\25\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4(\n")
        buf.write("\4\3\4\2\2\5\2\4\6\2\5\3\2\5\6\3\2\7\b\3\2\f\r\2(\2\b")
        buf.write("\3\2\2\2\4\24\3\2\2\2\6\'\3\2\2\2\b\t\5\4\3\2\t\n\7\2")
        buf.write("\2\3\n\13\b\2\1\2\13\3\3\2\2\2\f\r\5\6\4\2\r\16\7\16\2")
        buf.write("\2\16\17\5\4\3\2\17\20\b\3\1\2\20\25\3\2\2\2\21\22\5\6")
        buf.write("\4\2\22\23\b\3\1\2\23\25\3\2\2\2\24\f\3\2\2\2\24\21\3")
        buf.write("\2\2\2\25\5\3\2\2\2\26\27\7\3\2\2\27\30\7\n\2\2\30\31")
        buf.write("\7\4\2\2\31\32\7\3\2\2\32\33\7\n\2\2\33\34\t\2\2\2\34")
        buf.write("\35\7\n\2\2\35(\b\4\1\2\36\37\t\3\2\2\37 \7\3\2\2 !\7")
        buf.write("\n\2\2!\"\7\t\2\2\"#\7\n\2\2#$\7\13\2\2$%\t\4\2\2%&\7")
        buf.write("\n\2\2&(\b\4\1\2\'\26\3\2\2\2\'\36\3\2\2\2(\7\3\2\2\2")
        buf.write("\4\24\'")
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
            self.instruction = None


        def getRuleIndex(self):
            return MyGrammarParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.instruction = ctx.instruction



    class MakeListContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ProgramContext
            super().__init__(parser)
            self._code = None # CodeContext
            self.copyFrom(ctx)

        def code(self):
            return self.getTypedRuleContext(MyGrammarParser.CodeContext,0)

        def EOF(self):
            return self.getToken(MyGrammarParser.EOF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMakeList" ):
                listener.enterMakeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMakeList" ):
                listener.exitMakeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMakeList" ):
                return visitor.visitMakeList(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = MyGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            localctx = MyGrammarParser.MakeListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            localctx._code = self.code()
            self.state = 7
            self.match(MyGrammarParser.EOF)
            localctx.instruction=localctx._code.instruction
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
            self.instruction = None
            self._expr = None # ExprContext
            self._code = None # CodeContext

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(MyGrammarParser.NEWLINE, 0)

        def code(self):
            return self.getTypedRuleContext(MyGrammarParser.CodeContext,0)


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
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                localctx._expr = self.expr()
                self.state = 11
                self.match(MyGrammarParser.NEWLINE)
                self.state = 12
                localctx._code = self.code()
                localctx.instruction =localctx._expr.instruction
                localctx.instruction.setNext(localctx._code.instruction)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                localctx._expr = self.expr()
                localctx.instruction =localctx._expr.instruction
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
            self.instruction = None
            self.r1 = None # Token
            self.r2 = None # Token
            self.op = None # Token
            self.un = None # Token
            self.zero = None # Token
            self.goto = None # Token
            self.n = None # Token

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.INT)
            else:
                return self.getToken(MyGrammarParser.INT, i)

        def THEN(self):
            return self.getToken(MyGrammarParser.THEN, 0)

        def GOTOB(self):
            return self.getToken(MyGrammarParser.GOTOB, 0)

        def GOTOF(self):
            return self.getToken(MyGrammarParser.GOTOF, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MyGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(MyGrammarParser.T__0)
                self.state = 21
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 22
                self.match(MyGrammarParser.T__1)
                self.state = 23
                self.match(MyGrammarParser.T__0)
                self.state = 24
                localctx.r2 = self.match(MyGrammarParser.INT)
                self.state = 25
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.T__2 or _la==MyGrammarParser.T__3):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 26
                localctx.un = self.match(MyGrammarParser.INT)

                if (None if localctx.r1 is None else localctx.r1.text) != (None if localctx.r2 is None else localctx.r2.text):
                    raise ValueError("line "+str((0 if localctx.r1 is None else localctx.r1.line))+": R"+(None if localctx.r1 is None else localctx.r1.text)+" != "+"R"+(None if localctx.r2 is None else localctx.r2.text))
                if (None if localctx.un is None else localctx.un.text) != '1':
                    raise ValueError("line "+str((0 if localctx.un is None else localctx.un.line))+": "+(None if localctx.un is None else localctx.un.text)+" != 1")
                if (None if localctx.op is None else localctx.op.text)=='+':
                    localctx.instruction= Instruction(0, (None if localctx.r1 is None else localctx.r1.text))
                else:
                    localctx.instruction= Instruction(1, (None if localctx.r1 is None else localctx.r1.text))

                pass
            elif token in [MyGrammarParser.T__4, MyGrammarParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.T__4 or _la==MyGrammarParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self.match(MyGrammarParser.T__0)
                self.state = 30
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 31
                self.match(MyGrammarParser.T__6)
                self.state = 32
                localctx.zero = self.match(MyGrammarParser.INT)
                self.state = 33
                self.match(MyGrammarParser.THEN)
                self.state = 34
                localctx.goto = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.GOTOB or _la==MyGrammarParser.GOTOF):
                    localctx.goto = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                localctx.n = self.match(MyGrammarParser.INT)

                if (None if localctx.zero is None else localctx.zero.text) != '0':
                    raise ValueError("line "+str((0 if localctx.zero is None else localctx.zero.line))+": "+(None if localctx.zero is None else localctx.zero.text)+" != 0")
                if (None if localctx.goto is None else localctx.goto.text)=='GOTOB' or (None if localctx.goto is None else localctx.goto.text)=='gotob':
                    localctx.instruction= Instruction(2, (None if localctx.r1 is None else localctx.r1.text), (None if localctx.n is None else localctx.n.text))
                else:
                    localctx.instruction= Instruction(3, (None if localctx.r1 is None else localctx.r1.text), (None if localctx.n is None else localctx.n.text))

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





