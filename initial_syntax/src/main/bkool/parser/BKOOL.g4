grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
// mptype 'main' LB RB LP body? RP

program: (vardecl|funcdecl)+ EOF;

// funcdecl :typ (ID(RB (vardecl)SM+)LB body) ;

funcdecl :typ ID paramdecl body;
paramdecl: LB (param (SM param)*)? RB;
param : typ (ID (CM ID)*);



vardecl : typ (ID(CM ID)*)SM ;

typ : ('int'|'float');

ID: [a-zA-Z]+;

body: 'body';

CM :',';
SM : ';';
RB :')';
LB :'(';



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;