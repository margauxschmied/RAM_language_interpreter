# Generated from MyGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\t\6\t\60\n\t\r\t\16\t\61\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n<\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13H\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fT\n\f\3\r\5\rW\n\r\3\r")
        buf.write("\3\r\6\r[\n\r\r\r\16\r\\\3\16\6\16`\n\16\r\16\16\16a\3")
        buf.write("\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\3\2\4\3\2\62;\5\2\13\f\16\17")
        buf.write("\"\"\2l\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3")
        buf.write("\2\2\2\13%\3\2\2\2\r(\3\2\2\2\17+\3\2\2\2\21/\3\2\2\2")
        buf.write("\23;\3\2\2\2\25G\3\2\2\2\27S\3\2\2\2\31Z\3\2\2\2\33_\3")
        buf.write("\2\2\2\35\36\7T\2\2\36\4\3\2\2\2\37 \7?\2\2 \6\3\2\2\2")
        buf.write("!\"\7-\2\2\"\b\3\2\2\2#$\7/\2\2$\n\3\2\2\2%&\7K\2\2&\'")
        buf.write("\7H\2\2\'\f\3\2\2\2()\7k\2\2)*\7h\2\2*\16\3\2\2\2+,\7")
        buf.write("#\2\2,-\7?\2\2-\20\3\2\2\2.\60\t\2\2\2/.\3\2\2\2\60\61")
        buf.write("\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\22\3\2\2\2\63\64")
        buf.write("\7V\2\2\64\65\7J\2\2\65\66\7G\2\2\66<\7P\2\2\678\7v\2")
        buf.write("\289\7j\2\29:\7g\2\2:<\7p\2\2;\63\3\2\2\2;\67\3\2\2\2")
        buf.write("<\24\3\2\2\2=>\7I\2\2>?\7Q\2\2?@\7V\2\2@A\7Q\2\2AH\7D")
        buf.write("\2\2BC\7i\2\2CD\7q\2\2DE\7v\2\2EF\7q\2\2FH\7d\2\2G=\3")
        buf.write("\2\2\2GB\3\2\2\2H\26\3\2\2\2IJ\7I\2\2JK\7Q\2\2KL\7V\2")
        buf.write("\2LM\7Q\2\2MT\7H\2\2NO\7i\2\2OP\7q\2\2PQ\7v\2\2QR\7q\2")
        buf.write("\2RT\7h\2\2SI\3\2\2\2SN\3\2\2\2T\30\3\2\2\2UW\7\17\2\2")
        buf.write("VU\3\2\2\2VW\3\2\2\2WX\3\2\2\2X[\7\f\2\2Y[\7\17\2\2ZV")
        buf.write("\3\2\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\32")
        buf.write("\3\2\2\2^`\t\3\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2")
        buf.write("\2\2bc\3\2\2\2cd\b\16\2\2d\34\3\2\2\2\13\2\61;GSVZ\\a")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    INT = 8
    THEN = 9
    GOTOB = 10
    GOTOF = 11
    NEWLINE = 12
    WHITESPACE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'R'", "'='", "'+'", "'-'", "'IF'", "'if'", "'!='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "THEN", "GOTOB", "GOTOF", "NEWLINE", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "INT", "THEN", "GOTOB", "GOTOF", "NEWLINE", "WHITESPACE" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


