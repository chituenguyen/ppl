grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}

// program  : VAR COLON ID SEMI EOF ;
program:  EOF;

// REALNUMBER : '-'?[0-9]+'e'?'-'?[0-9]+
// |'-'?[0-9]+'e'?'-'?[0-9]*'.''-'?[0-9]+
// |'-'?[0-9]+'.''-'?[0-9]+'e'?'-'?[0-9]+;

// STRINGPASCAL : ['] ((~[']) | (['](~['])?[']))* ['];

// PHP : ([0]|[1-9]([0-9]*([_]?[0-9]+))*){
//     d=""
//     for v in self.text:
//         if v != "_":
//             d+=v
//     self.text = d
// };



// SEMI: ';' ;

// COLON: ':' ;

// VAR: 'Var' ;

fragment SINGQ : '\'';
STRING : SINGQ (~['] | SINGQ SINGQ)* SINGQ;

WS: [\t\r\n]+ -> skip; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;