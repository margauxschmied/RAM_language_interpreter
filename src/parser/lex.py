import ply.lex as lex

# List of token names.   This is always required


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
    'ID',
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
nondigit = r'([_A-Za-z])'
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


@lex.TOKEN(identifier)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
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


# Build the lexer
lexer = lex.lex()

if __name__ == '__main__':
    data = """BEGIN MACRO name(Rx, Ry)
    R1 = R1 + 1
    R1 = R1 + 1
    R1 = R1 - 1
    if R1 != 0 then gotob 2
    R1 = R1 - 1
    end macro;"""
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
