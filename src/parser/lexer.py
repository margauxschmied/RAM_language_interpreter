import ply.lex as lex
import ply.yacc as yacc

# List of token names.   This is always required
from src.instruction.instruction import Instruction
from src.instruction.macro import Macro
from src.instruction.register import Register

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'R',
    'IF',
    'THEN',
    'GOTOB',
    'GOTOF',
    'BEGIN',
    'END',
    'MACRO',
    'PUSH',
    'POP',
    'LPAREN',
    'RPAREN',
    'EQ',
    'NEQ',
    'VIRGULE',
    'POINTVIRGULE',
    'MACROID',
    'RID',
)

# Regular expression rules for simple tokens

t_R = 'R'
t_IF = 'IF'
t_THEN = 'THEN'
t_GOTOB = 'GOTOB'
t_GOTOF = 'GOTOF'
t_BEGIN = 'BEGIN'
t_END = 'END'
t_MACRO = 'MACRO'
t_PUSH = 'PUSH'
t_POP = 'POP'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQ = r'\='
t_NEQ = r'\!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_VIRGULE = r','
t_POINTVIRGULE = r';'

digit = r'([0-9])'
nondigit = r'([_A-Za-z]+)'
# identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

macroIdentifier = r'(' + nondigit + '\()'
RIdentifier = r'(R' + nondigit + ')'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


@lex.TOKEN(RIdentifier)
def t_RID(t):
    t.value = str(t.value)
    return t


