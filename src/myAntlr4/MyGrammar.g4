grammar MyGrammar;

@header{
from src.instruction.instruction import Instruction
from src.instruction.register import Register

}

program returns [Instruction instruction]:
    code EOF {$instruction=$code.instruction} # MakeList
    ;

code returns [Instruction instruction]:
    expr NEWLINE code {$instruction =$expr.instruction
$instruction.setNext($code.instruction)}
    | expr {$instruction =$expr.instruction}
    ;

expr returns [Instruction instruction]:
    PUSH R r1=INT {$instruction= Instruction(4, Register($r1.text))}
    | POP R r1=INT {$instruction= Instruction(5, Register($r1.text))}
    | R r1=INT '=' R r2=INT op=('+'|'-') un=INT  {
if $r1.text != $r2.text:
    raise ValueError("line "+str($r1.line)+": R"+$r1.text+" != "+"R"+$r2.text)
if $un.text != '1':
    raise ValueError("line "+str($un.line)+": "+$un.text+" != 1")
if $op.text=='+':
    $instruction= Instruction(0, Register($r1.text))
else:
    $instruction= Instruction(1, Register($r1.text))
}
    | IF R r1=INT '!=' zero=INT THEN goto=(GOTOB|GOTOF) n=INT {
if $zero.text != '0':
    raise ValueError("line "+str($zero.line)+": "+$zero.text+" != 0")
if $goto.text=='GOTOB' or $goto.text=='gotob':
    $instruction= Instruction(2, Register($r1.text), $n.text)
else:
    $instruction= Instruction(3, Register($r1.text), $n.text)
}
    | macro {$instruction=$macro.instruction}
    ;

list_register returns [Register register]:
    R r1=INT ',' list_register {$register=Register($r1.text, $list_register.register)}
    | R r1=INT    {$register=Register($r1.text)}
    ;


macro returns [Instruction instruction]:
    BEGIN MACRO name=MACROIDENTIFIER  macro_list_register ')' NEWLINE code NEWLINE END MACRO ';'  {$instruction=Macro($name.text, macro_list_register.register, $code.instruction)}
;

macro_list_register returns [Register register]:
    r1=RIDENTIFIER ',' list_register {$register=Register($r1.text, $list_register.register)}
    | r1=RIDENTIFIER   {$register=Register($r1.text)}
    ;


INT  : [0-9]+;
R  :  'R';
IF  :  ('IF'|'if');
THEN : ('THEN'|'then');
GOTOB : ('GOTOB'|'gotob');
GOTOF : ('GOTOF'|'gotof');
BEGIN : ('BEGIN'|'begin');
END : ('END'|'end');
MACRO : ('MACRO'|'macro');
PUSH : ('PUSH'|'push');
POP : ('POP'|'pop');

RIDENTIFIER  : 'R'[a-zA-Z][a-zA-Z0-9]*;
MACROIDENTIFIER  : [a-zA-Z][a-zA-Z0-9]* '(';
NEWLINE : ('\r'? '\n' | '\r')+;
WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip;
