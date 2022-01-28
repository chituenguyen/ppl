# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declare.
    def visitClass_declare(self, ctx:D96Parser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listOfMember.
    def visitListOfMember(self, ctx:D96Parser.ListOfMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mutable.
    def visitMutable(self, ctx:D96Parser.MutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#immutable.
    def visitImmutable(self, ctx:D96Parser.ImmutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listOfAttributeName.
    def visitListOfAttributeName(self, ctx:D96Parser.ListOfAttributeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier.
    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dollarIdentifier.
    def visitDollarIdentifier(self, ctx:D96Parser.DollarIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#interger_literal.
    def visitInterger_literal(self, ctx:D96Parser.Interger_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_array.
    def visitIndex_array(self, ctx:D96Parser.Index_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_array.
    def visitExpression_array(self, ctx:D96Parser.Expression_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_array.
    def visitMulti_array(self, ctx:D96Parser.Multi_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ.
    def visitTyp(self, ctx:D96Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listOfParameter.
    def visitListOfParameter(self, ctx:D96Parser.ListOfParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockStatement.
    def visitBlockStatement(self, ctx:D96Parser.BlockStatementContext):
        return self.visitChildren(ctx)



del D96Parser