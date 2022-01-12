# Generated from MyGrammar.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\u00b0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\fI\n\f\r\f\16")
        buf.write("\fJ\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\rU\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16a\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("m\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\5\20y\n\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0081")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u008d\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u0097\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u009f\n\24\3\25\5\25\u00a2\n\25\3\25\3\25\6\25\u00a6")
        buf.write("\n\25\r\25\16\25\u00a7\3\26\6\26\u00ab\n\26\r\26\16\26")
        buf.write("\u00ac\3\26\3\26\2\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27\3\2\4\3\2\62;\5\2\13\f\16\17\"\"\2\u00bc")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2")
        buf.write("\5/\3\2\2\2\7\61\3\2\2\2\t\63\3\2\2\2\13\65\3\2\2\2\r")
        buf.write("8\3\2\2\2\17;\3\2\2\2\21>\3\2\2\2\23C\3\2\2\2\25E\3\2")
        buf.write("\2\2\27H\3\2\2\2\31T\3\2\2\2\33`\3\2\2\2\35l\3\2\2\2\37")
        buf.write("x\3\2\2\2!\u0080\3\2\2\2#\u008c\3\2\2\2%\u0096\3\2\2\2")
        buf.write("\'\u009e\3\2\2\2)\u00a5\3\2\2\2+\u00aa\3\2\2\2-.\7T\2")
        buf.write("\2.\4\3\2\2\2/\60\7?\2\2\60\6\3\2\2\2\61\62\7-\2\2\62")
        buf.write("\b\3\2\2\2\63\64\7/\2\2\64\n\3\2\2\2\65\66\7K\2\2\66\67")
        buf.write("\7H\2\2\67\f\3\2\2\289\7k\2\29:\7h\2\2:\16\3\2\2\2;<\7")
        buf.write("#\2\2<=\7?\2\2=\20\3\2\2\2>?\7p\2\2?@\7c\2\2@A\7o\2\2")
        buf.write("AB\7g\2\2B\22\3\2\2\2CD\7=\2\2D\24\3\2\2\2EF\7.\2\2F\26")
        buf.write("\3\2\2\2GI\t\2\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2")
        buf.write("\2\2K\30\3\2\2\2LM\7V\2\2MN\7J\2\2NO\7G\2\2OU\7P\2\2P")
        buf.write("Q\7v\2\2QR\7j\2\2RS\7g\2\2SU\7p\2\2TL\3\2\2\2TP\3\2\2")
        buf.write("\2U\32\3\2\2\2VW\7I\2\2WX\7Q\2\2XY\7V\2\2YZ\7Q\2\2Za\7")
        buf.write("D\2\2[\\\7i\2\2\\]\7q\2\2]^\7v\2\2^_\7q\2\2_a\7d\2\2`")
        buf.write("V\3\2\2\2`[\3\2\2\2a\34\3\2\2\2bc\7I\2\2cd\7Q\2\2de\7")
        buf.write("V\2\2ef\7Q\2\2fm\7H\2\2gh\7i\2\2hi\7q\2\2ij\7v\2\2jk\7")
        buf.write("q\2\2km\7h\2\2lb\3\2\2\2lg\3\2\2\2m\36\3\2\2\2no\7D\2")
        buf.write("\2op\7G\2\2pq\7I\2\2qr\7K\2\2ry\7P\2\2st\7d\2\2tu\7g\2")
        buf.write("\2uv\7i\2\2vw\7k\2\2wy\7p\2\2xn\3\2\2\2xs\3\2\2\2y \3")
        buf.write("\2\2\2z{\7G\2\2{|\7P\2\2|\u0081\7F\2\2}~\7g\2\2~\177\7")
        buf.write("p\2\2\177\u0081\7f\2\2\u0080z\3\2\2\2\u0080}\3\2\2\2\u0081")
        buf.write("\"\3\2\2\2\u0082\u0083\7O\2\2\u0083\u0084\7C\2\2\u0084")
        buf.write("\u0085\7E\2\2\u0085\u0086\7T\2\2\u0086\u008d\7Q\2\2\u0087")
        buf.write("\u0088\7o\2\2\u0088\u0089\7c\2\2\u0089\u008a\7e\2\2\u008a")
        buf.write("\u008b\7t\2\2\u008b\u008d\7q\2\2\u008c\u0082\3\2\2\2\u008c")
        buf.write("\u0087\3\2\2\2\u008d$\3\2\2\2\u008e\u008f\7R\2\2\u008f")
        buf.write("\u0090\7W\2\2\u0090\u0091\7U\2\2\u0091\u0097\7J\2\2\u0092")
        buf.write("\u0093\7r\2\2\u0093\u0094\7w\2\2\u0094\u0095\7u\2\2\u0095")
        buf.write("\u0097\7j\2\2\u0096\u008e\3\2\2\2\u0096\u0092\3\2\2\2")
        buf.write("\u0097&\3\2\2\2\u0098\u0099\7R\2\2\u0099\u009a\7Q\2\2")
        buf.write("\u009a\u009f\7R\2\2\u009b\u009c\7r\2\2\u009c\u009d\7q")
        buf.write("\2\2\u009d\u009f\7r\2\2\u009e\u0098\3\2\2\2\u009e\u009b")
        buf.write("\3\2\2\2\u009f(\3\2\2\2\u00a0\u00a2\7\17\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a6\7\f\2\2\u00a4\u00a6\7\17\2\2\u00a5\u00a1\3\2\2")
        buf.write("\2\u00a5\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8*\3\2\2\2\u00a9\u00ab")
        buf.write("\t\3\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\u00af\b\26\2\2\u00af,\3\2\2\2\20\2JT`lx\u0080\u008c")
        buf.write("\u0096\u009e\u00a1\u00a5\u00a7\u00ac\3\b\2\2")
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
    T__7 = 8
    T__8 = 9
    T__9 = 10
    INT = 11
    THEN = 12
    GOTOB = 13
    GOTOF = 14
    BEGIN = 15
    END = 16
    MACRO = 17
    PUSH = 18
    POP = 19
    NEWLINE = 20
    WHITESPACE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'R'", "'='", "'+'", "'-'", "'IF'", "'if'", "'!='", "'name'",
            "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INT", "THEN", "GOTOB", "GOTOF", "BEGIN", "END", "MACRO", "PUSH",
            "POP", "NEWLINE", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "INT", "THEN", "GOTOB", "GOTOF",
                  "BEGIN", "END", "MACRO", "PUSH", "POP", "NEWLINE", "WHITESPACE" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


