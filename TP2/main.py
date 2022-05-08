"""
/**
num i = 0.1;
str j = "";
list l = ["abc",1,"def",2];
dict d = ["abc":1,"def":2];

if(condition)
    for(element : list) {

        $text$element$text$; #same as printf("text %s text", element)

        //text
        /*
            text
        */
    }
else
    for(i = 0; i < 10; i = i + 1)
        j = j + i;
    
**/

if + else
for(;;)
for(:)
comments (//, /**/)
variable declaration (num & str & list & dictionary)
num operations (+, -, *,  /, //)
str operations (+str, +num, [::])
list operations (+value, -value, [::])
dict operations ([key], -key, [key] = value)
"""

import sys
import re
import ply.lex as lex
import ply.yacc as yacc
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


from lexer import *
from grammar1 import *






### lexer

lexer = lex.lex()

### yacc
    
parser = yacc.yacc()

### open files

f_template = open(sys.argv[1],'r')
f_yaml = open(sys.argv[2],'r')
f_output = open(sys.argv[3],'w')

### read files

content = f_template.read()
yaml_content = f_yaml.read()

### parse files

lexer.input(content)

dic = yaml.load(yaml_content, Loader=Loader)

ast = parser.parse(content)

### solve



def format(string):
    symbols = {
        '\\n':'\n',
        '\\t':'\t',
        '\\"':'\"'
    }
    for symbol in symbols:
        string = string.replace(symbol,symbols[symbol])
    return string



def evaluate_bool_expression(condition,dic):
    cond_type = condition[0]

    if(cond_type == 'id'):
        return (dic.get(condition[1],None))

    if(cond_type == 'not'):
        return not evaluate_bool_expression(condition[1],dic)

    left,right = condition[1]
    if(cond_type == 'and'):
        return evaluate_bool_expression(left,dic) and evaluate_bool_expression(right,dic)
    
    if(cond_type == 'or'):
        return evaluate_bool_expression(left,dic) or evaluate_bool_expression(right,dic)
    
    if(cond_type == '>'):
        return evaluate_expression(left,dic) > evaluate_expression(right,dic)
    
    if(cond_type == '<'):
        return evaluate_expression(left,dic) < evaluate_expression(right,dic)
    
    if(cond_type == '>='):
        return evaluate_expression(left,dic) >= evaluate_expression(right,dic)
    
    if(cond_type == '<='):
        return evaluate_expression(left,dic) <= evaluate_expression(right,dic)
    
    if(cond_type == '=='):
        return evaluate_expression(left,dic) == evaluate_expression(right,dic)
    
    if(cond_type == '!='):
        return evaluate_expression(left,dic) != evaluate_expression(right,dic)

    return False



def evaluate_expression(exp,dic):
    op_type = exp[0]

    if(op_type == 'id'):
        return dic.get(exp[1])

    if(op_type == 'num'):
        try:
            result = int(exp[1])
        except:
            result = float(exp[1])
        return result

    if(op_type == 'str'):
        return exp[1]

    if(op_type == 'index'):
        return dic[exp[1][0]][evaluate_expression(exp[1][1],dic)]

    left = evaluate_expression(exp[1][0],dic)
    right = evaluate_expression(exp[1][1],dic)

    if(op_type == 'add'):
        return left + right

    if(op_type == 'sub'):
        return left - right

    if(op_type == 'mult'):
        return left * right

    if(op_type == 'div'):
        return left / right

    return None



def solve(ast,dic,output):
    for op in ast:
        op_type = op[0]

        if op_type == 'text':
            output.write(op[1])

        elif op_type == 'section':
            solve(op[1],dic,output)

        elif op_type == 'str':
            output.write(format(op[1]))

        elif op_type == 'id':
            output.write(str(dic[op[1]]))

        elif op_type == 'for':
            var,lst,ops = op[1]
            for element in dic[lst]:
                dic[var] = element
                solve(ops,dic,output)
            dic.pop(var)

        elif op_type == 'if':
            condition,ifops,elseops = op[1]
            if(evaluate_bool_expression(condition,dic)):
                solve(ifops,dic,output)
            else:
                solve(elseops,dic,output)

        elif op_type == 'assign':
            var,exp = op[1]
            dic[var] = evaluate_expression(exp,dic)

        elif op_type == 'while':
            condition,ops = op[1]
            while(evaluate_bool_expression(condition,dic)):
                solve(ops,dic,output)



solve(ast,dic,f_output)

### exit

f_template.close()
f_yaml.close()
f_output.close()