grammar PlayScript;


classDeclaration
    : CLASS IDENTIFIER
      (EXTENDS typeType)?
      classBody
    ;

classBody
    : '{' classBodyDeclaration* '}'
    ;

classBodyDeclaration
    : ';'
    | memberDeclaration
    ;

memberDeclaration
    : functionDeclaration
    | fieldDeclaration
    // | constructorDeclaration
    // | genericConstructorDeclaration
    // | annotationTypeDeclaration
     | classDeclaration
    // | enumDeclaration
    ;

functionDeclaration
    : typeTypeOrVoid? IDENTIFIER formalParameters
      functionBody
    ;

functionBody
    : block
    | ';'
    ;

typeTypeOrVoid
    : typeType
    | VOID
    ;

qualifiedNameList
    : qualifiedName (',' qualifiedName)*
    ;

formalParameters
    : '(' formalParameterList? ')'
    ;

formalParameterList
    : formalParameter (',' formalParameter)*
    ;

formalParameter
    : variableModifier* typeType variableDeclaratorId
    ;

variableModifier
    : CONST
    | STATIC
    //| annotation
    ;

qualifiedName
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

fieldDeclaration
    : variableDeclarators ';'
    ;

// constructorDeclaration
//     : IDENTIFIER formalParameters (THROWS qualifiedNameList)? constructorBody=block
//     ;

variableDeclarators
    : variableModifier* typeType variableDeclarator (',' variableDeclarator)*
    ;

variableDeclarator
    : variableDeclaratorId ('=' variableInitializer)?
    ;

variableDeclaratorId
    : IDENTIFIER
    ;

variableInitializer
    : arrayInitializer
    | expression
    ;

arrayInitializer
    : '{' (variableInitializer (',' variableInitializer)* (',')? )? '}'
    ;

classType
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

literal
    : integerLiteral
    | floatLiteral
    | STRING_LITERAL
    | BOOL_LITERAL
    | NULL_LITERAL
    ;

integerLiteral
    : DECIMAL_LITERAL
    | HEX_LITERAL
    ;

floatLiteral
    : FLOAT_LITERAL
    ;

// STATEMENTS / BLOCKS
prog
    : blockStatements
    ;

block
    : '{' blockStatements '}'
    ;

blockStatements
    : blockStatement*
    ;

blockStatement
    : variableDeclarators ';'
    | statement
   // | localTypeDeclaration
    | functionDeclaration
    | classDeclaration
    ;

statement
    : blockLabel=block
    // | ASSERT expression (':' expression)? ';'
    | IF parExpression statement (ELSE statement)?
    | FOR '(' forControl ')' statement
    | WHILE parExpression statement
    //| DO statement WHILE parExpression ';'
    //| TRY block (catchClause+ finallyBlock? | finallyBlock)
    //| TRY resourceSpecification block catchClause* finallyBlock?
    //| SWITCH parExpression '{' switchBlockStatementGroup* switchLabel* '}'
    //| SYNCHRONIZED parExpression block
    | RETURN expression? ';'
    //| THROW expression ';'
    //| BREAK IDENTIFIER? ';'
    | BREAK ';'
    //| CONTINUE IDENTIFIER? ';'
    | CONTINUE ';'
    | SEMI
    | statementExpression=expression ';'
    //| identifierLabel=IDENTIFIER ':' statement
    ;

/** Matches cases then statements, both of which are mandatory.
 *  To handle empty cases at the end, we add switchLabel* to statement.
 */
// switchBlockStatementGroup
//     : switchLabel+ blockStatement+
//     ;

// switchLabel
//     : CASE (constantExpression=expression | enumConstantName=IDENTIFIER) ':'
//     | DEFAULT ':'
//     ;

forControl
    : enhancedForControl
    | forInit? ';' expression? ';' forUpdate=expressionList?
    ;

forInit
    : variableDeclarators
    | expressionList
    ;

enhancedForControl
    : variableModifier* typeType variableDeclaratorId ':' expression
    ;

// EXPRESSIONS
parExpression
    : '(' expression ')'
    ;

expressionList
    : expression (',' expression)*
    ;

functionCall
    : IDENTIFIER '(' expressionList? ')'
    | THIS '(' expressionList? ')'
    | SUPER '(' expressionList? ')'
    ;

expression
    : primary
    | expression bop='.'
      ( IDENTIFIER
      | functionCall
    //   | THIS
    //   | NEW nonWildcardTypeArguments? innerCreator
    //   | SUPER superSuffix
    //   | explicitGenericInvocation
      )
    | expression '[' expression ']'
    | functionCall
    // | NEW creator   //不用new关键字，而是用类名相同的函数直接生成对象。
    // | '(' typeType ')' expression
    | expression postfix=('++' | '--')
    | prefix=('+'|'-'|'++'|'--') expression
    | prefix='!' expression
    | expression bop=('*'|'/'|'%') expression
    | expression bop=('+'|'-') expression
    | expression bop=('<=' | '>=' | '>' | '<') expression
    | expression bop=INSTANCEOF typeType
    | expression bop=('==' | '!=') expression
    | expression bop='&&' expression
    | expression bop='||' expression
    | expression bop='?' expression ':' expression
    | <assoc=right> expression
      bop=('=' | '+=' | '-=' | '*=' | '/=' | '%=')
      expression
    // | lambdaExpression // Java8
    // Java 8 functionReference
    // | expression '::' typeArguments? IDENTIFIER
    // | typeType '::' (typeArguments? IDENTIFIER | NEW)
    // | classType '::' typeArguments? NEW
    ;

