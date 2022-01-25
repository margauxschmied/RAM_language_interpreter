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
t_IF = r'(IF|if)'
t_THEN = r'(THEN|then)'
t_GOTOB = r'(GOTOB|gotob)'
t_GOTOF = r'(GOTOF|gotof)'
t_BEGIN = r'(BEGIN|begin)'
t_END = r'(END|end)'
t_MACRO = r'(MACRO|macro)'
t_PUSH = r'(PUSH|push)'
t_POP = r'(POP|pop)'
t_RPAREN = r'\)'
t_EQ = r'\='
t_NEQ = r'\!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_VIRGULE = r','
t_POINTVIRGULE = r';'

digit = r'([0-9]+)'
nondigit = r'([A-Za-z_]+)'
macroIdentifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*\()'

# macroIdentifier = r'(' + nondigit + '\()'
RIdentifier = r'(R(' + nondigit + r'(' + digit + r'|' + nondigit + r')*))'


# RIdentifier = r'(R(' + digit + r'|' + nondigit + r')+)'


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


macros = {}


# registerUse = []


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
    p[0] = p[1]


# expr returns [Instruction instruction]:
#     ;

def p_expression_push(p):
    #     PUSH R r1=INT {$instruction= Instruction(4, Register($r1.text))}
    'expression : PUSH R NUMBER'
    p[0] = Instruction("push", Register(p[3]))  # "PUSH R" + str(p[3])


def p_expression_pop(p):
    #     | POP R r1=INT {$instruction= Instruction(5, Register($r1.text))}
    'expression : POP R NUMBER'
    p[0] = Instruction("pop", Register(p[3]))  # "POP R" + str(p[3])


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

    line = p.lineno(1)

    if p[2] != p[5]:
        p_error_verif(p, line)

    if p[7] != 1:
        p_error_verif(p, line)

    if p[6] == '+':
        # p[1] + str(p[2]) + p[3] + p[4] + str(p[5]) + "+" + str(p[7])
        p[0] = Instruction(0, Register(p[2]))
    elif p[6] == '-':
        # p[1] + str(p[2]) + p[3] + p[4] + str(p[5]) + "-" + str(p[7])
        p[0] = Instruction(1, Register(p[2]))


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

    line = p.lineno(1)

    if p[5] != 0:
        p_error_verif(p, line)

    if p[7] == 'GOTOB' or p[7] == 'gotob':
        p[0] = Instruction(2, Register(p[3]),
                           p[8])  # p[1] + p[2] + str(p[3]) + p[4] + str(p[5]) + p[6] + 'GOTOB' + str(p[8])
    elif p[7] == 'GOTOF' or p[7] == 'gotof':
        p[0] = Instruction(3, Register(p[3]),
                           p[8])  # p[1] + p[2] + str(p[3]) + p[4] + str(p[5]) + p[6] + 'GOTOF' + str(p[8])


def p_expression_5(p):
    # | macro {$instruction=$macro.instruction}
    'expression : macroDeclaration'
    p[0] = p[1]


def p_expression_callmacro(p):
    # | ID(list) {$instruction=$macro.instruction}
    'expression : callmacro'
    p[0] = p[1]


def p_callmacro(p):
    'callmacro : MACROID listRegister RPAREN'
    line = p.lineno(1)

    if p[1][:-1] not in macros.keys():
        p_error_verif(p, line)

    elif not macros[p[1][:-1]].good_number_of_register(p[2]):
        p_error_verif(p, line)

    p[0] = Instruction(p[1][:-1], p[2])  # p[1] + p[2] + p[3]


# macro returns [Instruction instruction]:
#     BEGIN MACRO name=MACROIDENTIFIER  macro_list_register ')' NEWLINE code NEWLINE END MACRO ';'  {$instruction=Macro($name.text, macro_list_register.register, $code.instruction)}
# ;

def p_macroDeclaration(p):
    'macroDeclaration : BEGIN MACRO MACROID macroListRegister RPAREN macroCode END MACRO POINTVIRGULE'

    macros[p[3][:-1]] = p[4]

    macro = Macro(p[3][:-1], p[4], p[6])
    # p[1] + p[2] + p[3] + str(p[4]) + p[5] + "\n" + p[6] + p[7] + p[8] + p[9]
    line = p.lineno(1)

    if not macro.verification_of_use_register():
        p_error_verif(p, line)

    p[0] = macro


def p_listRegister(p):
    '''listRegister : R NUMBER VIRGULE listRegister
                            | R NUMBER
                            | '''
    if len(p) == 3:
        p[0] = Register(p[2])  # p[1] + str(p[2])
    elif len(p) == 5:
        p[0] = Register(p[2], p[4])  # p[1] + str(p[2]) + p[3] + p[4]
    else:
        p[0] = None


# macro_list_register returns [Register register]:
#     r1=RIDENTIFIER ',' list_register {$register=Register($r1.text, $list_register.register)}
#     | r1=RIDENTIFIER   {$register=Register($r1.text)}
#     ;


