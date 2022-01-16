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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u00c0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\6\t@\n\t\r\t\16\tA\3\n\3\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("J\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fT\n\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r`\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16l\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("x\n\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0080\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u008c\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u0096\n\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u009e")
        buf.write("\n\23\3\24\3\24\3\24\7\24\u00a3\n\24\f\24\16\24\u00a6")
        buf.write("\13\24\3\25\3\25\7\25\u00aa\n\25\f\25\16\25\u00ad\13\25")
        buf.write("\3\25\3\25\3\26\5\26\u00b2\n\26\3\26\3\26\6\26\u00b6\n")
        buf.write("\26\r\26\16\26\u00b7\3\27\6\27\u00bb\n\27\r\27\16\27\u00bc")
        buf.write("\3\27\3\27\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30\3\2\6\3\2\62;\4\2C\\c|\5\2\62;C\\c|\5\2\13")
        buf.write("\f\16\17\"\"\2\u00cf\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\3/\3\2\2\2\5\61\3\2\2\2\7\63\3\2\2\2")
        buf.write("\t\65\3\2\2\2\138\3\2\2\2\r:\3\2\2\2\17<\3\2\2\2\21?\3")
        buf.write("\2\2\2\23C\3\2\2\2\25I\3\2\2\2\27S\3\2\2\2\31_\3\2\2\2")
        buf.write("\33k\3\2\2\2\35w\3\2\2\2\37\177\3\2\2\2!\u008b\3\2\2\2")
        buf.write("#\u0095\3\2\2\2%\u009d\3\2\2\2\'\u009f\3\2\2\2)\u00a7")
        buf.write("\3\2\2\2+\u00b5\3\2\2\2-\u00ba\3\2\2\2/\60\7?\2\2\60\4")
        buf.write("\3\2\2\2\61\62\7-\2\2\62\6\3\2\2\2\63\64\7/\2\2\64\b\3")
        buf.write("\2\2\2\65\66\7#\2\2\66\67\7?\2\2\67\n\3\2\2\289\7.\2\2")
        buf.write("9\f\3\2\2\2:;\7+\2\2;\16\3\2\2\2<=\7=\2\2=\20\3\2\2\2")
        buf.write(">@\t\2\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\22")
        buf.write("\3\2\2\2CD\7T\2\2D\24\3\2\2\2EF\7K\2\2FJ\7H\2\2GH\7k\2")
        buf.write("\2HJ\7h\2\2IE\3\2\2\2IG\3\2\2\2J\26\3\2\2\2KL\7V\2\2L")
        buf.write("M\7J\2\2MN\7G\2\2NT\7P\2\2OP\7v\2\2PQ\7j\2\2QR\7g\2\2")
        buf.write("RT\7p\2\2SK\3\2\2\2SO\3\2\2\2T\30\3\2\2\2UV\7I\2\2VW\7")
        buf.write("Q\2\2WX\7V\2\2XY\7Q\2\2Y`\7D\2\2Z[\7i\2\2[\\\7q\2\2\\")
        buf.write("]\7v\2\2]^\7q\2\2^`\7d\2\2_U\3\2\2\2_Z\3\2\2\2`\32\3\2")
        buf.write("\2\2ab\7I\2\2bc\7Q\2\2cd\7V\2\2de\7Q\2\2el\7H\2\2fg\7")
        buf.write("i\2\2gh\7q\2\2hi\7v\2\2ij\7q\2\2jl\7h\2\2ka\3\2\2\2kf")
        buf.write("\3\2\2\2l\34\3\2\2\2mn\7D\2\2no\7G\2\2op\7I\2\2pq\7K\2")
        buf.write("\2qx\7P\2\2rs\7d\2\2st\7g\2\2tu\7i\2\2uv\7k\2\2vx\7p\2")
        buf.write("\2wm\3\2\2\2wr\3\2\2\2x\36\3\2\2\2yz\7G\2\2z{\7P\2\2{")
        buf.write("\u0080\7F\2\2|}\7g\2\2}~\7p\2\2~\u0080\7f\2\2\177y\3\2")
        buf.write("\2\2\177|\3\2\2\2\u0080 \3\2\2\2\u0081\u0082\7O\2\2\u0082")
        buf.write("\u0083\7C\2\2\u0083\u0084\7E\2\2\u0084\u0085\7T\2\2\u0085")
        buf.write("\u008c\7Q\2\2\u0086\u0087\7o\2\2\u0087\u0088\7c\2\2\u0088")
        buf.write("\u0089\7e\2\2\u0089\u008a\7t\2\2\u008a\u008c\7q\2\2\u008b")
        buf.write("\u0081\3\2\2\2\u008b\u0086\3\2\2\2\u008c\"\3\2\2\2\u008d")
        buf.write("\u008e\7R\2\2\u008e\u008f\7W\2\2\u008f\u0090\7U\2\2\u0090")
        buf.write("\u0096\7J\2\2\u0091\u0092\7r\2\2\u0092\u0093\7w\2\2\u0093")
        buf.write("\u0094\7u\2\2\u0094\u0096\7j\2\2\u0095\u008d\3\2\2\2\u0095")
        buf.write("\u0091\3\2\2\2\u0096$\3\2\2\2\u0097\u0098\7R\2\2\u0098")
        buf.write("\u0099\7Q\2\2\u0099\u009e\7R\2\2\u009a\u009b\7r\2\2\u009b")
        buf.write("\u009c\7q\2\2\u009c\u009e\7r\2\2\u009d\u0097\3\2\2\2\u009d")
        buf.write("\u009a\3\2\2\2\u009e&\3\2\2\2\u009f\u00a0\7T\2\2\u00a0")
        buf.write("\u00a4\t\3\2\2\u00a1\u00a3\t\4\2\2\u00a2\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3")
        buf.write("\2\2\2\u00a5(\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00ab")
        buf.write("\t\3\2\2\u00a8\u00aa\t\4\2\2\u00a9\u00a8\3\2\2\2\u00aa")
        buf.write("\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af\7")
        buf.write("*\2\2\u00af*\3\2\2\2\u00b0\u00b2\7\17\2\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b6\7\f\2\2\u00b4\u00b6\7\17\2\2\u00b5\u00b1\3\2\2")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8,\3\2\2\2\u00b9\u00bb")
        buf.write("\t\5\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00bf\b\27\2\2\u00bf.\3\2\2\2\23\2AIS_kw\177\u008b")
        buf.write("\u0095\u009d\u00a4\u00ab\u00b1\u00b5\u00b7\u00bc\3\b\2")
        buf.write("\2")
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
    R = 9
    IF = 10
    THEN = 11
    GOTOB = 12
    GOTOF = 13
    BEGIN = 14
    END = 15
    MACRO = 16
    PUSH = 17
    POP = 18
    RIDENTIFIER = 19
    MACROIDENTIFIER = 20
    NEWLINE = 21
    WHITESPACE = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'+'", "'-'", "'!='", "','", "')'", "';'", "'R'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "R", "IF", "THEN", "GOTOB", "GOTOF", "BEGIN", "END", 
            "MACRO", "PUSH", "POP", "RIDENTIFIER", "MACROIDENTIFIER", "NEWLINE", 
            "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "INT", "R", "IF", "THEN", "GOTOB", "GOTOF", "BEGIN", "END", 
                  "MACRO", "PUSH", "POP", "RIDENTIFIER", "MACROIDENTIFIER", 
                  "NEWLINE", "WHITESPACE" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


