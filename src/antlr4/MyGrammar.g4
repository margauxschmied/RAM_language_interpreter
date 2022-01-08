grammar MyGrammar;

program : code EOF;

code: expr NEWLINE program {}
    | expr {}
    ;

expr: 'R' r1=INT '=' 'R' r2=INT op=('+'|'-') un=INT {
if $r1.text != $r2.text:
    raise ValueError("line "+str($r1.line)+": R"+$r1.text+" != "+"R"+$r2.text)
if $un.text != '1':
    raise ValueError("line "+str($un.line)+": "+$un.text+" != 1")
                                                     } #ZeroUn
    | ('IF'|'if') 'R' r1=INT '!=' zero=INT THEN goto=(GOTOB|GOTOF) n=INT {
if $zero.text != '0':
    raise ValueError("line "+str($zero.line)+": "+$zero.text+" != 0")
} #DeuxTrois
    ;



INT  : [0-9]+  ;
THEN : ('THEN'|'then') ;
GOTOB : ('GOTOB'|'gotob') ;
GOTOF : ('GOTOF'|'gotof') ;
NEWLINE : ('\r'? '\n' | '\r')+ ;
WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;

