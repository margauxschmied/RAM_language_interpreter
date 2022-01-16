import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from ply import lex

from lexer import tokens, build



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
    p[0] = str(p[1]) + str(p[2])

def p_code_simple(p):
    'code : expression'
    p[0] = str(p[1])


# expr returns [Instruction instruction]:
#     | POP R r1=INT {$instruction= Instruction(5, Register($r1.text))}
#     | R r1=INT '=' R r2=INT op=('+'|'-') un=INT  {
# if $r1.text != $r2.text:
#     raise ValueError("line "+str($r1.line)+": R"+$r1.text+" != "+"R"+$r2.text)
# if $un.text != '1':
#     raise ValueError("line "+str($un.line)+": "+$un.text+" != 1")
# if $op.text=='+':
#     $instruction= Instruction(0, Register($r1.text))
# else:
#     $instruction= Instruction(1, Register($r1.text))
# }
#     | IF R r1=INT '!=' zero=INT THEN goto=(GOTOB|GOTOF) n=INT {
# if $zero.text != '0':
#     raise ValueError("line "+str($zero.line)+": "+$zero.text+" != 0")
# if $goto.text=='GOTOB' or $goto.text=='gotob':
#     $instruction= Instruction(2, Register($r1.text), $n.text)
# else:
#     $instruction= Instruction(3, Register($r1.text), $n.text)
# }
#     | macro {$instruction=$macro.instruction}
#     ;

def p_expression_push(p):
    #     PUSH R r1=INT {$instruction= Instruction(4, Register($r1.text))}

    'expression : PUSH R NUMBER'
    p[0] = str(p[3])

def p_expression_pop(p):
    #     | POP R r1=INT {$instruction= Instruction(5, Register($r1.text))}

    'expression : POP R NUMBER'
    p[0] = str(p[3])





# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

if __name__ == '__main__':
    data = """PUSH R2
POP R2
"""
    lexer = build()
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

    parser = yacc.yacc()

    while True:
        try:
            s = data
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)