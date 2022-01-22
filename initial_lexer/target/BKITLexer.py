# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write(".\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\31\n\3\f\3\16")
        buf.write("\3\34\13\3\3\3\3\3\3\4\6\4!\n\4\r\4\16\4\"\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\2\2\t\3\2\5\3\7\4\t\5\13")
        buf.write("\6\r\7\17\b\3\2\4\3\2))\4\2\13\f\17\17\2/\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7 \3\2\2\2\t&\3\2\2")
        buf.write("\2\13(\3\2\2\2\r*\3\2\2\2\17,\3\2\2\2\21\22\7)\2\2\22")
        buf.write("\4\3\2\2\2\23\32\5\3\2\2\24\31\n\2\2\2\25\26\5\3\2\2\26")
        buf.write("\27\5\3\2\2\27\31\3\2\2\2\30\24\3\2\2\2\30\25\3\2\2\2")
        buf.write("\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\35\3\2\2")
        buf.write("\2\34\32\3\2\2\2\35\36\5\3\2\2\36\6\3\2\2\2\37!\t\3\2")
        buf.write("\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#$\3\2")
        buf.write("\2\2$%\b\4\2\2%\b\3\2\2\2&\'\13\2\2\2\'\n\3\2\2\2()\13")
        buf.write("\2\2\2)\f\3\2\2\2*+\13\2\2\2+\16\3\2\2\2,-\13\2\2\2-\20")
        buf.write("\3\2\2\2\6\2\30\32\"\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5
    UNTERMINATED_COMMENT = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "SINGQ", "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