@lex.TOKEN(macroIdentifier)
def t_MACROID(t):
    t.value = str(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def build():
    return lex.lex()


def p_program(p):
    # program returns [Instruction instruction]:
    #     code EOF {$instruction=$code.instruction} # MakeList
    #     ;
    'program : code'
    p[0] = p[1]


# code returns [Instruction instruction]:
#     expr NEWLINE code {$instruction =$expr.instruction
# $instruction.setNext($code.instruction)}
#     | expr {$instruction =$expr.instruction}
#     ;

def p_code_list(p):
    'code : expression code'
    p[1].setNext(p[2])
    p[0] = p[1]


def p_code_simple(p):
    'code : expression'
    p[0] = str(p[1])


# expr returns [Instruction instruction]:
#     ;

def p_expression_push(p):
    #     PUSH R r1=INT {$instruction= Instruction(4, Register($r1.text))}

    'expression : PUSH R NUMBER'
    p[0] = Instruction(4, Register(p[3]))  # "PUSH R" + str(p[3])


def p_expression_pop(p):
    #     | POP R r1=INT {$instruction= Instruction(5, Register($r1.text))}

    'expression : POP R NUMBER'
    p[0] = Instruction(5, Register(p[3]))  # "POP R" + str(p[3])


def p_expression_12(p):
    # | R r1 = INT '=' R r2 = INT op = ('+' | '-') un = INT {
    # if $r1.text != $r2.text:
    #     raise ValueError("line "+str($r1.line)+": R"+$r1.text+" != "+"R"+$r2.text)
    # if $un.text != '1':
    #     raise ValueError("line "+str($un.line)+": "+$un.text+" != 1")
    # if $op.text=='+':
    #     $instruction= Instruction(0, Register($r1.text))
    # else:
    #     $instruction= Instruction(1, Register($r1.text))
    # }

    '''expression : R NUMBER EQ R NUMBER PLUS NUMBER
                    | R NUMBER EQ R NUMBER MINUS NUMBER'''

    if p[2] != p[5]:
        p_error(p)

    if p[7] != 1:
        p_error(p)

    if p[6] == '+':
        p[0] = Instruction(0, Register(p[2]))  #p[1] + str(p[2]) + p[3] + p[4] + str(p[5]) + "+" + str(p[7])
    elif p[6] == '-':
        p[0] = Instruction(1, Register(p[2]))  #p[1] + str(p[2]) + p[3] + p[4] + str(p[5]) + "-" + str(p[7])


def p_expression_34(p):
    # | IF R r1=INT '!=' zero=INT THEN goto=(GOTOB|GOTOF) n=INT {
    # if $zero.text != '0':
    #     raise ValueError("line "+str($zero.line)+": "+$zero.text+" != 0")
    # if $goto.text=='GOTOB' or $goto.text=='gotob':
    #     $instruction= Instruction(2, Register($r1.text), $n.text)
    # else:
    #     $instruction= Instruction(3, Register($r1.text), $n.text)
    # }
    '''expression : IF R NUMBER NEQ NUMBER THEN GOTOB NUMBER
                    | IF R NUMBER NEQ NUMBER THEN GOTOF NUMBER'''

    if p[5] != 0:
        p_error(p)

    if p[7] == 'GOTOB':
        p[0] = Instruction(2, Register(p[3]), p[8])  #p[1] + p[2] + str(p[3]) + p[4] + str(p[5]) + p[6] + 'GOTOB' + str(p[8])
    elif p[7] == 'GOTOF':
        p[0] = Instruction(3, Register(p[3]), p[8])  #p[1] + p[2] + str(p[3]) + p[4] + str(p[5]) + p[6] + 'GOTOF' + str(p[8])


def p_expression_5(p):
    # | macro {$instruction=$macro.instruction}
    'expression : macro'
    p[0] = p[1]


def p_expression_callmacro(p):
    # | ID(list) {$instruction=$macro.instruction}
    'expression : callmacro'
    p[0] = p[1]


def p_callmacro(p):
    'callmacro : MACROID list_register RPAREN'
    p[0] = Macro(p[1][:-1], p[2], None)  #p[1] + p[2] + p[3]

# macro returns [Instruction instruction]:
#     BEGIN MACRO name=MACROIDENTIFIER  macro_list_register ')' NEWLINE code NEWLINE END MACRO ';'  {$instruction=Macro($name.text, macro_list_register.register, $code.instruction)}
# ;

def p_macro(p):
    'macro : BEGIN MACRO MACROID macro_list_register RPAREN macro_code END MACRO POINTVIRGULE'
    p[0] = Macro(p[3][:-1], p[4], p[6]) #p[1] + p[2] + p[3] + str(p[4]) + p[5] + "\n" + p[6] + p[7] + p[8] + p[9]


def p_list_register(p):
    '''list_register : R NUMBER VIRGULE list_register
                            | R NUMBER
                            | '''
    if len(p) == 3:
        p[0] = Register(p[2])  #p[1] + str(p[2])
    elif len(p) == 5:
        p[0] = Register(p[2], p[4])  #p[1] + str(p[2]) + p[3] + p[4]
    else:
        p[0]=None


# macro_list_register returns [Register register]:
#     r1=RIDENTIFIER ',' list_register {$register=Register($r1.text, $list_register.register)}
#     | r1=RIDENTIFIER   {$register=Register($r1.text)}
#     ;


def p_macro_list_register(p):
    '''macro_list_register : RID VIRGULE macro_list_register
                            | RID
                            | '''
    if len(p) == 2:
        p[0] = Register(p[1][1:])  #p[1]
    elif len(p) == 4:
        p[0] = Register(p[1][1:], p[3])  #p[1] + p[2] + p[3]
    else:
        p[0] = None


def p_macro_code_list(p):
    'macro_code : macro_expression macro_code'
    p[1].setNext(p[2])
    p[0] = p[1]  #str(p[1]) + "\n" + str(p[2])


def p_macro_code_simple(p):
    'macro_code : macro_expression'
    p[0] = p[1]


# expr returns [Instruction instruction]:
#     ;

def p_macro_expression_push(p):
    #     PUSH R r1=INT {$instruction= Instruction(4, Register($r1.text))}

    'macro_expression : PUSH RID'
    p[0] = Instruction(4, Register(p[2][1:]))  #p[1] + p[2]


def p_macro_expression_pop(p):
    #     | POP R r1=INT {$instruction= Instruction(5, Register($r1.text))}

    'macro_expression : POP RID'
    p[0] = Instruction(5, Register(p[2][1:]))  #p[1] + p[2]


def p_macro_expression_12(p):
    # | R r1 = INT '=' R r2 = INT op = ('+' | '-') un = INT {
    # if $r1.text != $r2.text:
    #     raise ValueError("line "+str($r1.line)+": R"+$r1.text+" != "+"R"+$r2.text)
    # if $un.text != '1':
    #     raise ValueError("line "+str($un.line)+": "+$un.text+" != 1")
    # if $op.text=='+':
    #     $instruction= Instruction(0, Register($r1.text))
    # else:
    #     $instruction= Instruction(1, Register($r1.text))
    # }

    '''macro_expression : RID EQ RID PLUS NUMBER
                    | RID EQ RID MINUS NUMBER'''


    if p[1] != p[3]:
        p_error(p)

    if p[5] != 1:
        p_error(p)

    if p[4] == '+':
        p[0] = Instruction(0, Register(p[1][1:]))  #p[1] + str(p[2]) + p[3] + p[4] + str(p[5])
    elif p[4] == '-':
        p[0] = Instruction(1, Register(p[1][1:]))  #p[1] + str(p[2]) + p[3] + p[4] + str(p[5])


def p_macro_expression_34(p):
    # | IF R r1=INT '!=' zero=INT THEN goto=(GOTOB|GOTOF) n=INT {
    # if $zero.text != '0':
    #     raise ValueError("line "+str($zero.line)+": "+$zero.text+" != 0")
    # if $goto.text=='GOTOB' or $goto.text=='gotob':
    #     $instruction= Instruction(2, Register($r1.text), $n.text)
    # else:
    #     $instruction= Instruction(3, Register($r1.text), $n.text)
    # }
    '''macro_expression : IF RID NEQ NUMBER THEN GOTOB NUMBER
                    | IF RID NEQ NUMBER THEN GOTOF NUMBER'''

    if p[4] != 0:
        p_error(p)

    if p[6] == 'GOTOB':
        p[0] = Instruction(2, Register(p[2][1:]), p[7])  #p[1] + p[2] + p[3] + str(p[4]) + p[5] + p[6] + str(p[7])
    elif p[6] == 'GOTOF':
        p[0] = Instruction(3, Register(p[2][1:]), p[7])  #p[1] + p[2] + p[3] + str(p[4]) + p[5] + p[6] + str(p[7])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! ")
    # yacc.errok()


if __name__ == '__main__':
    data = """BEGIN MACRO name(Rx, Ry)
    Rx = Rx + 1
    Rx = Rx + 1
    Rx = Rx - 1
    IF Rx != 0 THEN GOTOB 2
    Rx = Rx - 1
    END MACRO;
    a()
"""

    # data = """PUSH R2
    # POP R2
    # """

    lexer = lex.lex()
    lexer.input(data)

    # Tokenize
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break  # No more input
    #     print(tok)

    parser = yacc.yacc()

    # while True:
    #     try:
    #         s = data
    #     except EOFError:
    #         break
    #     if not s: continue
    result = parser.parse(data)
    print(result)