def p_macroListRegister(p):
    '''macroListRegister : RID VIRGULE macroListRegister
                            | RID
                            | '''
    if len(p) == 2:
        p[0] = Register(p[1][1:])  # p[1]
    elif len(p) == 4:
        p[0] = Register(p[1][1:], p[3])  # p[1] + p[2] + p[3]
    else:
        p[0] = None


def p_macroCode_list(p):
    'macroCode : macroExpression macroCode'
    p[1].setNext(p[2])
    p[0] = p[1]  # str(p[1]) + "\n" + str(p[2])


def p_macroCode_simple(p):
    'macroCode : macroExpression'
    p[0] = p[1]


# expr returns [Instruction instruction]:
#     ;

def p_macroExpression_push(p):
    #     PUSH R r1=INT {$instruction= Instruction(4, Register($r1.text))}
    'macroExpression : PUSH macroid'
    p[0] = Instruction("push", Register(p[2]))  # p[1] + p[2]


def p_macroExpression_pop(p):
    #     | POP R r1=INT {$instruction= Instruction(5, Register($r1.text))}
    'macroExpression : POP macroid'
    p[0] = Instruction("pop", Register(p[2]))  # p[1] + p[2]


def p_macroExpression_12(p):
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
    '''macroExpression : macroid EQ macroid PLUS NUMBER
                    | macroid EQ macroid MINUS NUMBER'''

    line = p.lineno(1)

    if p[1] != p[3]:
        p_error_verif(p, line)

    if p[5] != 1:
        p_error_verif(p, line)

    if p[4] == '+':
        # p[1] + str(p[2]) + p[3] + p[4] + str(p[5])
        p[0] = Instruction(0, Register(p[1]))
    elif p[4] == '-':
        # p[1] + str(p[2]) + p[3] + p[4] + str(p[5])
        p[0] = Instruction(1, Register(p[1]))


def p_macroExpression_34(p):
    # | IF R r1=INT '!=' zero=INT THEN goto=(GOTOB|GOTOF) n=INT {
    # if $zero.text != '0':
    #     raise ValueError("line "+str($zero.line)+": "+$zero.text+" != 0")
    # if $goto.text=='GOTOB' or $goto.text=='gotob':
    #     $instruction= Instruction(2, Register($r1.text), $n.text)
    # else:
    #     $instruction= Instruction(3, Register($r1.text), $n.text)
    # }
    '''macroExpression : IF macroid NEQ NUMBER THEN GOTOB NUMBER
                    | IF macroid NEQ NUMBER THEN GOTOF NUMBER'''

    line = p.lineno(1)

    if p[4] != 0:
        p_error_verif(p, line)

    if p[6] == 'GOTOB' or p[6] == 'gotob':
        # p[1] + p[2] + p[3] + str(p[4]) + p[5] + p[6] + str(p[7])
        p[0] = Instruction(2, Register(p[2]), p[7])
    elif p[6] == 'GOTOF' or p[6] == 'gotof':
        # p[1] + p[2] + p[3] + str(p[4]) + p[5] + p[6] + str(p[7])
        p[0] = Instruction(3, Register(p[2]), p[7])


def p_macroExpression_callmacro(p):
    'macroExpression : MACROID listMacroid RPAREN'

    line = p.lineno(1)

    if p[1][:-1] not in macros.keys():
        p_error_verif(p, line)

    elif not macros[p[1][:-1]].good_number_of_register(p[2]):
        p_error_verif(p, line)

    p[0] = Instruction(p[1][:-1], p[2])  # p[1] + p[2] + p[3]


def p_macroid(p):
    '''macroid : RID
               | R NUMBER'''

    if len(p) == 2:
        # registerUse.append(p[1][1:])
        p[0] = p[1][1:]
    elif len(p) == 3:
        p[0] = p[2]


def p_listMacroid(p):
    '''listMacroid : macroid VIRGULE listMacroid
                            | macroid
                            | '''
    if len(p) == 2:
        p[0] = Register(p[1])  # p[1] + str(p[2])
    elif len(p) == 4:
        p[0] = Register(p[1], p[3])  # p[1] + str(p[2]) + p[3] + p[4]
    else:
        p[0] = None


# Error rule for syntax errors


def p_error_verif(p, line):
    raise Exception(f"Syntax error: Unexpected line {line}")


def p_error(p):
    raise Exception(f"Syntax error: Unexpected line {p.lineno}")


def myLex():
    return lex.lex()


def myYacc():
    return yacc.yacc()


if __name__ == '__main__':
    data = """begin MACRO a(Rx, Ry)
    Rx = Rx + 1
    R1 = R1 + 1
    Rx = Rx - 1
    IF Rx != 0 THEN GOTOB 2
    Rx = Rx - 1
    END MACRO;
    a(R1, R1)
"""

    lexer = lex.lex()
    lexer.input(data)

    parser = yacc.yacc()

    result = parser.parse(data)
