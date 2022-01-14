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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\33\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\49\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5D\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7Z\n\7\3\7\2\2\b")
        buf.write("\2\4\6\b\n\f\2\4\3\2\4\5\3\2\16\17\2\\\2\16\3\2\2\2\4")
        buf.write("\32\3\2\2\2\68\3\2\2\2\bC\3\2\2\2\nE\3\2\2\2\fY\3\2\2")
        buf.write("\2\16\17\5\4\3\2\17\20\7\2\2\3\20\21\b\2\1\2\21\3\3\2")
        buf.write("\2\2\22\23\5\6\4\2\23\24\7\27\2\2\24\25\5\4\3\2\25\26")
        buf.write("\b\3\1\2\26\33\3\2\2\2\27\30\5\6\4\2\30\31\b\3\1\2\31")
        buf.write("\33\3\2\2\2\32\22\3\2\2\2\32\27\3\2\2\2\33\5\3\2\2\2\34")
        buf.write("\35\5\n\6\2\35\36\b\4\1\2\369\3\2\2\2\37 \7\23\2\2 !\7")
        buf.write("\13\2\2!\"\7\n\2\2\"9\b\4\1\2#$\7\24\2\2$%\7\13\2\2%&")
        buf.write("\7\n\2\2&9\b\4\1\2\'(\7\13\2\2()\7\n\2\2)*\7\3\2\2*+\7")
        buf.write("\13\2\2+,\7\n\2\2,-\t\2\2\2-.\7\n\2\2.9\b\4\1\2/\60\7")
        buf.write("\f\2\2\60\61\7\13\2\2\61\62\7\n\2\2\62\63\7\6\2\2\63\64")
        buf.write("\7\n\2\2\64\65\7\r\2\2\65\66\t\3\2\2\66\67\7\n\2\2\67")
        buf.write("9\b\4\1\28\34\3\2\2\28\37\3\2\2\28#\3\2\2\28\'\3\2\2\2")
        buf.write("8/\3\2\2\29\7\3\2\2\2:;\7\13\2\2;<\7\n\2\2<=\7\7\2\2=")
        buf.write(">\5\b\5\2>?\b\5\1\2?D\3\2\2\2@A\7\13\2\2AB\7\n\2\2BD\b")
        buf.write("\5\1\2C:\3\2\2\2C@\3\2\2\2D\t\3\2\2\2EF\7\20\2\2FG\7\22")
        buf.write("\2\2GH\7\26\2\2HI\5\f\7\2IJ\7\b\2\2JK\7\27\2\2KL\5\4\3")
        buf.write("\2LM\7\27\2\2MN\7\21\2\2NO\7\22\2\2OP\7\t\2\2PQ\b\6\1")
        buf.write("\2Q\13\3\2\2\2RS\7\25\2\2ST\7\7\2\2TU\5\f\7\2UV\b\7\1")
        buf.write("\2VZ\3\2\2\2WX\7\25\2\2XZ\b\7\1\2YR\3\2\2\2YW\3\2\2\2")
        buf.write("Z\r\3\2\2\2\6\328CY")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'!='", "','", "')'", 
                     "';'", "<INVALID>", "'R'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "R", "IF", "THEN", "GOTOB", "GOTOF", "BEGIN", 
                      "END", "MACRO", "PUSH", "POP", "RIDENTIFIER", "MACROIDENTIFIER", 
                      "NEWLINE", "WHITESPACE" ]

    RULE_program = 0
    RULE_code = 1
    RULE_expr = 2
    RULE_list_register = 3
    RULE_macro = 4
    RULE_macro_list_register = 5

    ruleNames =  [ "program", "code", "expr", "list_register", "macro", 
                   "macro_list_register" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INT=8
    R=9
    IF=10
    THEN=11
    GOTOB=12
    GOTOF=13
    BEGIN=14
    END=15
    MACRO=16
    PUSH=17
    POP=18
    RIDENTIFIER=19
    MACROIDENTIFIER=20
    NEWLINE=21
    WHITESPACE=22

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
            self.state = 12
            localctx._code = self.code()
            self.state = 13
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
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                localctx._expr = self.expr()
                self.state = 17
                self.match(MyGrammarParser.NEWLINE)
                self.state = 18
                localctx._code = self.code()
                localctx.instruction =localctx._expr.instruction
                localctx.instruction.setNext(localctx._code.instruction)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
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
            self._macro = None # MacroContext
            self.r1 = None # Token
            self.r2 = None # Token
            self.op = None # Token
            self.un = None # Token
            self.zero = None # Token
            self.goto = None # Token
            self.n = None # Token

        def macro(self):
            return self.getTypedRuleContext(MyGrammarParser.MacroContext,0)


        def PUSH(self):
            return self.getToken(MyGrammarParser.PUSH, 0)

        def R(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.R)
            else:
                return self.getToken(MyGrammarParser.R, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.INT)
            else:
                return self.getToken(MyGrammarParser.INT, i)

        def POP(self):
            return self.getToken(MyGrammarParser.POP, 0)

        def IF(self):
            return self.getToken(MyGrammarParser.IF, 0)

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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammarParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                localctx._macro = self.macro()
                localctx.instruction=localctx._macro.instruction
                pass
            elif token in [MyGrammarParser.PUSH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(MyGrammarParser.PUSH)
                self.state = 30
                self.match(MyGrammarParser.R)
                self.state = 31
                localctx.r1 = self.match(MyGrammarParser.INT)
                localctx.instruction= Instruction(4, Register((None if localctx.r1 is None else localctx.r1.text)))
                pass
            elif token in [MyGrammarParser.POP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.match(MyGrammarParser.POP)
                self.state = 34
                self.match(MyGrammarParser.R)
                self.state = 35
                localctx.r1 = self.match(MyGrammarParser.INT)
                localctx.instruction= Instruction(5, Register((None if localctx.r1 is None else localctx.r1.text)))
                pass
            elif token in [MyGrammarParser.R]:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(MyGrammarParser.R)
                self.state = 38
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 39
                self.match(MyGrammarParser.T__0)
                self.state = 40
                self.match(MyGrammarParser.R)
                self.state = 41
                localctx.r2 = self.match(MyGrammarParser.INT)
                self.state = 42
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.T__1 or _la==MyGrammarParser.T__2):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 43
                localctx.un = self.match(MyGrammarParser.INT)

                if (None if localctx.r1 is None else localctx.r1.text) != (None if localctx.r2 is None else localctx.r2.text):
                    raise ValueError("line "+str((0 if localctx.r1 is None else localctx.r1.line))+": R"+(None if localctx.r1 is None else localctx.r1.text)+" != "+"R"+(None if localctx.r2 is None else localctx.r2.text))
                if (None if localctx.un is None else localctx.un.text) != '1':
                    raise ValueError("line "+str((0 if localctx.un is None else localctx.un.line))+": "+(None if localctx.un is None else localctx.un.text)+" != 1")
                if (None if localctx.op is None else localctx.op.text)=='+':
                    localctx.instruction= Instruction(0, Register((None if localctx.r1 is None else localctx.r1.text)))
                else:
                    localctx.instruction= Instruction(1, Register((None if localctx.r1 is None else localctx.r1.text)))

                pass
            elif token in [MyGrammarParser.IF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.match(MyGrammarParser.IF)
                self.state = 46
                self.match(MyGrammarParser.R)
                self.state = 47
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 48
                self.match(MyGrammarParser.T__3)
                self.state = 49
                localctx.zero = self.match(MyGrammarParser.INT)
                self.state = 50
                self.match(MyGrammarParser.THEN)
                self.state = 51
                localctx.goto = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MyGrammarParser.GOTOB or _la==MyGrammarParser.GOTOF):
                    localctx.goto = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                localctx.n = self.match(MyGrammarParser.INT)

                if (None if localctx.zero is None else localctx.zero.text) != '0':
                    raise ValueError("line "+str((0 if localctx.zero is None else localctx.zero.line))+": "+(None if localctx.zero is None else localctx.zero.text)+" != 0")
                if (None if localctx.goto is None else localctx.goto.text)=='GOTOB' or (None if localctx.goto is None else localctx.goto.text)=='gotob':
                    localctx.instruction= Instruction(2, Register((None if localctx.r1 is None else localctx.r1.text)), (None if localctx.n is None else localctx.n.text))
                else:
                    localctx.instruction= Instruction(3, Register((None if localctx.r1 is None else localctx.r1.text)), (None if localctx.n is None else localctx.n.text))

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


    class List_registerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.register = None
            self.r1 = None # Token
            self._list_register = None # List_registerContext

        def R(self):
            return self.getToken(MyGrammarParser.R, 0)

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
        self.enterRule(localctx, 6, self.RULE_list_register)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(MyGrammarParser.R)
                self.state = 57
                localctx.r1 = self.match(MyGrammarParser.INT)
                self.state = 58
                self.match(MyGrammarParser.T__4)
                self.state = 59
                localctx._list_register = self.list_register()
                localctx.register=Register((None if localctx.r1 is None else localctx.r1.text), localctx._list_register.register)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(MyGrammarParser.R)
                self.state = 63
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

        def macro_list_register(self):
            return self.getTypedRuleContext(MyGrammarParser.Macro_list_registerContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.NEWLINE)
            else:
                return self.getToken(MyGrammarParser.NEWLINE, i)

        def code(self):
            return self.getTypedRuleContext(MyGrammarParser.CodeContext,0)


        def END(self):
            return self.getToken(MyGrammarParser.END, 0)

        def MACROIDENTIFIER(self):
            return self.getToken(MyGrammarParser.MACROIDENTIFIER, 0)

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
        self.enterRule(localctx, 8, self.RULE_macro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(MyGrammarParser.BEGIN)
            self.state = 68
            self.match(MyGrammarParser.MACRO)
            self.state = 69
            localctx.name = self.match(MyGrammarParser.MACROIDENTIFIER)
            self.state = 70
            self.macro_list_register()
            self.state = 71
            self.match(MyGrammarParser.T__5)
            self.state = 72
            self.match(MyGrammarParser.NEWLINE)
            self.state = 73
            localctx._code = self.code()
            self.state = 74
            self.match(MyGrammarParser.NEWLINE)
            self.state = 75
            self.match(MyGrammarParser.END)
            self.state = 76
            self.match(MyGrammarParser.MACRO)
            self.state = 77
            self.match(MyGrammarParser.T__6)
            localctx.instruction=Macro((None if localctx.name is None else localctx.name.text), macro_list_register.register, localctx._code.instruction)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_list_registerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.register = None
            self.r1 = None # Token
            self._macro_list_register = None # Macro_list_registerContext

        def macro_list_register(self):
            return self.getTypedRuleContext(MyGrammarParser.Macro_list_registerContext,0)


        def RIDENTIFIER(self):
            return self.getToken(MyGrammarParser.RIDENTIFIER, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_macro_list_register

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_list_register" ):
                listener.enterMacro_list_register(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_list_register" ):
                listener.exitMacro_list_register(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_list_register" ):
                return visitor.visitMacro_list_register(self)
            else:
                return visitor.visitChildren(self)




    def macro_list_register(self):

        localctx = MyGrammarParser.Macro_list_registerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_macro_list_register)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                localctx.r1 = self.match(MyGrammarParser.RIDENTIFIER)
                self.state = 81
                self.match(MyGrammarParser.T__4)
                self.state = 82
                localctx._macro_list_register = self.macro_list_register()
                localctx.register=Register((None if localctx.r1 is None else localctx.r1.text), localctx._macro_list_register.register)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                localctx.r1 = self.match(MyGrammarParser.RIDENTIFIER)
                localctx.register=Register((None if localctx.r1 is None else localctx.r1.text))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





