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
    PUSH 'R' r1=INT {$instruction= Instruction(5, $r1.text)}
    | POP 'R' r1=INT {$instruction= Instruction(6, $r1.text)}
    | 'R' r1=INT '=' 'R' r2=INT op=('+'|'-') un=INT  {
if $r1.text != $r2.text:
    raise ValueError("line "+str($r1.line)+": R"+$r1.text+" != "+"R"+$r2.text)
if $un.text != '1':
    raise ValueError("line "+str($un.line)+": "+$un.text+" != 1")
if $op.text=='+':
    $instruction= Instruction(0, $r1.text)
else:
    $instruction= Instruction(1, $r1.text)
}
    | ('IF'|'if') 'R' r1=INT '!=' zero=INT THEN goto=(GOTOB|GOTOF) n=INT {
if $zero.text != '0':
    raise ValueError("line "+str($zero.line)+": "+$zero.text+" != 0")
if $goto.text=='GOTOB' or $goto.text=='gotob':
    $instruction= Instruction(2, $r1.text, $n.text)
else:
    $instruction= Instruction(3, $r1.text, $n.text)
}
    ;


macro returns [Instruction instruction]:
    BEGIN MACRO name='name' list_register code END MACRO ';'  {$instruction=Macro($name.text, list_register.register, $code.instruction)}
;

list_register returns [Register register]:
    'R' r1=INT ',' list_register {$register=Register($r1.text, $list_register.register)}
    | 'R' r1=INT    {$register=Register($r1.text)}
    ;

INT  : [0-9]+  ;
THEN : ('THEN'|'then') ;
GOTOB : ('GOTOB'|'gotob') ;
GOTOF : ('GOTOF'|'gotof') ;
BEGIN : ('BEGIN'|'begin') ;
END : ('END'|'end') ;
MACRO : ('MACRO'|'macro') ;
PUSH : ('PUSH'|'push') ;
POP : ('POP'|'pop') ;
NEWLINE : ('\r'? '\n' | '\r')+ ;
WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;
