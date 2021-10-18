from frontend import *

'''
 * 代表Return语句的返回值
'''
class ReturnObject():
    def __init__(self, value):
        self.returnValue = value  # 真正的返回值

    # 在打印时输出ReturnObject
    def toString() -> str:
        return "ReturnObject"

'''
 * 用于代表一个Break语句的对象
'''
class BreakObject():
    def __init__(self):
        pass
    # 在打印时输出Break
    def toString(self) -> str:
        return "Break"
# 创建唯一实例
breakObject = BreakObject()

'''
 * PlayScript的对象
 * 本意是用来表示一个对象内部的field-value pairs。也可以用来装栈帧里的变量
'''
class PlayObject():    
    def __init__(self):
        # 成员变量, Map<Variable, Object>
        self.fields = {}

    def getValue(self, variable:Variable):
        rtn = self.fields.get(variable, None)
        # TODO 父类的属性如何返回？还是说都在这里了？

        # //替换成自己的NullObject
        # if (rtn == null){
        #     rtn = NullObject.instance();
        # }
        return rtn

    def setValue(self, variable:Variable, value):
        self.fields[variable] = value

'''
 * 存放一个函数运行时的本地变量的值，包括参数的值
'''
class FunctionObject(PlayObject):
    def __init__(self, function:Function):  # symbol/type/scope
        super().__init__()
        self.function = function
        '''
         * 接收者所在的scope。缺省是function的enclosingScope，也就是词法的Scope。
         * 当赋值给一个函数型变量的时候，要修改receiverEnclosingScope等于这个变量的enclosingScope。
        '''
        self.receiver:Variable = None

    def setFunction(self, function:Function):
          self.function = function

class StackFrame():
    def __init__(self, scope):
        if isinstance(scope, BlockScope):
            self.scope = scope  # 该frame所对应的scope
            self.object:PlayObject = PlayObject()  # 实际存放变量的地方
        elif isinstance(scope, FunctionObject):
            # 为函数调用，创建一个StackFrame
            object = scope
            self.scope = object.function
            self.object = object
        '''
        * 放parent scope所对应的frame的指针，就叫parentFrame吧，便于提高查找效率。
        * 规则：如果是同一级函数调用，跟上一级的parentFrame相同；
        * 如果是下一级的函数调用或For、If等block，parentFrame是自己；
        * 如果是一个闭包（如何判断？），那么要带一个存放在堆里的环境。
        '''
        self.parentFrame:StackFrame = None
    
    # 本栈桢里有没有包含某个变量的数据
    def contains(self, variable:Variable):
        if self.object and self.object.fields:
            return (variable in self.object.fields)
        return False

    def toString(self) -> str:
        rtn = self.scope.toString()
        if self.parentFrame:
            rtn += " -> " + self.parentFrame.toString()
        return rtn

# 对栈中的值的引用
class LValue():
    def getValue():
        pass
    def setValue(value):
        pass
    def getVariable() -> Variable:
        pass
    def getValueContainer() -> PlayObject:
        pass
    # def getFrame() -> StackFrame:
    #   pass

# 自己实现的左值对象
class MyLValue(LValue):
    def __init__(self, valueContainer:PlayObject, variable:Variable):
        self.valueContainer = valueContainer
        self.variable = variable

    def getValue(self):
        return self.valueContainer.getValue(self.variable)

    def setValue(self, value):
        self.valueContainer.setValue(self.variable, value)
        # 如果variable是函数型变量，那改变 functionObject.receiver
        if isinstance(value, FunctionObject):
            value.receiver = self.variable

    def getVariable(self):
        return self.variable

    def toString(self):
        return "LValue of " + self.variable.name + " : " + self.getValue()

    def getValueContainer(self) -> PlayObject:
        return self.valueContainer



''' AST执行器。利用语义信息(AnnotatedTree)，在AST上解释执行脚本 '''

