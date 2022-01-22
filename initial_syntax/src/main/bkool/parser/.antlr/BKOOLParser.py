# Generated from d:\PPL\initial_syntax\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\6\2\23\n\2\r\2\16\2\24\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\"\n\4\f\4\16\4%\13\4\5")
        buf.write("\4\'\n\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5/\n\5\f\5\16\5\62")
        buf.write("\13\5\3\6\3\6\3\6\3\6\7\68\n\6\f\6\16\6;\13\6\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\3\4")
        buf.write("\2A\2\22\3\2\2\2\4\30\3\2\2\2\6\35\3\2\2\2\b*\3\2\2\2")
        buf.write("\n\63\3\2\2\2\f>\3\2\2\2\16@\3\2\2\2\20\23\5\n\6\2\21")
        buf.write("\23\5\4\3\2\22\20\3\2\2\2\22\21\3\2\2\2\23\24\3\2\2\2")
        buf.write("\24\22\3\2\2\2\24\25\3\2\2\2\25\26\3\2\2\2\26\27\7\2\2")
        buf.write("\3\27\3\3\2\2\2\30\31\5\f\7\2\31\32\7\6\2\2\32\33\5\6")
        buf.write("\4\2\33\34\5\16\b\2\34\5\3\2\2\2\35&\7\n\2\2\36#\5\b\5")
        buf.write("\2\37 \7\b\2\2 \"\5\b\5\2!\37\3\2\2\2\"%\3\2\2\2#!\3\2")
        buf.write("\2\2#$\3\2\2\2$\'\3\2\2\2%#\3\2\2\2&\36\3\2\2\2&\'\3\2")
        buf.write("\2\2\'(\3\2\2\2()\7\t\2\2)\7\3\2\2\2*+\5\f\7\2+\60\7\6")
        buf.write("\2\2,-\7\7\2\2-/\7\6\2\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2")
        buf.write("\2\2\60\61\3\2\2\2\61\t\3\2\2\2\62\60\3\2\2\2\63\64\5")
        buf.write("\f\7\2\649\7\6\2\2\65\66\7\7\2\2\668\7\6\2\2\67\65\3\2")
        buf.write("\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3\2\2")
        buf.write("\2<=\7\b\2\2=\13\3\2\2\2>?\t\2\2\2?\r\3\2\2\2@A\7\5\2")
        buf.write("\2A\17\3\2\2\2\b\22\24#&\609")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'body'", "<INVALID>", 
                     "','", "';'", "')'", "'('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "CM", "SM", "RB", "LB", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_funcdecl = 1
    RULE_paramdecl = 2
    RULE_param = 3
    RULE_vardecl = 4
    RULE_typ = 5
    RULE_body = 6

    ruleNames =  [ "program", "funcdecl", "paramdecl", "param", "vardecl", 
                   "typ", "body" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ID=4
    CM=5
    SM=6
    RB=7
    LB=8
    WS=9
    ERROR_CHAR=10
    UNCLOSE_STRING=11
    ILLEGAL_ESCAPE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 14
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 15
                    self.funcdecl()
                    pass


                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.T__0 or _la==BKOOLParser.T__1):
                    break

            self.state = 20
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamdeclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.typ()
            self.state = 23
            self.match(BKOOLParser.ID)
            self.state = 24
            self.paramdecl()
            self.state = 25
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SM)
            else:
                return self.getToken(BKOOLParser.SM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramdecl




    def paramdecl(self):

        localctx = BKOOLParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(BKOOLParser.LB)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.T__0 or _la==BKOOLParser.T__1:
                self.state = 28
                self.param()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.SM:
                    self.state = 29
                    self.match(BKOOLParser.SM)
                    self.state = 30
                    self.param()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 38
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.typ()

            self.state = 41
            self.match(BKOOLParser.ID)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 42
                self.match(BKOOLParser.CM)
                self.state = 43
                self.match(BKOOLParser.ID)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.typ()

            self.state = 50
            self.match(BKOOLParser.ID)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 51
                self.match(BKOOLParser.CM)
                self.state = 52
                self.match(BKOOLParser.ID)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_typ




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.T__0 or _la==BKOOLParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(BKOOLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





