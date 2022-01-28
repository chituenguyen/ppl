grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (class_declare)+ EOF;

// 2.1 Class declaration

class_declare: CLASS IDENTIFIER (COLON IDENTIFIER)* LP listOfMember RP; 
// listOfMember: class_Elements|;
// class_Elements : class_Element class_Elements | class_Element;
// class_Element:attribute;
listOfMember: (attribute | method|);

// 2.2
// attribute :(mutable | immutable);
// mutable: VAR listOfAttributeName COLON typ ASSIGN expression SEMI;
// immutable: VAL listOfAttributeName COLON typ ASSIGN expression SEMI;
attribute:('Var'|'Val') listOfAttributeName COLON typ SEMI;
typ : 'Int' | 'Float'|'Boolean'|'String' ;

listOfAttributeName: IDENTIFIER COMMA *listOfAttributeName | IDENTIFIER;

// 2.3 chua xong
method: (IDENTIFIER|DOLLARIDENTIFIER) LB listOfParameter? RB LP blockStatement RP;
listOfParameter:param (SEMI param)*;
param : IDENTIFIER (COMMA IDENTIFIER)* COLON typ;
blockStatement: statement+;
statement:;



// 3.2
COMMENT : '##' (.)*? '##' -> skip;

// 3.3
CLASS:'Class';
IDENTIFIER:([A-Za-z]|'_')+ ([A-Za-z0-9]|'_')* ;

DOLLARIDENTIFIER: DOLA [A-Za-z_]+ [A-Za-z_0-9]*;

// 3.7
interger_literal :INT_DEC | OCTAL | HEXADECIMAL | BINARY;
INT_DEC :'0'|[1-9][0-9]*('_'[0-9]+)*{
    d = ""
    for i in self.text:
        if i != "_":
            d += i
    self.text = d
};
OCTAL : ('00')|'0'[1-7][0-7]*('_'[0-7]+)*{
    d = ""
    for i in self.text:
        if i != "_":
            d += i
    self.text = d
};
HEXADECIMAL: '0'[xX][1-9A-F][0-9A-F]*('_'[0-9A-F]+)*{
    d = ""
    for i in self.text:
        if i != "_":
            d += i
    self.text = d
};
BINARY:('0b0'|'0B0')|'0'[bB]('1')[0-1]*('_'[0-1]+)*{
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

STRING_LITERAL
	: '"' CHARACTER* '"'
	{
		inputstr=str(self.text)
		self.text=inputstr[1:-1]
	}
	;

fragment CHARACTER
	: ~[\b\f\r\n\t"'\\]|ESCAPE_CHAR|DOUBLE_QUOTE_IN_STRING
	;
fragment ESCAPE_CHAR
	: '\\' [bfrnt'\\]
	;
fragment DOUBLE_QUOTE_IN_STRING
	:'\'"'
	;
fragment ESCAPE_CHAR_ILEGAL
	: '\\' ~[bfrnt'\\] 
	| ~'\\'
	;


index_array : 'Array' LB expression_array RB;
expression_array : (expression (COMMA expression)*) | (STRING_LITERAL (COMMA STRING_LITERAL)*) ;
expression: INTLIT ((ADD|SUB|MUL|DIV) INTLIT)*;

multi_array : 'Array' LB (index_array (COMMA index_array)*) RB;

// 4


// Utilities



// VAL : 'Val';
// VAR : 'Var';










// NUMBER_WITH_UNDERSCORE : ([0]|[1-9]([0-9]*([_]?[0-9]+))*){ 
//     d=""
//     for v in self.text:
//         if v != "_":
//             d+=v
//     self.text = d
// };











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


ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
UNCLOSE_STRING
	: '"' CHARACTER* END_A_LINE_SIGN 
	{ 
		unclose_str=str(self.text)
		raise UncloseString(unclose_str[1:])
	};
fragment END_A_LINE_SIGN
	: [\b\t\n\f\r"'\\] | EOF
	;
ILLEGAL_ESCAPE
	: '"' CHARACTER* ESCAPE_CHAR_ILEGAL
	{
		ilegal = str(self.text)
		raise IllegalEscape(ilegal[1:])
	}
	;