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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u00c4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\6\nD\n\n\r\n\16\nE\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\5\fN\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\rX\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16d\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17p\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20|\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u0084\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u0090\n\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u009a\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u00a2\n\24\3\25\3\25\3\25\7\25\u00a7")
        buf.write("\n\25\f\25\16\25\u00aa\13\25\3\26\3\26\3\26\3\26\7\26")
        buf.write("\u00b0\n\26\f\26\16\26\u00b3\13\26\3\27\5\27\u00b6\n\27")
        buf.write("\3\27\3\27\6\27\u00ba\n\27\r\27\16\27\u00bb\3\30\6\30")
        buf.write("\u00bf\n\30\r\30\16\30\u00c0\3\30\3\30\2\2\31\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\3\2\6\3")
        buf.write("\2\62;\4\2C\\c|\5\2\62;C\\c|\5\2\13\f\16\17\"\"\2\u00d3")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\3\61\3\2\2\2\5\63\3\2\2\2\7\65\3\2\2\2\t\67")
        buf.write("\3\2\2\2\13:\3\2\2\2\r<\3\2\2\2\17>\3\2\2\2\21@\3\2\2")
        buf.write("\2\23C\3\2\2\2\25G\3\2\2\2\27M\3\2\2\2\31W\3\2\2\2\33")
        buf.write("c\3\2\2\2\35o\3\2\2\2\37{\3\2\2\2!\u0083\3\2\2\2#\u008f")
        buf.write("\3\2\2\2%\u0099\3\2\2\2\'\u00a1\3\2\2\2)\u00a3\3\2\2\2")
        buf.write("+\u00ab\3\2\2\2-\u00b9\3\2\2\2/\u00be\3\2\2\2\61\62\7")
        buf.write("?\2\2\62\4\3\2\2\2\63\64\7-\2\2\64\6\3\2\2\2\65\66\7/")
        buf.write("\2\2\66\b\3\2\2\2\678\7#\2\289\7?\2\29\n\3\2\2\2:;\7*")
        buf.write("\2\2;\f\3\2\2\2<=\7+\2\2=\16\3\2\2\2>?\7=\2\2?\20\3\2")
        buf.write("\2\2@A\7.\2\2A\22\3\2\2\2BD\t\2\2\2CB\3\2\2\2DE\3\2\2")
        buf.write("\2EC\3\2\2\2EF\3\2\2\2F\24\3\2\2\2GH\7T\2\2H\26\3\2\2")
        buf.write("\2IJ\7K\2\2JN\7H\2\2KL\7k\2\2LN\7h\2\2MI\3\2\2\2MK\3\2")
        buf.write("\2\2N\30\3\2\2\2OP\7V\2\2PQ\7J\2\2QR\7G\2\2RX\7P\2\2S")
        buf.write("T\7v\2\2TU\7j\2\2UV\7g\2\2VX\7p\2\2WO\3\2\2\2WS\3\2\2")
        buf.write("\2X\32\3\2\2\2YZ\7I\2\2Z[\7Q\2\2[\\\7V\2\2\\]\7Q\2\2]")
        buf.write("d\7D\2\2^_\7i\2\2_`\7q\2\2`a\7v\2\2ab\7q\2\2bd\7d\2\2")
        buf.write("cY\3\2\2\2c^\3\2\2\2d\34\3\2\2\2ef\7I\2\2fg\7Q\2\2gh\7")
        buf.write("V\2\2hi\7Q\2\2ip\7H\2\2jk\7i\2\2kl\7q\2\2lm\7v\2\2mn\7")
        buf.write("q\2\2np\7h\2\2oe\3\2\2\2oj\3\2\2\2p\36\3\2\2\2qr\7D\2")
        buf.write("\2rs\7G\2\2st\7I\2\2tu\7K\2\2u|\7P\2\2vw\7d\2\2wx\7g\2")
        buf.write("\2xy\7i\2\2yz\7k\2\2z|\7p\2\2{q\3\2\2\2{v\3\2\2\2| \3")
        buf.write("\2\2\2}~\7G\2\2~\177\7P\2\2\177\u0084\7F\2\2\u0080\u0081")
        buf.write("\7g\2\2\u0081\u0082\7p\2\2\u0082\u0084\7f\2\2\u0083}\3")
        buf.write("\2\2\2\u0083\u0080\3\2\2\2\u0084\"\3\2\2\2\u0085\u0086")
        buf.write("\7O\2\2\u0086\u0087\7C\2\2\u0087\u0088\7E\2\2\u0088\u0089")
        buf.write("\7T\2\2\u0089\u0090\7Q\2\2\u008a\u008b\7o\2\2\u008b\u008c")
        buf.write("\7c\2\2\u008c\u008d\7e\2\2\u008d\u008e\7t\2\2\u008e\u0090")
        buf.write("\7q\2\2\u008f\u0085\3\2\2\2\u008f\u008a\3\2\2\2\u0090")
        buf.write("$\3\2\2\2\u0091\u0092\7R\2\2\u0092\u0093\7W\2\2\u0093")
        buf.write("\u0094\7U\2\2\u0094\u009a\7J\2\2\u0095\u0096\7r\2\2\u0096")
        buf.write("\u0097\7w\2\2\u0097\u0098\7u\2\2\u0098\u009a\7j\2\2\u0099")
        buf.write("\u0091\3\2\2\2\u0099\u0095\3\2\2\2\u009a&\3\2\2\2\u009b")
        buf.write("\u009c\7R\2\2\u009c\u009d\7Q\2\2\u009d\u00a2\7R\2\2\u009e")
        buf.write("\u009f\7r\2\2\u009f\u00a0\7q\2\2\u00a0\u00a2\7r\2\2\u00a1")
        buf.write("\u009b\3\2\2\2\u00a1\u009e\3\2\2\2\u00a2(\3\2\2\2\u00a3")
        buf.write("\u00a4\7T\2\2\u00a4\u00a8\t\3\2\2\u00a5\u00a7\t\4\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a9\3\2\2\2\u00a9*\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ac\5\37\20\2\u00ac\u00ad\5#\22\2\u00ad")
        buf.write("\u00b1\t\3\2\2\u00ae\u00b0\t\4\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3")
        buf.write("\2\2\2\u00b2,\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b6")
        buf.write("\7\17\2\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00ba\7\f\2\2\u00b8\u00ba\7\17\2")
        buf.write("\2\u00b9\u00b5\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write(".\3\2\2\2\u00bd\u00bf\t\5\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c3\b\30\2\2\u00c3\60\3\2")
        buf.write("\2\2\23\2EMWco{\u0083\u008f\u0099\u00a1\u00a8\u00b1\u00b5")
        buf.write("\u00b9\u00bb\u00c0\3\b\2\2")
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
    INT = 9
    R = 10
    IF = 11
    THEN = 12
    GOTOB = 13
    GOTOF = 14
    BEGIN = 15
    END = 16
    MACRO = 17
    PUSH = 18
    POP = 19
    RIDENTIFIER = 20
    MACROIDENTIFIER = 21
    NEWLINE = 22
    WHITESPACE = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'+'", "'-'", "'!='", "'('", "')'", "';'", "','", "'R'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "R", "IF", "THEN", "GOTOB", "GOTOF", "BEGIN", "END", 
            "MACRO", "PUSH", "POP", "RIDENTIFIER", "MACROIDENTIFIER", "NEWLINE", 
            "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "INT", "R", "IF", "THEN", "GOTOB", "GOTOF", "BEGIN", 
                  "END", "MACRO", "PUSH", "POP", "RIDENTIFIER", "MACROIDENTIFIER", 
                  "NEWLINE", "WHITESPACE" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


