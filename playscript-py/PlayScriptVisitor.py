# Generated from PlayScript.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PlayScriptParser import PlayScriptParser
else:
    from PlayScriptParser import PlayScriptParser

# This class defines a complete generic visitor for a parse tree produced by PlayScriptParser.

class PlayScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PlayScriptParser#classDeclaration.
    def visitClassDeclaration(self, ctx:PlayScriptParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#classBody.
    def visitClassBody(self, ctx:PlayScriptParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:PlayScriptParser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:PlayScriptParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:PlayScriptParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#functionBody.
    def visitFunctionBody(self, ctx:PlayScriptParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#typeTypeOrVoid.
    def visitTypeTypeOrVoid(self, ctx:PlayScriptParser.TypeTypeOrVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:PlayScriptParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#formalParameters.
    def visitFormalParameters(self, ctx:PlayScriptParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx:PlayScriptParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#formalParameter.
    def visitFormalParameter(self, ctx:PlayScriptParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#variableModifier.
    def visitVariableModifier(self, ctx:PlayScriptParser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#qualifiedName.
    def visitQualifiedName(self, ctx:PlayScriptParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:PlayScriptParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:PlayScriptParser.VariableDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:PlayScriptParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:PlayScriptParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#variableInitializer.
    def visitVariableInitializer(self, ctx:PlayScriptParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:PlayScriptParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#classType.
    def visitClassType(self, ctx:PlayScriptParser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#literal.
    def visitLiteral(self, ctx:PlayScriptParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:PlayScriptParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#floatLiteral.
    def visitFloatLiteral(self, ctx:PlayScriptParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#prog.
    def visitProg(self, ctx:PlayScriptParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#block.
    def visitBlock(self, ctx:PlayScriptParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#blockStatements.
    def visitBlockStatements(self, ctx:PlayScriptParser.BlockStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#blockStatement.
    def visitBlockStatement(self, ctx:PlayScriptParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#statement.
    def visitStatement(self, ctx:PlayScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#forControl.
    def visitForControl(self, ctx:PlayScriptParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#forInit.
    def visitForInit(self, ctx:PlayScriptParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#enhancedForControl.
    def visitEnhancedForControl(self, ctx:PlayScriptParser.EnhancedForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#parExpression.
    def visitParExpression(self, ctx:PlayScriptParser.ParExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#expressionList.
    def visitExpressionList(self, ctx:PlayScriptParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#functionCall.
    def visitFunctionCall(self, ctx:PlayScriptParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#expression.
    def visitExpression(self, ctx:PlayScriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#primary.
    def visitPrimary(self, ctx:PlayScriptParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#typeList.
    def visitTypeList(self, ctx:PlayScriptParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#typeType.
    def visitTypeType(self, ctx:PlayScriptParser.TypeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#functionType.
    def visitFunctionType(self, ctx:PlayScriptParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlayScriptParser#primitiveType.
    def visitPrimitiveType(self, ctx:PlayScriptParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del PlayScriptParser