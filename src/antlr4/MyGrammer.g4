grammar MyGrammer;

program : code EOF;

code: expr NEWLINE program {}
    | expr {}
    ;

expr: 'R' r1=INT '=' 'R' r2=INT op=('+'|'-') un=INT {} #coucou
    | ('IF'|'if') 'R' r1=INT '!=' zero=INT THEN goto=(GOTOB|GOTOF) n=INT #pomme
    ;



INT  : [0-9]+  ;
THEN : ('THEN'|'then') ;
GOTOB : ('GOTOB'|'gotob') ;
GOTOF : ('GOTOF'|'gotof') ;
NEWLINE : ('\r'? '\n' | '\r')+ ;
WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;

