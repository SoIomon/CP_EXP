#coding:utf-8

import ply.lex as lex

# 词法单元名列表
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
    'SIN',
    'COS'
)

# 词法单元的正则匹配
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SIN     = r'sin'
t_COS     = r'cos'

# 带操作码的正则匹配
def t_NUMBER(t):
    r'(\d+(\.\d+)?)'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# 捕捉新行
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# 忽略空格和制表符
t_ignore  = ' \t'

# 错误规则
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# 建立词法分析器
lexer = lex.lex()

if __name__ == "__main__":
    #测试用例
    data = '''cos(3)+(4*10)
            + -20 *2'''

    #传入词法分析器
    lexer.input(data)

    #打印结果
    while True:
        tok = lexer.token()
        if tok:
            print(tok)