primary
    : '(' expression ')'
    | THIS
    | SUPER
    | literal
    | IDENTIFIER
    // | typeTypeOrVoid '.' CLASS
    ;

typeList
    : typeType (',' typeType)*
    ;

typeType
    : (classType| functionType | primitiveType) ('[' ']')*
    ;

functionType
    : FUNCTION typeTypeOrVoid '(' typeList? ')'
    ;

primitiveType
    : BOOLEAN
    | INT
    | FLOAT
    | STRING
    ;

// creator
//     : IDENTIFIER arguments
//     ;

// superSuffix
//     : arguments
//     | '.' IDENTIFIER arguments?
//     ;

// arguments
//     : '(' expressionList? ')'
//     ;






// lexer grammar

// Keywords
BOOLEAN:            'boolean';
FLOAT:              'float';
INT:                'int';
VOID:               'void';
// ENUM:               'enum';
STRING:             'string';
FUNCTION:           'function';

CLASS:              'class';
EXTENDS:            'extends';
PRIVATE:            'private';
PROTECTED:          'protected';
PUBLIC:             'public';
INSTANCEOF:         'instanceof';
SUPER:              'super';
THIS:               'this';

CONST:              'const';
STATIC:             'static';
// VOLATILE:           'volatile';

IF:                 'if';
ELSE:               'else';
WHILE:              'while';
FOR:                'for';
BREAK:              'break';
CONTINUE:           'continue';
RETURN:             'return';

// TRY:                'try';
// CATCH:              'catch';
// THROW:              'throw';
// THROWS:             'throws';
// FINALLY:            'finally';

IMPORT:             'import';
NEW:                'new';

// Literals
DECIMAL_LITERAL:    '0' | [1-9] (Digits? | '_'+ Digits);
HEX_LITERAL:        '0' [xX] [0-9a-fA-F] ([0-9a-fA-F_]* [0-9a-fA-F])?;
// OCT_LITERAL:        '0' '_'* [0-7] ([0-7_]* [0-7])? [lL]?;
// BINARY_LITERAL:     '0' [bB] [01] ([01_]* [01])? [lL]?;
FLOAT_LITERAL:      (Digits '.' Digits? | '.' Digits) ExponentPart?
             |       Digits ExponentPart
             ;
// HEX_FLOAT_LITERAL:  '0' [xX] (HexDigits '.'? | HexDigits? '.' HexDigits) [pP] [+-]? Digits [fFdD]?;
BOOL_LITERAL:       'true'
            |       'false'
            ;
// CHAR_LITERAL:       '\'' (~['\\\r\n] | EscapeSequence) '\'';
STRING_LITERAL:     '"' (~["\\\r\n] | EscapeSequence)* '"';
NULL_LITERAL:       'null';

// Separators
LPAREN:             '(';
RPAREN:             ')';
LBRACE:             '{';
RBRACE:             '}';
LBRACK:             '[';
RBRACK:             ']';
SEMI:               ';';
COMMA:              ',';
DOT:                '.';

// Operators
ASSIGN:             '=';
GT:                 '>';
LT:                 '<';
BANG:               '!';
QUESTION:           '?';
COLON:              ':';
EQUAL:              '==';
LE:                 '<=';
GE:                 '>=';
NOTEQUAL:           '!=';
AND:                '&&';
OR:                 '||';
INC:                '++';
DEC:                '--';
ADD:                '+';
SUB:                '-';
MUL:                '*';
DIV:                '/';
MOD:                '%';

ADD_ASSIGN:         '+=';
SUB_ASSIGN:         '-=';
MUL_ASSIGN:         '*=';
DIV_ASSIGN:         '/=';
MOD_ASSIGN:         '%=';
// AND_ASSIGN:         '&=';
// OR_ASSIGN:          '|=';
// XOR_ASSIGN:         '^=';

// Whitespace and comments
WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);

// Identifiers
IDENTIFIER:         Letter LetterOrDigit*;

// Fragment rules
fragment ExponentPart
    : [eE] [+-]? Digits
    ;

fragment EscapeSequence
    : '\\' [btnfr"'\\]
    | '\\' 'u'+ HexDigit HexDigit HexDigit HexDigit
    ;

// fragment HexDigits
//     : HexDigit ((HexDigit | '_')* HexDigit)?
//     ;

fragment HexDigit
    : [0-9a-fA-F]
    ;

fragment Digits
    : [0-9] ([0-9_]* [0-9])?
    ;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;

fragment Letter
    : [a-zA-Z$_]
    // | ~[\u0000-\u007F\uD800-\uDBFF] // covers all characters above 0x7F which are not a surrogate
    // | [\uD800-\uDBFF] [\uDC00-\uDFFF] // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
    ;
