# Generated from PlayScript.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PlayScriptParser import PlayScriptParser
else:
    from PlayScriptParser import PlayScriptParser

# This class defines a complete listener for a parse tree produced by PlayScriptParser.
class PlayScriptListener(ParseTreeListener):

    # Enter a parse tree produced by PlayScriptParser#classDeclaration.
    def enterClassDeclaration(self, ctx:PlayScriptParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#classDeclaration.
    def exitClassDeclaration(self, ctx:PlayScriptParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#classBody.
    def enterClassBody(self, ctx:PlayScriptParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#classBody.
    def exitClassBody(self, ctx:PlayScriptParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:PlayScriptParser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:PlayScriptParser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:PlayScriptParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:PlayScriptParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:PlayScriptParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:PlayScriptParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#functionBody.
    def enterFunctionBody(self, ctx:PlayScriptParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#functionBody.
    def exitFunctionBody(self, ctx:PlayScriptParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#typeTypeOrVoid.
    def enterTypeTypeOrVoid(self, ctx:PlayScriptParser.TypeTypeOrVoidContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#typeTypeOrVoid.
    def exitTypeTypeOrVoid(self, ctx:PlayScriptParser.TypeTypeOrVoidContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:PlayScriptParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:PlayScriptParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#formalParameters.
    def enterFormalParameters(self, ctx:PlayScriptParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#formalParameters.
    def exitFormalParameters(self, ctx:PlayScriptParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#formalParameterList.
    def enterFormalParameterList(self, ctx:PlayScriptParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#formalParameterList.
    def exitFormalParameterList(self, ctx:PlayScriptParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#formalParameter.
    def enterFormalParameter(self, ctx:PlayScriptParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#formalParameter.
    def exitFormalParameter(self, ctx:PlayScriptParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#variableModifier.
    def enterVariableModifier(self, ctx:PlayScriptParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#variableModifier.
    def exitVariableModifier(self, ctx:PlayScriptParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#qualifiedName.
    def enterQualifiedName(self, ctx:PlayScriptParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#qualifiedName.
    def exitQualifiedName(self, ctx:PlayScriptParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:PlayScriptParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:PlayScriptParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:PlayScriptParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:PlayScriptParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:PlayScriptParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:PlayScriptParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:PlayScriptParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:PlayScriptParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#variableInitializer.
    def enterVariableInitializer(self, ctx:PlayScriptParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#variableInitializer.
    def exitVariableInitializer(self, ctx:PlayScriptParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:PlayScriptParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:PlayScriptParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#classType.
    def enterClassType(self, ctx:PlayScriptParser.ClassTypeContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#classType.
    def exitClassType(self, ctx:PlayScriptParser.ClassTypeContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#literal.
    def enterLiteral(self, ctx:PlayScriptParser.LiteralContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#literal.
    def exitLiteral(self, ctx:PlayScriptParser.LiteralContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:PlayScriptParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:PlayScriptParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#floatLiteral.
    def enterFloatLiteral(self, ctx:PlayScriptParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#floatLiteral.
    def exitFloatLiteral(self, ctx:PlayScriptParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#prog.
    def enterProg(self, ctx:PlayScriptParser.ProgContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#prog.
    def exitProg(self, ctx:PlayScriptParser.ProgContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#block.
    def enterBlock(self, ctx:PlayScriptParser.BlockContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#block.
    def exitBlock(self, ctx:PlayScriptParser.BlockContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#blockStatements.
    def enterBlockStatements(self, ctx:PlayScriptParser.BlockStatementsContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#blockStatements.
    def exitBlockStatements(self, ctx:PlayScriptParser.BlockStatementsContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#blockStatement.
    def enterBlockStatement(self, ctx:PlayScriptParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#blockStatement.
    def exitBlockStatement(self, ctx:PlayScriptParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#statement.
    def enterStatement(self, ctx:PlayScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#statement.
    def exitStatement(self, ctx:PlayScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#forControl.
    def enterForControl(self, ctx:PlayScriptParser.ForControlContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#forControl.
    def exitForControl(self, ctx:PlayScriptParser.ForControlContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#forInit.
    def enterForInit(self, ctx:PlayScriptParser.ForInitContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#forInit.
    def exitForInit(self, ctx:PlayScriptParser.ForInitContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:PlayScriptParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:PlayScriptParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#parExpression.
    def enterParExpression(self, ctx:PlayScriptParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#parExpression.
    def exitParExpression(self, ctx:PlayScriptParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#expressionList.
    def enterExpressionList(self, ctx:PlayScriptParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#expressionList.
    def exitExpressionList(self, ctx:PlayScriptParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#functionCall.
    def enterFunctionCall(self, ctx:PlayScriptParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#functionCall.
    def exitFunctionCall(self, ctx:PlayScriptParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#expression.
    def enterExpression(self, ctx:PlayScriptParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#expression.
    def exitExpression(self, ctx:PlayScriptParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#primary.
    def enterPrimary(self, ctx:PlayScriptParser.PrimaryContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#primary.
    def exitPrimary(self, ctx:PlayScriptParser.PrimaryContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#typeList.
    def enterTypeList(self, ctx:PlayScriptParser.TypeListContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#typeList.
    def exitTypeList(self, ctx:PlayScriptParser.TypeListContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#typeType.
    def enterTypeType(self, ctx:PlayScriptParser.TypeTypeContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#typeType.
    def exitTypeType(self, ctx:PlayScriptParser.TypeTypeContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#functionType.
    def enterFunctionType(self, ctx:PlayScriptParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#functionType.
    def exitFunctionType(self, ctx:PlayScriptParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by PlayScriptParser#primitiveType.
    def enterPrimitiveType(self, ctx:PlayScriptParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by PlayScriptParser#primitiveType.
    def exitPrimitiveType(self, ctx:PlayScriptParser.PrimitiveTypeContext):
        pass



del PlayScriptParser