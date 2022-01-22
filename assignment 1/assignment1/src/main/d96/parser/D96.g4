grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (class_declare programclass)+ EOF;

// 2.1 Class declaration
programclass: CLASS 'Program' 'main' LP RP LB 'programclassbody' RB;
class_declare: CLASS identifier (COLON ID)* LP listOfMember RP; 
listOfMember: (attribute | method);

// 2.2
attribute :(mutable | immutable);
mutable: VAR listOfAttributeName COLON typ ASSIGN expression SEMI;
immutable: VAL listOfAttributeName COLON typ ASSIGN expression SEMI;

listOfAttributeName: (identifier|dollarIdentifier) (COMMA DOLA?(identifier|dollarIdentifier))*;

// 2.3 chua xong
method: (identifier|dollarIdentifier) LP listOfParameter? RP blockStatement;

// 3.2
COMMENT : '##' (.)*? '##' -> skip;

// 3.3
identifier :(ID|UNDERSCORE)(ID|UNDERSCORE|INTLIT)*;
dollarIdentifier: DOLA (ID|UNDERSCORE|INTLIT)+;

// 3.7
interger_literal :INT_DEC | OCTAL | HEXADECIMAL | BINARY;
INT_DEC :'0'|[1-9][0-9]*('_'[0-9]+)*{
    d = ""
    for i in self.text:
        if i != "_":
            d += i
    self.text = d
};
OCTAL : '0'[0-7][0-7]*('_'[0-7]+)*{
    d = ""
    for i in self.text:
        if i != "_":
            d += i
    self.text = d
};
HEXADECIMAL: '0'[xX][0-9A-F]+('_'[0-9A-F]+)*{
    d = ""
    for i in self.text:
        if i != "_":
            d += i
    self.text = d
};
BINARY:'0'[bB][0-1]+('_'[0-1]+)*{
    d = ""
    for i in self.text:
        if i != "_":
            d += i
    self.text = d
};

FLOAT_LITERAL :INT_PART+ DOT ([0-9])*{
                    d = ""
                    for i in self.text:
                        if i != "_":
                            d += i
                    self.text = d
                }
                |INT_PART+ EXPONENT{
                    d = ""
                    for i in self.text:
                        if i != "_":
                            d += i
                    self.text = d
                }
                |INT_PART+ DOT ([0-9])* EXPONENT{
                    d = ""
                    for i in self.text:
                        if i != "_":
                            d += i
                    self.text = d
                }
                | DOT ([0-9])* EXPONENT{
                    d = ""
                    for i in self.text:
                        if i != "_":
                            d += i
                    self.text = d
                }
                ;
fragment INT_PART:[1-9][0-9]*('_'[0-9]+)* | '0';
fragment EXPONENT: [eE] SIGN? [0-9]+ ;
fragment SIGN: [+-] ;



BOOLEAN_LITERAL : 'True|False';

STRING_LITERAL: '"' STR_CHAR* '"'
	{
		y = str(self.text)
		self.text = y[1:-1]
	}
	;
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [btnfr"'\\] ;


index_array : 'Array' LB expression_array RB;
expression_array : (expression (COMMA expression)*) | (STRING_LITERAL (COMMA STRING_LITERAL)*) ;

multi_array : 'Array' LB (index_array (COMMA index_array)*) RB;

// 4


// Utilities
CLASS : 'Class';


VAL : 'Val';
VAR : 'Var';

typ : ;

expression: INTLIT ((ADD|SUB|MUL|DIV) INTLIT)*;

listOfParameter:param (SEMI param)*;
param : ID (COMMA ID)* COLON typ;
blockStatement:;




NUMBER_WITH_UNDERSCORE : ([0]|[1-9]([0-9]*([_]?[0-9]+))*){ 
    d=""
    for v in self.text:
        if v != "_":
            d+=v
    self.text = d
};










ID: [a-zA-Z]+;
UNDERSCORE : '_';
INTLIT: [0-9]+;

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

COMMA :',';

DOLA:'$';

COLON: ':';

fragment DOT :'.';


fragment E :'e|E';

ASSIGN : '=';

ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';



WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;