class ASTEvaluator(PlayScriptVisitor):

    def __init__(self, at:AnnotatedTree):
        self.at = at  # 之前的编译结果
        self.stack:List[StackFrame] = []

        self.traceStackFrame = False
        self.traceFunctionCall = False

    ############################################################
    # 运行时 栈桢的管理
    '''
     * 栈桢入栈
     * 其中最重要的任务，是要保证栈桢的parentFrame设置正确。否则：
     * (1) 随着栈的变深，查找变量的性能会降低；
     * (2) 甚至有可能找错栈桢，比如在递归(直接或间接)的场景下。
    '''
    def pushStack(self, frame:StackFrame):
        if len(self.stack) > 0:
            # 从栈顶到栈底依次查找
            i:int = len(self.stack) - 1
            while i > 0:
                f:StackFrame = self.stack[i]
                # 如果新加入的栈桢，跟某个已有的栈桢的enclosingScope是一样的，那么这俩的parentFrame也一样。
                # 因为它们原本就是同一级的。
                # 比如：
                # void foo(){};
                # void bar(foo());
                # 或者：
                # void foo();
                # if (...){
                #     foo();
                # }
                if f.scope.enclosingScope == frame.scope.enclosingScope:
                    frame.parentFrame = f.parentFrame
                    break
                # 如果新加入的栈桢，是某个已有的栈桢的下一级，那么就把这个父子关系建立起来。比如：
                # void foo(){
                #     if (...){  //把这个块往栈桢里加的时候，就符合这个条件。
                #     }
                # }
                elif f.scope == frame.scope.enclosingScope:
                    frame.parentFrame = f
                    break
                # 这是针对函数可能是一等公民的情况。这个时候，函数运行时的作用域，与声明时的作用域会不一致。
                # 这里设计的“receiver”的机制，意思是这个函数是被哪个变量接收了。要按照这个receiver的作用域来判断。
                elif isinstance(frame.object, FunctionObject):
                    functionObject:FunctionObject = frame.object
                    if functionObject.receiver and functionObject.receiver.enclosingScope == f.scope:
                        frame.parentFrame = f
                        break
                i -= 1

            if frame.parentFrame is None:
                # 这里不会发生？
                frame.parentFrame = self.stack[-1]

        self.stack.append(frame)

        if self.traceStackFrame:
            self.dumpStackFrame()

    def popStack(self):
        self.stack.pop()

    def dumpStackFrame(self):
        print("\nStack Frames ----------------")
        for frame in self.stack:
            print(frame.toString())
        print("-----------------------------\n")


    def getLValue(self, variable:Variable) -> LValue:
        f:StackFrame = self.stack[-1]
        valueContainer:PlayObject = None
        while f:
            if f.scope.containsSymbol(variable):
                valueContainer = f.object
                break
            f = f.parentFrame

        # 通过正常的作用域找不到，就从闭包里找
        # PlayObject中可能有一些变量，其作用域跟 StackFrame.scope 是不同的。
        if valueContainer is None:
            f = self.stack[-1]
            while f:
                if f.contains(variable):
                    valueContainer = f.object
                    break
                f = f.parentFrame

        lvalue = MyLValue(valueContainer, variable)
        return lvalue


    ############################################################
    # 为闭包获取环境变量的值
    '''
     * 为闭包获取环境变量的值
     * @param function 闭包所关联的函数。这个函数会访问一些环境变量。
     * @param valueContainer 存放环境变量的值的容器
    '''
    def getClosureValues(self, function:Function, valueContainer:PlayObject):
        if function.closureVariables:
            for var in function.closureVariables:
                lValue:LValue = self.getLValue(var)  # 现在还可以从栈里取，退出函数以后就不行了
                value = lValue.getValue()
                valueContainer.setValue(var, value)

    ############################################################
    # 内置函数

    # 硬编码的println方法
    def println(self, ctx:PlayScriptParser.FunctionCallContext):
        if ctx.expressionList():
            value = self.visitExpressionList(ctx.expressionList())
            if isinstance(value, LValue):
                value = value.getValue()
            print(value)
        else:
            print()

    ############################################################
    # 各种运算
    def add(self, obj1, obj2, targetType:Type):
        rtn = None
        if targetType == String:
            rtn = str(obj1) + str(obj2)
        elif targetType == Integer:
            rtn = obj1 + obj2
        elif targetType == Float:
            rtn = obj1 + obj2
        else:
            print("unsupported add operation")
        return rtn

    def minus(self, obj1, obj2, targetType:Type):
        rtn = None
        if targetType == Integer:
            rtn = obj1 - obj2
        elif targetType == Float:
            rtn = obj1 - obj2
        else:
            print("unsupported minus operation")
        return rtn

    def mul(self, obj1, obj2, targetType:Type):
        rtn = None
        if targetType == Integer:
            rtn = obj1 * obj2
        elif targetType == Float:
            rtn = obj1 * obj2
        else:
            print("unsupported mul operation")
        return rtn
    
    def div(self, obj1, obj2, targetType:Type):
        # TODO 检查 devided by zero 的错误
        rtn = None
        if targetType == Integer:
            rtn = obj1 / obj2
        elif targetType == Float:
            rtn = obj1 / obj2
        else:
            print("unsupported div operation")
        return rtn

    def EQ(self, obj1, obj2, targetType:Type):
        rtn = False
        if targetType == Integer:
            rtn = int(obj1) == int(obj2)
        elif targetType == Float:
            rtn = float(obj1) == float(obj2)
        # 对于对象实例、函数，直接比较对象引用
        else:
            rtn = obj1 == obj2
        return rtn
    
    def GE(self, obj1, obj2, targetType:Type):
        rtn = False
        if targetType == Integer:
            rtn = int(obj1) >= int(obj2)
        elif targetType == Float:
            rtn = float(obj1) >= float(obj2)
        # 对于函数，不支持比较大小。对于对象，不支持运算符重载
        return rtn
    
    def GT(self, obj1, obj2, targetType:Type):
        rtn = False
        if targetType == Integer:
            rtn = int(obj1) > int(obj2)
        elif targetType == Float:
            rtn = float(obj1) > float(obj2)
        # 对于函数，不支持比较大小。对于对象，不支持运算符重载
        return rtn
    
    def LE(self, obj1, obj2, targetType:Type):
        rtn = False
        if targetType == Integer:
            rtn = int(obj1) <= int(obj2)
        elif targetType == Float:
            rtn = float(obj1) <= float(obj2)
        # 对于函数，不支持比较大小。对于对象，不支持运算符重载
        return rtn

    def LT(self, obj1, obj2, targetType:Type):
        rtn = False
        if targetType == Integer:
            rtn = int(obj1) < int(obj2)
        elif targetType == Float:
            rtn = float(obj1) < float(obj2)
        # 对于函数，不支持比较大小。对于对象，不支持运算符重载
        return rtn

    ############################################################
    # visit每个节点

    def visitBlock(self, ctx:PlayScriptParser.BlockContext):
        scope:BlockScope = self.at.node2Scope.get(ctx, None)
        if scope:  # 有些block是不对应scope的，比如函数底下的block
            frame = StackFrame(scope)
            # frame.parentFrame = stack.peek();
            self.pushStack(frame)
        rtn = self.visitBlockStatements(ctx.blockStatements())
        if scope:
            self.popStack()
        return rtn

    def visitBlockStatement(self, ctx:PlayScriptParser.BlockStatementContext):
        rtn = None
        if ctx.variableDeclarators():
            rtn = self.visitVariableDeclarators(ctx.variableDeclarators())
        elif ctx.statement():
            rtn = self.visitStatement(ctx.statement())
        return rtn

    def visitExpression(self, ctx:PlayScriptParser.ExpressionContext):
        rtn = None
        if ctx.bop and len(ctx.expression()) >= 2:
            ## TODO 还未支持 ? : 三目运算符
            left = self.visitExpression(ctx.expression(0))
            right = self.visitExpression(ctx.expression(1))
            leftObject = left
            rightObject = right

            if isinstance(left, LValue):
                leftObject = left.getValue()
            if isinstance(right, LValue):
                rightObject = right.getValue()

            # 本节点期待的数据类型
            type:Type = self.at.typeOfNode[ctx]

            # 左右两个子节点的类型
            type1 = self.at.typeOfNode[ctx.expression(0)]
            type2 = self.at.typeOfNode[ctx.expression(1)]

            bop_type = ctx.bop.type
            if bop_type == PlayScriptParser.ADD:
                rtn = self.add(leftObject, rightObject, type)
            elif bop_type == PlayScriptParser.SUB:
                rtn = self.minus(leftObject, rightObject, type)
            elif bop_type == PlayScriptParser.MUL:
                rtn = self.mul(leftObject, rightObject, type)
            elif bop_type == PlayScriptParser.DIV:
                rtn = self.div(leftObject, rightObject, type)
            elif bop_type == PlayScriptParser.EQUAL:
                rtn = self.EQ(leftObject, rightObject, PrimitiveType.getUpperType(type1, type2))
            elif bop_type == PlayScriptParser.NOTEQUAL:
                rtn = not self.EQ(leftObject, rightObject, PrimitiveType.getUpperType(type1, type2))
            elif bop_type == PlayScriptParser.LE:
                rtn = self.LE(leftObject, rightObject, PrimitiveType.getUpperType(type1, type2))
            elif bop_type == PlayScriptParser.LT:
                rtn = self.LT(leftObject, rightObject, PrimitiveType.getUpperType(type1, type2))
            elif bop_type == PlayScriptParser.GE:
                rtn = self.GE(leftObject, rightObject, PrimitiveType.getUpperType(type1, type2))
            elif bop_type == PlayScriptParser.GT:
                rtn = self.GT(leftObject, rightObject, PrimitiveType.getUpperType(type1, type2))
            elif bop_type == PlayScriptParser.AND:
                rtn = leftObject and rightObject
            elif bop_type == PlayScriptParser.OR:
                rtn = leftObject or rightObject
            elif bop_type == PlayScriptParser.ASSIGN:
                # 注意：这里赋值，不用做类型检查，因为前面语义分析已经做了
                if isinstance(left, LValue):
                    left.setValue(rightObject)
                    rtn = right
                else:
                    print("Unsupported feature during assignment")
                    raise Exception("ERROR")
            elif bop_type == PlayScriptParser.ADD_ASSIGN:
                # 注意：这里赋值，不用做类型检查，因为前面语义分析已经做了
                if isinstance(left, LValue):
                    rtn = self.add(leftObject, rightObject, type)
                    left.setValue(rtn)
                else:
                    print("Unsupported feature during add assignment")
                    raise Exception("ERROR")
            elif bop_type == PlayScriptParser.SUB_ASSIGN:
                # 注意：这里赋值，不用做类型检查，因为前面语义分析已经做了
                if isinstance(left, LValue):
                    rtn = self.minus(leftObject, rightObject, type)
                    left.setValue(rtn)
                else:
                    print("Unsupported feature during add assignment")
                    raise Exception("ERROR")
            elif bop_type == PlayScriptParser.MUL_ASSIGN:
                # 注意：这里赋值，不用做类型检查，因为前面语义分析已经做了
                if isinstance(left, LValue):
                    rtn = self.mul(leftObject, rightObject, type)
                    left.setValue(rtn)
                else:
                    print("Unsupported feature during add assignment")
                    raise Exception("ERROR")
            elif bop_type == PlayScriptParser.DIV_ASSIGN:
                # 注意：这里赋值，不用做类型检查，因为前面语义分析已经做了
                if isinstance(left, LValue):
                    rtn = self.div(leftObject, rightObject, type)
                    left.setValue(rtn)
                else:
                    print("Unsupported feature during add assignment")
                    raise Exception("ERROR")
        elif ctx.primary():
            rtn = self.visitPrimary(ctx.primary())
        elif ctx.postfix:
            # 后缀运算，例如：i++ 或 i--
            value = self.visitExpression(ctx.expression(0))
            lValue:LValue = None
            type = self.at.typeOfNode.get(ctx.expression(0))
            if isinstance(value, LValue):
                lValue = value
                value = lValue.getValue()
            else:
                # 必须能取左值
                raise Exception("ERROR")
            token_type = ctx.postfix.type
            if token_type == PlayScriptParser.INC:
                if type == Integer:
                    lValue.setValue(value + 1)
                    rtn = value
            elif token_type == PlayScriptParser.DEC:
                if type == Integer:
                    lValue.setValue(value - 1)
                    rtn = value
        elif ctx.prefix:
            # 前缀操作，例如：++i 或 --i  或 !i
            value = self.visitExpression(ctx.expression(0))
            lValue:LValue = None
            type = self.at.typeOfNode.get(ctx.expression(0))
            if isinstance(value, LValue):
                lValue = value
                value = lValue.getValue()
            token_type = ctx.prefix.type
            if token_type == PlayScriptParser.INC:
                # TODO 这里必须用左值
                if type == Integer:
                    lValue.setValue(value + 1)
                    rtn = value + 1
            elif token_type == PlayScriptParser.DEC:
                # TODO 这里必须用左值
                if type == Integer:
                    lValue.setValue(value - 1)
                    rtn = value - 1
            elif token_type == PlayScriptParser.BANG:
                rtn = not value
        elif ctx.functionCall():  # functionCall
            rtn = self.visitFunctionCall(ctx.functionCall())
        return rtn

    def visitExpressionList(self, ctx:PlayScriptParser.ExpressionListContext):
        rtn = None
        for child in ctx.expression():
            rtn = self.visitExpression(child)
        # 这里只返回最后一个表达式的结果。其实rtn并不重要，上一层并不使用这个rtn，单纯地只是为了执行所有的表达式语句罢了，用在 forInit 和 forUpdate 语句中
        return rtn

    def visitForInit(self, ctx:PlayScriptParser.ForInitContext):
        rtn = None
        if ctx.variableDeclarators():
            rtn = self.visitVariableDeclarators(ctx.variableDeclarators())
        elif ctx.expressionList():
            rtn = self.visitExpressionList(ctx.expressionList())
        return rtn

    def visitLiteral(self, ctx:PlayScriptParser.LiteralContext):
        rtn = None
        # 整数
        if ctx.integerLiteral():
            rtn = self.visitIntegerLiteral(ctx.integerLiteral())
        # 浮点数
        elif ctx.floatLiteral():
            rtn = self.visitFloatLiteral(ctx.floatLiteral())
        # 布尔值
        elif ctx.BOOL_LITERAL():
            if ctx.BOOL_LITERAL().getText() == "true":
                rtn = True
            else:
                rtn = False
        # 字符串
        elif ctx.STRING_LITERAL():
            # TODO 考虑转义字符
            rtn = ctx.STRING_LITERAL().getText()
            rtn = rtn[1:]
            rtn = rtn[:-1]
        # null字面量
        elif ctx.NULL_LITERAL():
            # rtn = NullObject.instance()
            rtn = None
        return rtn

    def visitIntegerLiteral(self, ctx:PlayScriptParser.IntegerLiteralContext):
        rtn = None
        if ctx.DECIMAL_LITERAL():
            rtn = int(ctx.DECIMAL_LITERAL().getText())
        else:
            # TODO 处理 HEX LITERAL
            pass
        return rtn

    def visitFloatLiteral(self, ctx:PlayScriptParser.FloatLiteralContext):
        return float(ctx.getText())

    def visitParExpression(self, ctx:PlayScriptParser.ParExpressionContext):
        return self.visitExpression(ctx.expression())

    def visitPrimary(self, ctx:PlayScriptParser.PrimaryContext):
        rtn = None
        # 字面量
        if ctx.literal():
            rtn = self.visitLiteral(ctx.literal())
        # 变量
        elif ctx.IDENTIFIER():
            symbol:Symbol = self.at.symbolOfNode[ctx]
            if isinstance(symbol, Variable):
                rtn = self.getLValue(symbol)
            elif isinstance(symbol, Function):
                obj:FunctionObject = FunctionObject(symbol)
                rtn = obj
        # 括号括起来的表达式
        elif ctx.expression():
            rtn = self.visitExpression(ctx.expression())
        return rtn

    def visitPrimitiveType(self, ctx:PlayScriptParser.PrimitiveTypeContext):
        rtn = None
        if ctx.INT():
            rtn = PlayScriptParser.INT
        elif ctx.FLOAT():
            rtn = PlayScriptParser.FLOAT
        elif ctx.STRING():
            rtn = PlayScriptParser.STRING
        elif ctx.BOOLEAN():
            rtn = PlayScriptParser.BOOLEAN
        return rtn

    def visitStatement(self, ctx:PlayScriptParser.StatementContext):
        rtn = None
        if ctx.statementExpression:
            rtn = self.visitExpression(ctx.statementExpression)
        elif ctx.IF():
            condition:bool = self.visitParExpression(ctx.parExpression())
            if condition:
                rtn = self.visitStatement(ctx.statement(0))
            elif ctx.ELSE():
                rtn = self.visitStatement(ctx.statement(1))
        # while循环
        elif ctx.WHILE():
            if ctx.parExpression().expression() and ctx.statement(0):
                while True:
                    # 每次循环都要计算一下循环条件
                    condition:bool = True
                    value = self.visitExpression(ctx.parExpression().expression())
                    if isinstance(value, LValue):
                        condition:bool = value.getValue()
                    else:
                        condition:bool = value
                    if condition:
                        # 执行while后面的语句
                        rtn = self.visitStatement(ctx.statement(0))
                        # break
                        if isinstance(rtn, BreakObject):
                            rtn = None  # 清除BreakObject，也就是只跳出一层循环，否则会继续向外层返回 breakObject，导致一个break就能退出所有循环，不符合预期的语义设计
                            break
                        # return
                        elif isinstance(rtn, ReturnObject):
                            break
                        # 注意：考虑到在 for/while循环、函数体内出现 break/return 语句的各种情况，似乎这里该有很多异常情况要处理
                        # 但因为前面的语义分析阶段已经检查并排除了所以可能的异常，所以这里不用担心。（语义分析阶段对 break/return 的合法性检查还不够完整！）
                    else:
                        break
        # for循环
        elif ctx.FOR():
            # 添加 StackFrame
            scope:BlockScope = self.at.node2Scope[ctx]
            frame:StackFrame = StackFrame(scope)
            # frame.parentFrame = stack.peek();
            self.pushStack(frame)

            forControl:PlayScriptParser.ForControlContext = ctx.forControl()
            if forControl.enhancedForControl():
                # TODO
                pass
            else:
                # 初始化部分执行一次
                if forControl.forInit():
                    rtn = self.visitForInit(forControl.forInit())

                while True:
                    condition:bool = True  # 如果没有条件判断部分，意味着一直循环
                    if forControl.expression():
                        value = self.visitExpression(forControl.expression())
                        if isinstance(value, LValue):
                            condition:bool = value.getValue()
                        else:
                            condition:bool = value

                    if condition:
                        # 执行for的语句体
                        rtn = self.visitStatement(ctx.statement(0))
                        # 处理break
                        if isinstance(rtn, BreakObject):
                            rtn = None  # 清除BreakObject，也就是只跳出一层循环，否则会继续向外层返回 breakObject，导致一个break就能退出所有循环，不符合预期的语义设计
                            break
                        # return
                        elif isinstance(rtn, ReturnObject):
                            break
                        # 执行forUpdate，通常是“i++”这样的语句。这个执行顺序不能出错
                        if forControl.forUpdate:
                            self.visitExpressionList(forControl.forUpdate)
                    else:
                        break
            # 去掉StackFrame
            self.popStack()
        # block
        elif ctx.blockLabel:
            rtn = self.visitBlock(ctx.blockLabel)
        # break语句
        elif ctx.BREAK():
            rtn = breakObject
        # return语句
        elif ctx.RETURN():
            rtn = None
            if ctx.expression():
                rtn = self.visitExpression(ctx.expression())
                # return语句应该不需要左值   //TODO 其它取左值的地方也需要优化，目前都是取左值。统统返回左值，如果上层需要的是右值，再转成右值。左值的表达能力比右值强
                if isinstance(rtn, LValue):
                    rtn = rtn.getValue()
                # 把闭包涉及的环境变量都打包带走
                if isinstance(rtn, FunctionObject):
                    functionObject:FunctionObject = rtn
                    self.getClosureValues(functionObject.function, functionObject)
                    # function所需要的ClosureVariable在语义分析环节已经记录，这里要在当下的作用域取出那些闭包变量对应的值，记录在functionObject（PlayObject）里，作为这个FunctionObject独有的闭包环境变量
                    # 注意，语义分析在计算闭包变量时，可能算多了，比如把某个全局变量算了进来，这里没关系，因为后续执行这个函数变量对应的函数时，是优先按作用域取值的，作用域里都没有，才从闭包环境里取
                    # 这只是一种闭包实现方式而已
            # 把真实的返回值封装在一个ReturnObject对象里，告诉visitBlockStatements停止执行下面的语句
            rtn = ReturnObject(rtn)
        # 刚开始看，不明白 statement语句为什么需要返回值，实际上这是为了实现 break/return 功能所需的设计
        # statement 语句共有3种返回值：breakObject、returnObject、other，后续在处理这个返回值时，有4个原则：
        #（1）blockStatements，若其某个语句返回了 break/return，必须直接返回，不再执行后面的语句，同时向上传递 break/return
        #（2）for/while 每次执行其statement语句，都要检查返回值，若为break，则退出循环，并内部消化掉（将rtn置为None）；若为return，则退出循环，并且向上传递return
        #（3）functionCall表达式，函数体执行过程中，若其某个语句返回了 return，必须直接返回，不再执行后面的语句。并且functionCall表达式语句，需要消化掉return（取出returnValue向上返回）
        #（4）其余语句，返回下级语句的返回值即可，不需要特别处理
        # PS：如果没有及时消化掉 break，会出现：嵌套的多层循环深处，一个break就退出了所有循环
        # PS：如果没有及时消化掉 return，会出现：但凡执行了某个函数调用（FunctionCall)，它的一个return，就让程序直接终止并退出了
        # 注意：break/return的功能实现，还依赖于语义分析阶段检查 break/return 的合法性：break必须处在for/while里，return必须处在函数体里
        return rtn

    def visitTypeType(self, ctx:PlayScriptParser.TypeTypeContext):
        return self.visitPrimitiveType(ctx.primitiveType())

    def visitVariableDeclarator(self, ctx:PlayScriptParser.VariableDeclaratorContext):
        rtn = None
        lValue:LValue = self.visitVariableDeclaratorId(ctx.variableDeclaratorId())
        if ctx.variableInitializer():
            rtn = self.visitVariableInitializer(ctx.variableInitializer())
            if isinstance(rtn, LValue):
                rtn = rtn.getValue()
            lValue.setValue(rtn)
        return rtn

    def visitVariableDeclaratorId(self, ctx:PlayScriptParser.VariableDeclaratorIdContext):
        rtn = None
        symbol:Variable = self.at.symbolOfNode[ctx]
        rtn = self.getLValue(symbol)
        return rtn

    def visitVariableDeclarators(self, ctx:PlayScriptParser.VariableDeclaratorsContext):
        rtn = None
        # Integer typeType = (Integer)visitTypeType(ctx.typeType()); //后面要利用这个类型信息
        for child in ctx.variableDeclarator():
            rtn = self.visitVariableDeclarator(child)
        return rtn

    def visitVariableInitializer(self, ctx:PlayScriptParser.VariableInitializerContext):
        rtn = None
        if ctx.expression():
            rtn = self.visitExpression(ctx.expression())
        return rtn

    def visitBlockStatements(self, ctx:PlayScriptParser.BlockStatementsContext):
        rtn = None
        for child in ctx.blockStatement():
            rtn = self.visitBlockStatement(child)
            # 如果返回的是break，那么不执行下面的statement
            if isinstance(rtn, BreakObject):
                break
            # 碰到Return, 退出函数
            # TODO 要能层层退出一个个block，弹出一个个栈桢
            elif isinstance(rtn, ReturnObject):
                break
            # 注意：按这里的执行逻辑，在全局作用域下，break 和 return 都能让程序中断执行。但这种情况实际上不会出现，因为前面的语义分析阶段已经对 return/break 的合法性进行了检查
        return rtn

    def visitProg(self, ctx:PlayScriptParser.ProgContext):
        rtn = None
        self.pushStack(StackFrame(self.at.node2Scope[ctx]))
        rtn = self.visitBlockStatements(ctx.blockStatements())
        self.popStack()
        return rtn

    def visitFunctionCall(self, ctx:PlayScriptParser.FunctionCallContext):
        rtn = None
        functionName = ctx.IDENTIFIER().getText()  # 这是调用时的名称，不一定是真正的函数名，还可能是函数型变量的变量名

        if functionName == "println":
            # TODO 临时代码，用于打印输出
            self.println(ctx)
            return rtn

        # 在上下文中查找出函数，并根据需要创建 FunctionObject
        functionObject:FunctionObject = self.getFuntionObject(ctx)

        # 计算参数值
        paramValues = self.calcParamValues(ctx)

        if self.traceFunctionCall:
            print("\n>> FunctionCall : " + ctx.getText())

        rtn = self.functionCall(functionObject, paramValues)
        return rtn

    # 计算某个函数调用时的参数值
    def calcParamValues(self, ctx:PlayScriptParser.FunctionCallContext):
        paramValues = []
        if ctx.expressionList():
            for exp in ctx.expressionList().expression():
                value = self.visitExpression(exp)
                if isinstance(value, LValue):
                    value = value.getValue()
                paramValues.append(value)
        return paramValues

    '''
     * 根据函数调用的上下文，返回一个FunctionObject。
     * 对于函数类型的变量，这个functionObject是存在变量里的；
     * 对于普通的函数调用，此时创建一个。
    '''
    def getFuntionObject(self, ctx:PlayScriptParser.FunctionCallContext) -> FunctionObject:
        # if (ctx.IDENTIFIER() == null) return null;  //暂时不支持this和super

        function:Function = None
        functionObject:FunctionObject = None
        symbol:Symbol = self.at.symbolOfNode[ctx]
        # 函数类型的变量
        if isinstance(symbol, Variable):
            variable = symbol
            lValue:LValue = self.getLValue(variable)
            value = lValue.getValue()
            if isinstance(value, FunctionObject):
                functionObject = value
                function = functionObject.function
        # 普通函数
        elif isinstance(symbol, Function):
            function = symbol
        # 报错
        else:
            functionName = ctx.IDENTIFIER().getText()
            self.at.log("unable to find function or function variable " + functionName, ctx)
            raise Exception("boom")
            # return None

        if functionObject is None:
            functionObject = FunctionObject(function)
        return functionObject

    # 执行一个函数的方法体。需要先设置参数值，然后再执行代码
    def functionCall(self, functionObject:FunctionObject, paramValues):
        rtn = None
        # 添加函数的栈桢
        functionFrame:StackFrame = StackFrame(functionObject)
        self.pushStack(functionFrame)

        # 给参数赋值，这些值进入functionFrame
        functionCode:PlayScriptParser.FunctionDeclarationContext = functionObject.function.ctx
        if functionCode.formalParameters().formalParameterList():
            for i in range(len(functionCode.formalParameters().formalParameterList().formalParameter())):
                param:PlayScriptParser.FormalParameterContext = functionCode.formalParameters().formalParameterList().formalParameter()[i]
                lValue:LValue = self.visitVariableDeclaratorId(param.variableDeclaratorId())
                lValue.setValue(paramValues[i])

        # 调用函数（方法）体
        rtn = self.visitFunctionDeclaration(functionCode)

        # 弹出函数栈帧
        self.popStack()

        # 这里消化掉函数调用的 returnObject
        # 如果由一个return语句返回，真实返回值会被封装在一个ReturnObject里。
        if isinstance(rtn, ReturnObject):
            rtn = rtn.returnValue
        return rtn

    def visitFunctionDeclaration(self, ctx:PlayScriptParser.FunctionDeclarationContext):
        return self.visitFunctionBody(ctx.functionBody())

    def visitFunctionBody(self, ctx:PlayScriptParser.FunctionBodyContext):
        rtn = None
        if ctx.block():
            rtn = self.visitBlock(ctx.block())
        return rtn
