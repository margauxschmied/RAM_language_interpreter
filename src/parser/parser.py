import ply.lex as lex
import ply.yacc as yacc

# List of token names.   This is always required

try:
    from src.parser.instruction.instructionParser import Instruction
    from src.parser.instruction.macro import Macro
    from src.parser.instruction.register import Register
except:
    from src.parser.instruction.instructionParser import Instruction
    from src.parser.instruction.macro import Macro
    from src.parser.instruction.register import Register

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
t_IF = r'if'
t_THEN = r'then'
t_GOTOB = r'gotob'
t_GOTOF = r'gotof'
t_BEGIN = r'begin'
t_END = r'end'
t_MACRO = r'macro'
t_PUSH = r'push'
t_POP = r'pop'
t_RPAREN = r'\)'
t_EQ = r'\='
t_NEQ = r'\!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_VIRGULE = r','
t_POINTVIRGULE = r';'

digit = r'([0-9]+)'
nondigit = r'([a-z_]+)'


RIdentifier = r'(R(' + nondigit + r'(' + digit + r'|' + nondigit + r')*))'


macroIdentifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*\()'


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
    raise Exception(f"Illegal character {t.value[0]}: line {t.lineno}")


macros = {}


def p_program(p):
    'program : code'
    p[0] = p[1]


def p_code_list(p):
    'code : expression code'
    p[1].setNext(p[2])
    p[0] = p[1]


def p_code_simple(p):
    'code : expression'
    p[0] = p[1]


def p_expression_push(p):
    'expression : PUSH R NUMBER'
    p[0] = Instruction("push", Register(p[3]))


def p_expression_pop(p):
    'expression : POP R NUMBER'
    p[0] = Instruction("pop", Register(p[3]))


def p_callmacro(p):
    'callmacro : MACROID listRegister RPAREN'
    line = p.lineno(1)
    register = p[2]

    if p[1] == "rp(":
        if len(register.list_register()) != 2:
            error_verif(p, line)
        p[0] = Instruction(4, register)

    elif p[1] == "lp(":
        if len(register.list_register()) != 2:
            error_verif(p, line)
        p[0] = Instruction(5, register)

    elif p[1][:-1] not in macros.keys():
        error_verif(p, line)

    elif not macros[p[1][:-1]].good_number_of_register(register):
        error_verif(p, line)

    else:
        p[0] = Instruction(p[1][:-1], register)


def p_expression_12(p):
    '''expression : R NUMBER EQ R NUMBER PLUS NUMBER
                    | R NUMBER EQ R NUMBER MINUS NUMBER'''

    line = p.lineno(1)

    if p[2] != p[5]:
        error_verif(p, line)

    if p[7] != 1:
        error_verif(p, line)

    if p[6] == '+':
        p[0] = Instruction(0, Register(p[2]))
    elif p[6] == '-':
        p[0] = Instruction(1, Register(p[2]))


def p_expression_34(p):
    '''expression : IF R NUMBER NEQ NUMBER THEN GOTOB NUMBER
                    | IF R NUMBER NEQ NUMBER THEN GOTOF NUMBER'''

    line = p.lineno(1)

    if p[5] != 0:
        error_verif(p, line)

    if p[7] == 'gotob':
        p[0] = Instruction(2, Register(p[3]), p[8])
    elif p[7] == 'gotof':
        p[0] = Instruction(3, Register(p[3]), p[8])


def p_expression_5(p):
    'expression : macroDeclaration'
    p[0] = p[1]


def p_expression_callmacro(p):
    'expression : callmacro'
    p[0] = p[1]


def p_macroDeclaration(p):
    'macroDeclaration : BEGIN MACRO MACROID macroListRegister RPAREN macroCode END MACRO POINTVIRGULE'

    macros[p[3][:-1]] = p[4]

    macro = Macro(p[3][:-1], p[4], p[6])
    line = p.lineno(1)

    if not macro.verification_of_use_register():
        error_verif(p, line)

    p[0] = macro


def p_listRegister(p):
    '''listRegister : R NUMBER VIRGULE listRegister
                            | R NUMBER
                            | '''
    if len(p) == 3:
        p[0] = Register(p[2])
    elif len(p) == 5:
        p[0] = Register(p[2], p[4])
    else:
        p[0] = None


def p_macroListRegister(p):
    '''macroListRegister : RID VIRGULE macroListRegister
                            | RID
                            | '''
    if len(p) == 2:
        p[0] = Register(p[1][1:])
    elif len(p) == 4:
        p[0] = Register(p[1][1:], p[3])
    else:
        p[0] = None


def p_macroCode_list(p):
    'macroCode : macroExpression macroCode'
    p[1].setNext(p[2])
    p[0] = p[1]


def p_macroCode_simple(p):
    'macroCode : macroExpression'
    p[0] = p[1]


def p_macroExpression_push(p):
    'macroExpression : PUSH macroid'
    p[0] = Instruction("push", Register(p[2]))


def p_macroExpression_pop(p):
    'macroExpression : POP macroid'
    p[0] = Instruction("pop", Register(p[2]))


def p_macroExpression_12(p):
    '''macroExpression : macroid EQ macroid PLUS NUMBER
                    | macroid EQ macroid MINUS NUMBER'''

    line = p.lineno(1)

    if p[1] != p[3]:
        error_verif(p, line)

    if p[5] != 1:
        error_verif(p, line)

    if p[4] == '+':
        p[0] = Instruction(0, Register(p[1]))
    elif p[4] == '-':
        p[0] = Instruction(1, Register(p[1]))


def p_macroExpression_34(p):
    '''macroExpression : IF macroid NEQ NUMBER THEN GOTOB NUMBER
                    | IF macroid NEQ NUMBER THEN GOTOF NUMBER'''

    line = p.lineno(1)

    if p[4] != 0:
        error_verif(p, line)

    if p[6] == 'gotob':
        p[0] = Instruction(2, Register(p[2]), p[7])
    elif p[6] == 'gotof':
        p[0] = Instruction(3, Register(p[2]), p[7])


def p_macroExpression_callmacro(p):
    'macroExpression : MACROID listMacroid RPAREN'

    line = p.lineno(1)
    register = p[2]

    if p[1] == "rp(":
        if len(register.list_register()) != 2:
            error_verif(p, line)
        p[0] = Instruction(4, register)

    elif p[1] == "lp(":
        if len(register.list_register()) != 2:
            error_verif(p, line)
        p[0] = Instruction(5, register)

    if p[1][:-1] not in macros.keys():
        error_verif(p, line)

    elif not macros[p[1][:-1]].good_number_of_register(p[2]):
        error_verif(p, line)

    p[0] = Instruction(p[1][:-1], p[2])


def p_macroid(p):
    '''macroid : RID
               | R NUMBER'''

    if len(p) == 2:
        p[0] = p[1][1:]
    elif len(p) == 3:
        p[0] = p[2]


def p_listMacroid(p):
    '''listMacroid : macroid VIRGULE listMacroid
                            | macroid
                            | '''
    if len(p) == 2:
        p[0] = Register(p[1])
    elif len(p) == 4:
        p[0] = Register(p[1], p[3])
    else:
        p[0] = None


# Error rule for syntax errors


def error_verif(p, line):
    raise Exception(f"Syntax error: Unexpected line {line}")


def p_error(p):
    raise Exception(f"Syntax error: Unexpected line {p.lineno}")


def myLex():
    return lex.lex()


def myYacc():
    return yacc.yacc()


if __name__ == '__main__':
    data = """ffff
"""

    lexer = lex.lex()
    lexer.input(data)

    parser = yacc.yacc()

    result = parser.parse(data)
