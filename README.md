
# PlayScript 语言的编译器
参考：宫老师《极客时间-编译原理之美》教程：https://github.com/RichardGong/PlayWithCompiler
<br/></br>

## 介绍
这里对 `PlayScript` 的语法进行了裁剪，去掉了`Class`相关的特性，并用`Python`写了一版编译器（具体实现方法完全参考上述课程的源码）

目录介绍：
* `playscript-py`目录：编译器源码（Python文件）
* `test`目录：存放了一些测试用的play脚本
* `PlayScript.g4`文件：Antlr4 Grammar文件
* `cmt.txt`文件：存放了利用Antlr4和语法规则文件生成Python目标代码的指令

其语言特性，简要说明如下：（覆盖课程的 06、07、08、10、11、12小节）
* 支持 `int、float、string、boolean` 类型的变量的定义/赋值/运算
* 支持 `while/for/break` 流程控制
* 支持函数的定义和调用
* 支持函数一等公民，包括：可以声明一个函数类型的变量、可以对函数类型的变量进行赋值、函数类型的变量可以作为函数的形参和返回值
* 支持闭包
* 具体语言特性，可以参考`test`目录下的示例代码
<br/></br>

## 编译器程序入口：
`playscript-py/main.py`

* 功能1：打印 `AST`（以DOT文本形式）（调试用）
  + 示例：
    ```bash
    python playscript-py/main.py test/test-function-1.play -ast test/test-function-1.dot
    ```
  + 通过`Graphviz`工具，可以直观展示该AST
<br/></br>

* 功能2：打印 `Annotated AST`（以DOT文本形式）(调试用)
  + 示例：
    ```bash
    python playscript-py/main.py test/test-function-1.play -at test/test-function-1.dot
     ```
  + 通过`Graphviz`工具，可以直观展示该 annotated AST（见 `test/test-function-1.png` 图片)
  + 注意：这里只是在AST结点上附加了类型信息，其它语义信息，如作用域、引用关系，暂未画出
<br/></br>

* 功能3：运行`play`脚本
  + 示例：
    ```bash
    python playscript-py/main.py test/test-function-1.play
    ```
  + 运行该命令后，观察控制台上的输出与预期是否一致
  + 可以试试`test`目录下的其它`play`脚本

