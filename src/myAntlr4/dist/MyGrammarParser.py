# Generated from MyGrammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from src.instruction.instruction import Instruction
from src.instruction.register import Register



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\64\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6I\n\6\3\6\2\2\7\2\4\6\b\n\2\5")
        buf.write("\3\2\5\6\3\2\7\b\3\2\17\20\2J\2\f\3\2\2\2\4\30\3\2\2\2")
        buf.write("\6\63\3\2\2\2\b\65\3\2\2\2\nH\3\2\2\2\f\r\5\4\3\2\r\16")
        buf.write("\7\2\2\3\16\17\b\2\1\2\17\3\3\2\2\2\20\21\5\6\4\2\21\22")
        buf.write("\7\26\2\2\22\23\5\4\3\2\23\24\b\3\1\2\24\31\3\2\2\2\25")
        buf.write("\26\5\6\4\2\26\27\b\3\1\2\27\31\3\2\2\2\30\20\3\2\2\2")
        buf.write("\30\25\3\2\2\2\31\5\3\2\2\2\32\33\7\24\2\2\33\34\7\3\2")
        buf.write("\2\34\35\7\r\2\2\35\64\b\4\1\2\36\37\7\25\2\2\37 \7\3")
        buf.write("\2\2 !\7\r\2\2!\64\b\4\1\2\"#\7\3\2\2#$\7\r\2\2$%\7\4")
        buf.write("\2\2%&\7\3\2\2&\'\7\r\2\2\'(\t\2\2\2()\7\r\2\2)\64\b\4")
        buf.write("\1\2*+\t\3\2\2+,\7\3\2\2,-\7\r\2\2-.\7\t\2\2./\7\r\2\2")
        buf.write("/\60\7\16\2\2\60\61\t\4\2\2\61\62\7\r\2\2\62\64\b\4\1")
        buf.write("\2\63\32\3\2\2\2\63\36\3\2\2\2\63\"\3\2\2\2\63*\3\2\2")
        buf.write("\2\64\7\3\2\2\2\65\66\7\21\2\2\66\67\7\23\2\2\678\7\n")
        buf.write("\2\289\5\n\6\29:\5\4\3\2:;\7\22\2\2;<\7\23\2\2<=\7\13")
        buf.write("\2\2=>\b\5\1\2>\t\3\2\2\2?@\7\3\2\2@A\7\r\2\2AB\7\f\2")
        buf.write("\2BC\5\n\6\2CD\b\6\1\2DI\3\2\2\2EF\7\3\2\2FG\7\r\2\2G")
        buf.write("I\b\6\1\2H?\3\2\2\2HE\3\2\2\2I\13\3\2\2\2\5\30\63H")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'R'", "'='", "'+'", "'-'", "'IF'", "'if'", 
                     "'!='", "'name'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "THEN",
                      "GOTOB", "GOTOF", "BEGIN", "END", "MACRO", "PUSH",
                      "POP", "NEWLINE", "WHITESPACE" ]

    RULE_program = 0
    RULE_code = 1
    RULE_expr = 2
    RULE_macro = 3
    RULE_list_register = 4

    ruleNames =  [ "program", "code", "expr", "macro", "list_register" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    INT=11
    THEN=12
    GOTOB=13
    GOTOF=14
    BEGIN=15
    END=16
    MACRO=17
    PUSH=18
    POP=19
    NEWLINE=20
    WHITESPACE=21

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
            self.state = 10
            localctx._code = self.code()
            self.state = 11
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
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                localctx._expr = self.expr()
                self.state = 15
                self.match(MyGrammarParser.NEWLINE)
                self.state = 16
                localctx._code = self.code()
                localctx.instruction =localctx._expr.instruction
                localctx.instruction.setNext(localctx._code.instruction)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
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

        def PUSH(self):
            return self.getToken(MyGrammarParser.PUSH, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.INT)
            else:
                return self.getToken(MyGrammarParser.INT, i)

        def POP(self):
            return self.getToken(MyGrammarParser.POP, 0)

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
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammarParser.PUSH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(MyGrammarParser.PUSH)
                self.state = 25
                self.match(MyGrammarParser.T__0)
                self.state = 26
                localctx.r1 = self.match(MyGrammarParser.INT)
                localctx.instruction= Instruction(5, (None if localctx.r1 is None else localctx.r1.text))
                pass
            elif token in [MyGrammarParser.POP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(MyGrammarParser.POP)
                self.state = 29
                self.match(MyGrammarParser.T__0)
                self.state = 30
                localctx.r1 = self.match(MyGrammarParser.INT)
                localctx.instruction= Instruction(6, (None if localctx.r1 is None else localctx.r1.text))
                pass
            elif token in [MyGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(MyGrammarParser.T__0)
                self.state = 33
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 34
                self.match(MyGrammarParser.T__1)
                self.state = 35
                self.match(MyGrammarParser.T__0)
                self.state = 36
                localctx.r2 = self.match(MyGrammarParser.INT)
                self.state = 37
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.T__2 or _la==MyGrammarParser.T__3):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 38
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
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.T__4 or _la==MyGrammarParser.T__5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.match(MyGrammarParser.T__0)
                self.state = 42
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 43
                self.match(MyGrammarParser.T__6)
                self.state = 44
                localctx.zero = self.match(MyGrammarParser.INT)
                self.state = 45
                self.match(MyGrammarParser.THEN)
                self.state = 46
                localctx.goto = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.GOTOB or _la==MyGrammarParser.GOTOF):
                    localctx.goto = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
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


    class MacroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.instruction = None
            self.name = None # Token
            self._code = None # CodeContext

        def BEGIN(self):
            return self.getToken(MyGrammarParser.BEGIN, 0)

        def MACRO(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.MACRO)
            else:
                return self.getToken(MyGrammarParser.MACRO, i)

        def list_register(self):
            return self.getTypedRuleContext(MyGrammarParser.List_registerContext,0)


        def code(self):
            return self.getTypedRuleContext(MyGrammarParser.CodeContext,0)


        def END(self):
            return self.getToken(MyGrammarParser.END, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_macro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro" ):
                listener.enterMacro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro" ):
                listener.exitMacro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro" ):
                return visitor.visitMacro(self)
            else:
                return visitor.visitChildren(self)




    def macro(self):

        localctx = MyGrammarParser.MacroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_macro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MyGrammarParser.BEGIN)
            self.state = 52
            self.match(MyGrammarParser.MACRO)
            self.state = 53
            localctx.name = self.match(MyGrammarParser.T__7)
            self.state = 54
            self.list_register()
            self.state = 55
            localctx._code = self.code()
            self.state = 56
            self.match(MyGrammarParser.END)
            self.state = 57
            self.match(MyGrammarParser.MACRO)
            self.state = 58
            self.match(MyGrammarParser.T__8)
            localctx.instruction=Macro((None if localctx.name is None else localctx.name.text), list_register.register, localctx._code.instruction)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_registerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.register = None
            self.r1 = None # Token
            self._list_register = None # List_registerContext

        def list_register(self):
            return self.getTypedRuleContext(MyGrammarParser.List_registerContext,0)


        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_list_register

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_register" ):
                listener.enterList_register(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_register" ):
                listener.exitList_register(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_register" ):
                return visitor.visitList_register(self)
            else:
                return visitor.visitChildren(self)




    def list_register(self):

        localctx = MyGrammarParser.List_registerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list_register)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(MyGrammarParser.T__0)
                self.state = 62
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 63
                self.match(MyGrammarParser.T__9)
                self.state = 64
                localctx._list_register = self.list_register()
                localctx.register=Register((None if localctx.r1 is None else localctx.r1.text), localctx._list_register.register)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(MyGrammarParser.T__0)
                self.state = 68
                localctx.r1 = self.match(MyGrammarParser.INT)
                localctx.register=Register((None if localctx.r1 is None else localctx.r1.text))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





