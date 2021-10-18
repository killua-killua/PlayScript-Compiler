from frontend import *
from ast_evaluator import *


def parseParams(args):
    res = {'scriptPath':None, 'verbose':False, '-astdump':False, 'astdump_file':None, '-atdump':False, 'atdump_file':None}
    i = 0
    while i < len(args):
        if '.play' in args[i]:
            res['scriptPath'] = args[i]
        elif args[i] == '-v':
            res['verbose'] = True
        elif args[i] == '-astdump':
            res['-astdump'] = True
            if (i+1 < len(args)) and (not args[i+1] in res):
                res['astdump_file'] = args[i+1]
                i += 1
        elif args[i] =='-atdump':
            res['-atdump'] = True
            if (i+1 < len(args)) and (not args[i+1] in res):
                res['atdump_file'] = args[i+1]
                i += 1
        i += 1
    return res


def main(argv):
    args = argv[1:] if len(argv)>1 else []
    # print(args)
    params = parseParams(args)

    if params['scriptPath']:
        scriptPath = params['scriptPath']
        prog = ''
        with open(scriptPath, 'r', encoding='utf-8') as fin:
            prog = fin.read()
        
        at:AnnotatedTree = translate(prog)

        if params['-astdump'] or params['-atdump']:
            dumper = Dumper(at)
            if params['-astdump']:
                f = params['astdump_file']
                f = open(f, 'w') if f else f
                dumper.dump_ast(f)
                if f:
                    f.close()
            if params['-atdump']:
                f = params['atdump_file']
                f = open(f, 'w') if f else f
                dumper.dump_at(f)
                if f:
                    f.close()
        elif not at.hasCompilationError():
            eval = ASTEvaluator(at)
            eval.visit(at.ast)
        else:
            at.show_log()
    else:
        # REPL
        # 静态作用域，不便于实现 REPL
        print('Not support REPL yet')
        # compiler = PlayScriptCompiler()

        # prog = ''
        # print()
        # print('>> ', end='')
        # while True:
        #     line = input()
        #     prog += line
        #     if len(prog) > 0 and prog[-1] == ';':
        #         try:
        #             at:AnnotatedTree = compiler.compile(prog)
        #             # TODO: if compile error, do not excute
        #             compiler.excute(at)
        #         except Exception as e:
        #             print(e)
        #         prog = ''
        #         print(">> ", end='')



if __name__ == '__main__':
    main(sys.argv)
    # path = r'C:\Users\HP\Desktop\test\test-function-7-closure-fibonacci.play'
    # argv = [0, path]
    # main(argv)

    


# # 将一个目录下的所有 play脚本对应的的 AST，生成 DOT文件 和 PNG图片
# import subprocess

# dir_path = r'C:\Users\HP\Desktop\test'

# for name in os.listdir(dir_path):
#     if name.endswith('.play'):
#         path = os.path.join(dir_path, name)
#         dot_name = name.replace('.play', '.dot')
#         dot_path = os.path.join(dir_path, dot_name)
#         argv = [0, path, '-atdump', dot_path]
#         main(argv)

# for name in os.listdir(dir_path):
#     if name.endswith('.dot'):
#         png_name = name.replace('.dot', '.png')
#         path = os.path.join(dir_path, name)
#         png_path = os.path.join(dir_path, png_name)
#         cmd_str = 'dot -Tpng ' + path + ' -o ' + png_path
#         subprocess.check_output(cmd_str)
