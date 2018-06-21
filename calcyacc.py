#coding:utf-8

from calclex import  tokens
from calclex import lexer
import math

class LossRP(BaseException):
    pass

pos = None

data = ''
#tok = None

def GetData(sData):
    global data,tok
    data = sData
    lexer.input(data)
    tok = lexer.token()

def GetToken():
    global tok,pos
    pos = tok.lexpos
    tok = lexer.token()

def P_E():
    global tok
    temp = P_T()
    while (tok != None):
        if tok.type == 'PLUS':
            GetToken()
            if tok.type == 'PLUS':
                GetToken()
            elif tok.type == 'MINUS':
                GetToken()
                tok.value = -tok.value
            elif tok.type != 'NUMBER':
                #raise TypeError
                pass
            temp += P_T()
        elif tok.type == 'MINUS':
            GetToken()
            if tok.type == 'PLUS':
                GetToken()
            elif tok.type == 'MINUS':
                GetToken()
                tok.value = -tok.value
            elif tok.type != 'NUMBER':
                #raise TypeError
                pass
            temp -= P_T()
        else:
            break
    return temp

def P_T():
    global tok
    temp = P_F()
    while(tok != None):
        if tok.type == 'TIMES':
            GetToken()
            if tok.type == 'TIMES':
                GetToken()
                temp = temp ** P_F()
            else:
                temp *= P_F()
        elif tok.type == 'DIVIDE':
            GetToken()
            temp /= P_F()
        else:
            break
    return temp

def P_F():
    number = None
    global tok,pos
    if tok.type == 'NUMBER':
        number = tok.value
        GetToken()
    elif tok.type == 'LPAREN':
        GetToken()
        number = P_E()
        try:
            tok.type != 'RPAREN'
        except:
            raise LossRP
        GetToken()
    elif tok.type == 'SIN':
        GetToken()
        if tok.type == 'LPAREN':
            GetToken()
            number = math.sin(P_E())
            try:
                tok.type != 'RPAREN'
            except:
                raise LossRP
        GetToken()
    elif tok.type == 'COS':
        GetToken()
        if tok.type == 'LPAREN':
            GetToken()
            number = math.cos(P_E())
            try:
                tok.type != 'RPAREN'
            except:
                raise LossRP
        GetToken()
    else:
        pass
    return number

def GetResult():
    global tok,pos
    try:
        return P_E()
    except AttributeError:
        ErrorMsg = '不完整表达式,\n\t错误位置：%d'%pos
    except ZeroDivisionError:
        ErrorMsg = '除0，\n\t错误位置:%d'%pos
    except UserWarning:
        ErrorMsg = '不闭合的括号，\n\t错误位置:%d'%pos
    except TypeError:
        ErrorMsg = '错误的表达式，\n\t错误位置:%d'%pos
    except LossRP:
        ErrorMsg = '不闭合的括号，\n\t错误位置:%d' % pos
    return ErrorMsg


if __name__ == '__main__':
    GetData('cos(0)')
    a = GetResult()
    print(a)